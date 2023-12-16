import dateparser
import json
import xml.etree.ElementTree as ET


def determine_format(data):
    try:
        json.loads(data)
        return "json"

    except ValueError:
        pass

    try:
        ET.fromstring(data)
        return "xml"
    
    except ET.ParseError:
        pass

    return "Unknown"


def process_date(date):
    res = ""
    try:
        res = dateparser.parse(date, date_formats=["%d.%m %H:%M"])

    except Exception as e:
        print(e)
        res = ""

    finally:
        return res
