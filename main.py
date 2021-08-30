import uvicorn
from fastapi import FastAPI

from global_var import templates
from router import web, auth
from utils.db.database import Base, engine
from utils.i18n.language import languages

Base.metadata.create_all(bind=engine)
app = FastAPI()


# register filter
def tran(value, lang='en'):
    return languages[lang][value]


templates.env.filters["tran"] = tran

app.include_router(web.router, tags=['web'])
app.include_router(auth.router, tags=['auth'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
