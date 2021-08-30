from typing import List, Dict, Any

from pydantic import BaseModel

import task_system_schemas
from global_var import templates


class FormError(BaseModel):
    result_errors: Dict[str, List[str]]


def get_errors_msgs(errors: List[Dict[str, Any]]):
    result_errors: Dict[str, List[str]] = {}
    for error in errors:
        name = error['loc'][0]
        msg = error['msg']
        if name not in result_errors:
            result_errors[name] = [msg]
        else:
            result_errors[name].append(msg)

    return FormError(result_errors=result_errors)


# TODO add filter to handle the form error
def form_errors(value, lang='en'):
    pass


templates.env.filters["form_errors"] = form_errors