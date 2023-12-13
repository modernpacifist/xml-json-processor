import fastapi


app = fastapi.FastAPI()


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/api/json")
async def process_json():
    return {"hello": "world"}


@app.get("/api/xml")
async def process_xml():
    return {"hello": "world"}
