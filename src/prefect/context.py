"""
This module contains async and thread safe variables for passing runtime context data
"""
from contextvars import ContextVar
from typing import Optional, TypeVar, Union, Type
from uuid import UUID

import pendulum
from anyio.abc import BlockingPortal
from pendulum.datetime import DateTime
from pydantic import BaseModel, Field

from prefect.client import OrionClient
from prefect.executors import BaseExecutor
from prefect.flows import Flow
from prefect.tasks import Task

T = TypeVar("T")


class ContextModel(BaseModel):
    """
    A base model for context data that forbids mutation and extra data while providing
    a context manager
    """

    # The context variable for storing data must be defined by the child class
    __var__: ContextVar

    class Config:
        allow_mutation = False
        arbitrary_types_allowed = True
        extra = "forbid"

    def __enter__(self):
        # We've frozen the rest of the data on the class but we'd like to still store
        # this token for resetting on context exit
        object.__setattr__(self, "__token", self.__var__.set(self))
        return self

    def __exit__(self, *_):
        self.__var__.reset(getattr(self, "__token"))

    @classmethod
    def get(cls: Type[T]) -> Optional[T]:
        return cls.__var__.get(None)


class RunContext(ContextModel):
    start_time: DateTime = Field(default_factory=lambda: pendulum.now("UTC"))


class FlowRunContext(RunContext):
    flow: Flow
    flow_run_id: UUID
    client: OrionClient
    executor: BaseExecutor
    task_run_portal: BlockingPortal = None

    __var__ = ContextVar("flow_run")


class TaskRunContext(RunContext):
    task: Task
    task_run_id: UUID
    flow_run_id: UUID
    client: OrionClient

    __var__ = ContextVar("task_run")


def get_run_context() -> Union[FlowRunContext, TaskRunContext]:
    task_run_ctx = TaskRunContext.get()
    if task_run_ctx:
        return task_run_ctx

    flow_run_ctx = FlowRunContext.get()
    if flow_run_ctx:
        return flow_run_ctx

    raise RuntimeError(
        "No run context available. You are not in a flow or task run context."
    )
