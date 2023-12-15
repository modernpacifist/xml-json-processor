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
    # processed_data = ""

    if model.js_data is not None:
        CONTEXT.strategy = JsonProcessingStrategy()
        print("json chosen")

    if model.xml_data is not None:
        CONTEXT.strategy = XmlProcessingStrategy()
        print("xml chosen")


    return {"result": CONTEXT.process(model.js_data)}
    # return {"result": processed_data}
