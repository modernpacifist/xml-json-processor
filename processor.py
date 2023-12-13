import json

class Processor():
    def process(self):
        raise NotImplementedError


class CsvProcessor(Processor):
    def __init__(self):
        return self

    def process(self):
        return json.dumps({"sample": "hehe"})


class XmlProcessor(Processor):
    def __init__(self):
        return self

    def process(self):
        return 
