from fastapi import FastAPI, Request, Response, status
from models import AnyFormatModel
from formathandler import FormatHandler, JsonProcessingStrategy, XmlProcessingStrategy


app = FastAPI()


CONTEXT = FormatHandler(None)


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
            print("None chosen")
            response.status_code = status.HTTP_400_BAD_REQUEST


    # return {"result": CONTEXT.process(model.js_data)}
    return {"result": processed_data}
