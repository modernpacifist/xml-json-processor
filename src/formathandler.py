import json
import xml.etree.ElementTree as ET

from logging import getLogger
from config import setup_logging
from functools import singledispatch


setup_logging()

LOGGER = getLogger(__name__)


class FormatHandler:
    @staticmethod
    def determine_format(data):
        if isinstance(data, list):
            data = data[0]

        try:
            json.loads(data)
            return "json"

        except ValueError:
            LOGGER.warning("determine_format: could not load data as json")
            pass

        try:
            ET.fromstring(data)
            return "xml"
        
        except ET.ParseError:
            LOGGER.warning("determine_format: could not load data as xml")
            pass

        return "Unknown"
