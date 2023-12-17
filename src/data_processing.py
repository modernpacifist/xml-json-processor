import logging
import dateparser
import json
import xml.etree.ElementTree as ET


LOGGER = logging.getLogger(__name__)


def determine_format(data):
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


def process_date(date_string):
    try:
        dt_object = dateparser.parse(date_string, date_formats=["%d.%m.%Y"])
        if dt_object is not None:
            return dt_object.strftime("%m-%d-%Y")

    except Exception as e:
        LOGGER.warning(f"{e}")
        return ""
