import fastapi

from models import JsonModel
from formathandler import FormatHandler, JsonProcessingStrategy, XmlProcessingStrategy


app = fastapi.FastAPI()


CONTEXT = FormatHandler(None)


@app.get("/")
async def read_root():
    return {"status": "healthy"}


@app.post("/api/json")
async def process_json(model: JsonModel):
    CONTEXT.strategy = JsonProcessingStrategy()

    print(model)

    result = CONTEXT.process("json_data")

    return result


@app.get("/api/xml")
async def process_xml():
    CONTEXT.strategy = XmlProcessingStrategy()

    return CONTEXT.process("xml_data")
