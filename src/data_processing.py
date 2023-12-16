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


def process_date(date_string):
    try:
        dt_object = dateparser.parse(date_string, date_formats=["%d.%m.%Y"])
        return dt_object.strftime("%m-%d-%Y")

    except Exception as e:
        print(e)
        return ""
