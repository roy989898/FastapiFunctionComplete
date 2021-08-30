from fastapi import FastAPI
import uvicorn
from starlette.requests import Request

from global_var import templates

app = FastAPI()


@app.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
