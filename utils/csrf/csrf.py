from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel


class CsrfSettings(BaseModel):
    secret_key: str = 'asdasdasd123123'


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()
