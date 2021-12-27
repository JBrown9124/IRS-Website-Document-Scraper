import datetime
from typing import Dict, Union


class Form(object):
    def __init__(
            self, form_number: str, form_title: str, min_year: int
    ) -> Dict[str, Union[str, int]]:
        self.form_number = form_number
        self.form_title = form_title
        self.min_year = min_year
        self.max_year = datetime.date.today().year

    def to_dict(self):
        return {
            "form_number": self.form_number,
            "form_title": self.form_title,
            "min_year": self.min_year,
            "max_year": self.max_year,
        }
