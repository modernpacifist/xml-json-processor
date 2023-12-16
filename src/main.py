from fastapi import FastAPI, Response, status
from models import AnyFormatModel
from formathandler import FormatProcessor, JsonProcessingStrategy, XmlProcessingStrategy

import data_processing

app = FastAPI()


CONTEXT = FormatProcessor(None)


@app.get("/")
async def read_root():
    return {"status": "healthy"}


@app.post("/api/tree", status_code=200)
async def process_tree(model: AnyFormatModel, response: Response):
    match data_processing.determine_format(model.tree):
        case "json":
            CONTEXT.strategy = JsonProcessingStrategy()

        case "xml":
            CONTEXT.strategy = XmlProcessingStrategy()

        case _:
            print("None chosen")
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"result": "Check your tree, it might contain invalid data"}
    
    return {"result": CONTEXT.process(model.tree)}
