from fastapi import FastAPI, Response, status, Request
from models import AnyFormatModel
from formathandler import FormatProcessor, JsonProcessingStrategy, XmlProcessingStrategy

import xml.etree.ElementTree as ET

app = FastAPI()


CONTEXT = FormatProcessor(None)


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
    
    processed_data = CONTEXT.process(model.tree)

    return {"result": processed_data}


@app.post("/xml_handler", status_code=200)
async def xml_handler(request: Request):
    xml_data = await request.body()
    root = ET.fromstring(xml_data)
    # Process the XML data
    for i in root:
        print(f"{i.tag}: {root.find(i.tag).text}")


    return {"message": "XML data processed successfully"}

