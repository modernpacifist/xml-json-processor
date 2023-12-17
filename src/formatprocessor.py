import json
import xml.etree.ElementTree as ET
import xmltodict

from abc import ABC, abstractmethod
from logging import getLogger

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
    def process_single_entity(self, data):
        try:
            js_object = json.loads(data)

            if "date" in js_object.keys():
                js_object["date"] = data_processing.process_date(js_object["date"])

            if "deadline" in js_object.keys():
                js_object["deadline"] = data_processing.process_deadline(js_object["deadline"])

            return js_object

        except Exception as e:
            LOGGER.error(e)
    
    def merge(self, processed_data_list):
        merged_dict = dict()
        for d in processed_data_list:
            for key, value in d.items():
                if key in merged_dict:
                    count = 2
                    while f"{key}_{count}" in merged_dict:
                        count += 1
                    key = f"{key}_{count}"

                merged_dict[key] = value

        return merged_dict

    def process(self, data):
        try:
            processed_data_list = [self.process_single_entity(i) for i in data]

            return self.merge(processed_data_list)

        except Exception as e:
            LOGGER.error(e)



class XmlProcessingStrategy(Strategy):
    def process_single_entity(self, data):
        try:
            root = ET.fromstring(data)

            tags = [i.tag for i in root]

            if "date" in tags:
                el = root.find("date")
                if el is not None:
                    el.text = data_processing.process_date(el.text)

            if "deadline" in tags:
                el = root.find("deadline")
                if el is not None:
                    el.text = data_processing.process_deadline(el.text)

            return xmltodict.parse(ET.tostring(root))["root"]

        except Exception as e:
            LOGGER.error(e)

    def merge(self, processed_data_list):
        merged_dict = dict()
        for d in processed_data_list:
            for key, value in d.items():
                if key in merged_dict:
                    count = 2
                    while f"{key}_{count}" in merged_dict:
                        count += 1
                    key = f"{key}_{count}"

                merged_dict[key] = value

        return merged_dict

    def process(self, data):
        try:
            processed_data_list = [self.process_single_entity(i) for i in data]

            return self.merge(processed_data_list)

        except Exception as e:
            LOGGER.error(e)
