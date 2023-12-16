from fastapi import FastAPI, Response, status
from models import AnyFormatModel
from formathandler import FormatProcessor, JsonProcessingStrategy, XmlProcessingStrategy


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
