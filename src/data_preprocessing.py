import dateparser


def process_date(date):
    res = ""
    try:
        res = dateparser.parse(date, date_formats=["%d.%m %H:%M"])

    except Exception as e:


    finally:
        return res
