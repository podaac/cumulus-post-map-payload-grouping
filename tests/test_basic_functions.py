import pytest

from cumulus_post_map_payload_grouping.cumulus_post_map_payload_grouping import lambda_handler


lambda_input = 
{
    "cma": {
        "event": [
            {
                "dummy_data": "dummy_value"
            },
            {
                "dummy_data": "dummy_value2"
            }
        ]
    }
}

lambda_input_bad = 
{
    "cma": {
        "event": [
            {
                "Status": "FAILED",
                "Error": "ValueError",
                "Cause": "{\"errorMessage\":\"This safe_unpack run detected errors. See the Summmary of Errors log above for more details.\",\"errorType\":\"ValueError\",\"requestId\":\"402e850e-f1c5-402c-9d00-cdfd57484d62\",\"stackTrace\":[\"  File \\\"/function/lambda_safe_unpack_handler.py\\\", line 117, in handler\\n    return SafeUnpackCumulusTask.cumulus_handler(event, context=context)\\n\",\"  File \\\"/function/cumulus_process/process.py\\\", line 315, in cumulus_handler\\n    return run_cumulus_task(cls.handler, event, context)\\n\",\"  File \\\"/function/run_cumulus_task.py\\\", line 85, in run_cumulus_task\\n    return handle_task_exception(exception, cumulus_message, logger)\\n\",\"  File \\\"/function/run_cumulus_task.py\\\", line 83, in run_cumulus_task\\n    task_response = task_function(nested_event, context, **taskargs)\\n\",\"  File \\\"/function/cumulus_process/process.py\\\", line 310, in handler\\n    return cls.run(path=path, noclean=noclean, **event)\\n\",\"  File \\\"/function/cumulus_process/process.py\\\", line 337, in run\\n    output = process.process()\\n\",\"  File \\\"/function/lambda_safe_unpack_handler.py\\\", line 110, in process\\n    raise ValueError('This safe_unpack run detected errors. '\\n\"]}"
            },
            {
                "Status": "FAILED",
                "Error": "ValueError",
                "Cause": "{\"errorMessage\":\"This safe_unpack run detected errors. See the Summmary of Errors log above for more details.\",\"errorType\":\"ValueError\",\"requestId\":\"37094b0f-d0f6-4031-b0a9-33de05132660\",\"stackTrace\":[\"  File \\\"/function/lambda_safe_unpack_handler.py\\\", line 117, in handler\\n    return SafeUnpackCumulusTask.cumulus_handler(event, context=context)\\n\",\"  File \\\"/function/cumulus_process/process.py\\\", line 315, in cumulus_handler\\n    return run_cumulus_task(cls.handler, event, context)\\n\",\"  File \\\"/function/run_cumulus_task.py\\\", line 85, in run_cumulus_task\\n    return handle_task_exception(exception, cumulus_message, logger)\\n\",\"  File \\\"/function/run_cumulus_task.py\\\", line 83, in run_cumulus_task\\n    task_response = task_function(nested_event, context, **taskargs)\\n\",\"  File \\\"/function/cumulus_process/process.py\\\", line 310, in handler\\n    return cls.run(path=path, noclean=noclean, **event)\\n\",\"  File \\\"/function/cumulus_process/process.py\\\", line 337, in run\\n    output = process.process()\\n\",\"  File \\\"/function/lambda_safe_unpack_handler.py\\\", line 110, in process\\n    raise ValueError('This safe_unpack run detected errors. '\\n\"]}"
            }
        ]
    }
}


def test_basic_input_output():
    resp = lambda_handler(lambda_input, {})
    assert resp['statusCode'] == 200


def test_basic_input_failed_map():
    with pytest.raises(Exception):
        resp = lambda_handler(lambda_input_bad, {})
