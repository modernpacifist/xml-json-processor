import json
from logging import getLogger
import xml.etree.ElementTree as ET
import xmltodict

from abc import ABC, abstractmethod

# local
import data_processing

from config import setup_logging


setup_logging()

LOGGER = getLogger(__name__)


class FormatProcessor:
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
        try:
            js_object = json.loads(data)
            print(js_object)

            if 'date' in js_object.keys():
                js_object['date'] = data_processing.process_date(js_object['date'])

            if 'deadline' in js_object.keys():
                js_object['deadline'] = data_processing.process_deadline(js_object['deadline'])

            print(type(js_object))

            return js_object

        except Exception as e:
            LOGGER.error(e)


class XmlProcessingStrategy(Strategy):
    def process(self, data):
        try:
            root = ET.fromstring(data)

            tags = [i.tag for i in root]

            if "date" in tags:
                el = root.find("date")
                if el is not None:
                    el.text = data_processing.process_date(el.text)

            return xmltodict.parse(ET.tostring(root))["root"]

        except Exception as e:
            LOGGER.error(e)