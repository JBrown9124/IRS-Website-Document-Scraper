import datetime
from typing import Union


def validate_date(date_text: str) -> Union[None, str]:
    try:
        datetime.datetime.strptime(date_text, "%Y")
        return date_text
    except ValueError:
        print("Incorrect date format, should be YYYY")
