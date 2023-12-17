import dateparser
import json
import xml.etree.ElementTree as ET

from config import LOGGER

# LOGGER = logging.getLogger(__name__)




def process_date(date_string):
    try:
        dt_object = dateparser.parse(date_string, date_formats=["%d.%m.%Y"])
        if dt_object is not None:
            return dt_object.strftime("%m-%d-%Y")

    except Exception as e:
        LOGGER.warning(f"{e}")
        return ""
