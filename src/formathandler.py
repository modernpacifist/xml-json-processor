import json
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod

# local
import data_processing


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
        res = ""

        try:
            js_object = json.loads(data)
            print(js_object)

            if 'date' in js_object.keys():
                js_object['date'] = data_processing.process_date(js_object['date'])

            print(type(js_object))

            res = js_object
            # print(type(js_object['date']))

        except Exception as e:
            print(e)
            res = str(e)

        return res


class XmlProcessingStrategy(Strategy):
    def process(self, data):
        res = ""

        try:
            root = ET.fromstring(data)

            if 'date' in root.attrib:
                print('hehe')

            for i in root:
                value = root.find(i.tag)
                if value is None:
                    continue

                print(f"{i.tag}: {value.text}")

        except Exception as e:
            print(e)
            res = str(e)

        return res
