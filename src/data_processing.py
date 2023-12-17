import re
import dateparser

from logging import getLogger
from config import setup_logging


setup_logging()

LOGGER = getLogger(__name__)


def process_date(date_string):
    try:
        dt_object = dateparser.parse(date_string)
        if dt_object is not None:
            return dt_object.strftime("%d-%m-%Y")

    except Exception as e:
        LOGGER.warning(f"Date {date_string} could not be parsed: {e}")
        return ""


def process_deadline(deadline_string):
    try:
        pattern = r"\b(\d+) days\b"

        match = re.search(pattern, deadline_string)


        return deadline_string

    except Exception as e:
        LOGGER.warning(f"Date {deadline_string} could not be parsed: {e}")
        return ""
