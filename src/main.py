# import fastapi
from fastapi import FastAPI
# from fastapi_xml import XmlBody, XmlResponse

from models import DataModel
from formathandler import FormatHandler, JsonProcessingStrategy, XmlProcessingStrategy


app = FastAPI()


CONTEXT = FormatHandler(None)


@app.get("/")
async def read_root():
    return {"status": "healthy"}


@app.post("/api/json")
async def process_json(model: DataModel):
    CONTEXT.strategy = JsonProcessingStrategy()

    print(model)



    result = CONTEXT.process("json_data")

    return result


# @app.post("/api/xml", response_class=XMLResponse, content_type="application/xml")
@app.post("/api/xml")
async def process_xml(model: DataModel):
    CONTEXT.strategy = XmlProcessingStrategy()

    return CONTEXT.process("xml_data")
