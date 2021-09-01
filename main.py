import uvicorn
from fastapi import FastAPI
from loguru import logger
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse

from exception.Exception import MyException
from global_var import templates
from router import web, auth
from utils.db.database import Base, engine
from utils.i18n.language import languages
from utils.log import log_set_up

Base.metadata.create_all(bind=engine)
app = FastAPI()
log_set_up.setup()


# register filter
def tran(value, lang='en'):
    return languages[lang][value]


templates.env.filters["tran"] = tran


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        # you probably want some kind of logging here
        logger.exception("Global")
        return Response("Internal server error", status_code=500)


app.middleware('http')(catch_exceptions_middleware)
app.include_router(web.router, tags=['web'])
app.include_router(auth.router, tags=['auth'])

# @app.exception_handler(MyException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str('My exception'), status_code=404)


if __name__ == "__main__":
    logger.debug('App start')
    uvicorn.run(app, host="0.0.0.0", port=8000)
