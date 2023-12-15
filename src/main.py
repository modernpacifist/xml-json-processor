import time

from fastapi import FastAPI, Request, Response, status
from models import AnyFormatModel
from formathandler import FormatHandler, JsonProcessingStrategy, XmlProcessingStrategy


app = FastAPI()


CONTEXT = FormatHandler(None)


# @app.middleware("http")
# async def process_format(request: Request, call_next):
    # start_time = time.time()
    # response = await call_next(request)
    # process_time = time.time() - start_time
    # response.headers["X-Process-Time"] = str(process_time)
    # return response


@app.get("/")
async def read_root():
    return {"status": "healthy"}


@app.post("/api/tree", status_code=200)
async def process_tree(model: AnyFormatModel, response: Response):
    match model.format:
        case "json":
            CONTEXT.strategy = JsonProcessingStrategy()
            print("json chosen")

        case "xml":
            CONTEXT.strategy = XmlProcessingStrategy()
            print("xml chosen")

        case _:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"result": "only json and xml formats are supported"}
    
    return {"result": CONTEXT.process(model.data)}
