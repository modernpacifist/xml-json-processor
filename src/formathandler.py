import json
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod

# local
import data_preprocessing


class FormatHandler:
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
        res = ""

        try:
            res = json.loads(data)

        except Exception as e:
            print(e)
            res = str(e)

        return res


class XmlProcessingStrategy(Strategy):
    def process(self, data):
        res = ""

        try:
            root = ET.fromstring(data)

        except Exception as e:
            print(e)
            res = str(e)

        return res
