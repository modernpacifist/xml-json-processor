import dateparser
import json
import xml.etree.ElementTree as ET


def determine_format(data):
    if data.startswith(b"{") and data.endswith(b"}"):
        try:
            json.loads(data)
            return "JSON"

        except ValueError:
            pass

    if data.startswith(b"<") and data.endswith(b">"):
        try:
            ET.fromstring(data)
            return "XML"
        
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
