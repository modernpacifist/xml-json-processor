from fastapi import FastAPI, Response, status, Request
from models import AnyFormatModel
from formathandler import FormatProcessor, JsonProcessingStrategy, XmlProcessingStrategy

import xml.etree.ElementTree as ET
import data_processing

app = FastAPI()


CONTEXT = FormatProcessor(None)


@app.get("/")
async def read_root():
    return {"status": "healthy"}


@app.post("/api/tree", status_code=200)
async def process_tree(model: AnyFormatModel, response: Response):
    # data = await request.body()
    data = model.tree

    match data_processing.determine_format(data):
        case "json":
            CONTEXT.strategy = JsonProcessingStrategy()
            print("json chosen")

        case "xml":
            CONTEXT.strategy = XmlProcessingStrategy()
            print("xml chosen")

        case _:
            print("None chosen")
            response.status_code = status.HTTP_400_BAD_REQUEST
    
    # processed_data = CONTEXT.process(model.tree)

    # return {"result": processed_data}
    return {"result": ""}


# @app.post("/api/xml_handler", status_code=200)
# async def xml_handler(request: Request):
    # xml_data = await request.body()
    # root = ET.fromstring(xml_data)
    # for i in root:
        # print(f"{i.tag}: {root.find(i.tag).text}")

    # return {"message": "XML data processed successfully"}
