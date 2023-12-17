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
    def find_key(dictionary, value):
        for key, values in dictionary.items():
            if value in values:
                return key
        return None


    date_units_map = {
        "day": ["day", "days", "день", "дней", "дня"],
        "week": ["week", "weeks", "неделя", "недель"],
        "month": ["month", "months", "месяц", "месяца", "месяцев"],
        "year": ["year", "years", "год", "года", "лет"],
    }

    res = ""

    try:
        pattern = r"\b(?P<qty>\d+) (?P<units>day[s]?|week[s]?|неделя|недель|дня|день|дней|месяца|месяцев|месяц|год|года|лет|month[s]?|year[s]?)\b"

        match = re.search(pattern, deadline_string)

        if match is None:
            return res
        
        qty = match.group("qty")
        units = match.group("units")

        k = find_key(date_units_map, units)
        print(k)
        print(k)

        match k:
            case "day":
                res = f"0_0_0_{qty}"

            case "week":
                res = f"0_0_{qty}_0"

            case "month":
                res =  f"0_{qty}_0_0"

            case "year":
                res =  f"{qty}_0_0_0"

        return res

    except Exception as e:
        LOGGER.warning(f"Date {deadline_string} could not be parsed: {e}")
        return ""
