---
sidebarDepth: 2
editLink: false
---
# Great Expectations Task

::: tip Verified by Prefect
<div class="verified-task">
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none">
<circle cx="24" cy="24" r="24" fill="#42b983"/>
<circle cx="24" cy="24" r="9" stroke="#fff" stroke-width="2"/>
<path d="M19 24L22.4375 27L29 20.5" stroke="#fff" stroke-width="2"/>
</svg>
<div>
These tasks have been tested and verified by Prefect.
</div>
</div>
:::

---

A collection of tasks for interacting with Great Expectations deployments and APIs.

Note that all tasks currently require being executed in an environment where the great expectations configuration directory can be found; 
learn more about how to initialize a great expectation deployment [on their Getting Started docs](https://docs.greatexpectations.io/en/latest/intro.html#how-do-i-get-started).
 ## RunGreatExpectationsValidation
 <div class='class-sig' id='prefect-tasks-great-expectations-checkpoints-rungreatexpectationsvalidation'><p class="prefect-sig">class </p><p class="prefect-class">prefect.tasks.great_expectations.checkpoints.RunGreatExpectationsValidation</p>(checkpoint_name=None, context=None, assets_to_validate=None, batch_kwargs=None, expectation_suite_name=None, context_root_dir=None, runtime_environment=None, run_name=None, run_info_at_end=True, disable_markdown_artifact=False, validation_operator=&quot;action_list_operator&quot;, evaluation_parameters=None, **kwargs)<span class="source"><a href="https://github.com/PrefectHQ/prefect/blob/master/src/prefect/tasks/great_expectations/checkpoints.py#L23">[source]</a></span></div>

Task for running data validation with Great Expectations. Works with both the Great Expectations v2 (batch_kwargs) and v3 (Batch Request) APIs.

Example using the GE getting started tutorial: https://github.com/superconductive/ge_tutorials/tree/main/getting_started_tutorial_final_v3_api

The task can be used to run validation in one of the following ways:

1. checkpoint_name: the name of a pre-configured checkpoint (which bundles expectation suites and batch_kwargs). This is the preferred option. 2. expectation_suite AND batch_kwargs, where batch_kwargs is a dict. This will only work with the Great Expectations v2 API. 3. assets_to_validate: a list of dicts of expectation_suite + batch_kwargs. This will only work with the Great Expectations v2 API.

To create a checkpoint you can use: - for the v2 API: `great_expectations checkpoint new <expectations_suite_name> <checkpoint_name>` - for the v3 API: `great_expectations --v3-api checkpoint new <checkpoint_name>`

Here is an example that can be used with both v2 and v3 API provided that the checkpoint has been already created, as described above: 
```python
from prefect import Flow, Parameter
from prefect.tasks.great_expectations import RunGreatExpectationsValidation

validation_task = RunGreatExpectationsValidation()

with Flow("ge_test") as flow:
    checkpoint_name = Parameter("checkpoint_name")
    prev_run_row_count = 100  # can be taken eg. from Prefect KV store
    validation_task(
        checkpoint_name=checkpoint_name,
        evaluation_parameters=dict(prev_run_row_count=prev_run_row_count),
    )

flow.run(parameters={"checkpoint_name": "my_checkpoint"})

```


**Args**:     <ul class="args"><li class="args">`checkpoint_name (str, optional)`: the name of a pre-configured checkpoint; should match the         filename of the checkpoint without the extension. Required when using the Great         Expectations v3 API.     </li><li class="args">`context (DataContext, optional)`: an in-memory GE DataContext object. e.g.         `ge.data_context.DataContext()` If not provided then `context_root_dir` will be used to         look for one.     </li><li class="args">`assets_to_validate (list, optional)`: A list of assets to validate when running the         validation operator. Only used in the Great Expectations v2 API     </li><li class="args">`batch_kwargs (dict, optional)`: a dictionary of batch kwargs to be used when validating         assets. Only used in the Great Expectations v2 API     </li><li class="args">`expectation_suite_name (str, optional)`: the name of an expectation suite to be used when         validating assets. Only used in the Great Expectations v2 API     </li><li class="args">`context_root_dir (str, optional)`: the absolute or relative path to the directory holding         your `great_expectations.yml`     </li><li class="args">`runtime_environment (dict, optional)`: a dictionary of great expectation config key-value         pairs to overwrite your config in `great_expectations.yml`     </li><li class="args">`run_name (str, optional)`: the name of this  Great Expectation validation run; defaults to         the task slug     </li><li class="args">`run_info_at_end (bool, optional)`: add run info to the end of the artifact generated by this         task. Defaults to `True`.     </li><li class="args">`disable_markdown_artifact (bool, optional)`: toggle the posting of a markdown artifact from         this tasks. Defaults to `False`.     </li><li class="args">`validation_operator (str, optional)`: configure the actions to be executed after running         validation. Defaults to `action_list_operator`     </li><li class="args">`evaluation_parameters (Optional[dict], optional)`: the evaluation parameters to use when         running validation. For more information, see         [example](/api/latest/tasks/great_expectations.html#rungreatexpectationsvalidation)         and         [docs](https://docs.greatexpectations.io/en/latest/reference/core_concepts/evaluation_parameters.html).     </li><li class="args">`**kwargs (dict, optional)`: additional keyword arguments to pass to the Task constructor</li></ul>

|methods: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|:----|
 | <div class='method-sig' id='prefect-tasks-great-expectations-checkpoints-rungreatexpectationsvalidation-run'><p class="prefect-class">prefect.tasks.great_expectations.checkpoints.RunGreatExpectationsValidation.run</p>(checkpoint_name=None, context=None, assets_to_validate=None, batch_kwargs=None, expectation_suite_name=None, context_root_dir=None, runtime_environment=None, run_name=None, run_info_at_end=True, disable_markdown_artifact=False, validation_operator=&quot;action_list_operator&quot;, evaluation_parameters=None)<span class="source"><a href="https://github.com/PrefectHQ/prefect/blob/master/src/prefect/tasks/great_expectations/checkpoints.py#L128">[source]</a></span></div>
<p class="methods">Task run method.<br><br>**Args**:     <ul class="args"><li class="args">`checkpoint_name (str, optional)`: the name of the checkpoint; should match the filename of         the checkpoint without the extension. This is required for using the Great         Expectations v3 API.     </li><li class="args">`context (DataContext, optional)`: an in-memory GE DataContext object. e.g.         `ge.data_context.DataContext()` If not provided then `context_root_dir` will be used to         look for one.     </li><li class="args">`assets_to_validate (list, optional)`: A list of assets to validate when running the         validation operator. Only used in the Great Expectations v2 API     </li><li class="args">`batch_kwargs (dict, optional)`: a dictionary of batch kwargs to be used when validating         assets. Only used in the Great Expectations v2 API     </li><li class="args">`expectation_suite_name (str, optional)`: the name of an expectation suite to be used when         validating assets. Only used in the Great Expectations v2 API     </li><li class="args">`context_root_dir (str, optional)`: the absolute or relative path to the directory holding         your `great_expectations.yml`     </li><li class="args">`runtime_environment (dict, optional)`: a dictionary of great expectation config key-value         pairs to overwrite your config in `great_expectations.yml`     </li><li class="args">`run_name (str, optional)`: the name of this  Great Expectation validation run; defaults to         the task slug     </li><li class="args">`run_info_at_end (bool, optional)`: add run info to the end of the artifact generated by this         task. Defaults to `True`.     </li><li class="args">`disable_markdown_artifact (bool, optional)`: toggle the posting of a markdown artifact from         this tasks. Defaults to `False`.     </li><li class="args">`evaluation_parameters (Optional[dict], optional)`: the evaluation parameters to use when         running validation. For more information, see         [example](/latest/tasks/great_expectations.html#rungreatexpectationsvalidation)         and         [docs](https://docs.greatexpectations.io/en/latest/reference/core_concepts/evaluation_parameters.html).     </li><li class="args">`validation_operator (str, optional)`: configure the actions to be executed after running         validation. Defaults to `action_list_operator`.</li></ul> **Raises**:     <ul class="args"><li class="args">'signals.FAIL' if the validation was not a success</li></ul><br><br>**Returns**:     <ul class="args"></ul>         ('great_expectations.checkpoint.checkpoint.CheckpointResult'):         The Great Expectations metadata returned from running the provided checkpoint if a         checkpoint name is provided.</p>|

---
<br>


<p class="auto-gen">This documentation was auto-generated from commit <a href='https://github.com/PrefectHQ/prefect/commit/n/a'>n/a</a> </br>on February 23, 2022 at 19:26 UTC</p>