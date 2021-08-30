from fastapi import FastAPI
import uvicorn
from starlette.requests import Request

from global_var import templates
from utils.i18n.language import languages

app = FastAPI()

# register filter
def tran(value, lang='en'):
    return languages[lang][value]


templates.env.filters["tran"] = tran


@app.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
