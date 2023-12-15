import json

from abc import ABC, abstractmethod


class FormatHandler():
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def process(self, data):
        return self._strategy.process(data)


class Strategy(ABC):
    @abstractmethod
    def process(self, data):
        pass


class JsonProcessingStrategy(Strategy):
    def process(self, data):
        return json.loads(data)


class XmlProcessingStrategy(Strategy):
    def process(self, data):
        return {"XmlProcessor": data}
