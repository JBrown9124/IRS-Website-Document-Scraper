import sys
from ResponseModels.form import Form
from typing import List, Union
from Helpers.soup_helpers.make_soup import make_soup
from Helpers.download_documents_helpers.download_pdf import download_pdf
from Helpers.validation_helpers.validate_date import validate_date


class IRSFormProcessor(object):
    def __init__(self, form_names: List[str], cmd: str,
                 range_of_years: List[str] = []):
        self.form_names = form_names
        self.irs_forms = []
        self.cmd = cmd
        if len(range_of_years) >= 2:
            self.range_of_years = {
                validate_date(str(year))
                for year in
                range(int(range_of_years[0]), int(range_of_years[-1]) + 1)
            }
        for name in self.form_names:
            stripped_lowercased_name = name.strip().lower()
            self.irs_forms += self.handle_names(stripped_lowercased_name)

    def handle_names(self, product_number: str) -> List[Union[Form, None]]:
        responses = []
        max_int = sys.maxsize

        for page_num in range(0, max_int, 200):

            soup = make_soup(product_number, page_num)

            soup_results = soup.find_all(
                "a",
                string=lambda
                    text: text is not None and product_number == text.lower(),
            )
            if len(soup_results) == 0:
                break

            for soup_result in soup_results:
                pdf = soup_result["href"]
                form_number_siblings = soup_result.parent.find_next_siblings()
                form_number = soup_result.parent.text.strip()
                min_year = form_number_siblings[1].string.strip()
                form_title = form_number_siblings[0].string.strip()

                if self.cmd == "download documents":
                    if min_year not in self.range_of_years:
                        continue
                    filename = f"{form_number} - {min_year}"
                    download_pdf(pdf, filename, form_number)

                elif self.cmd == "form name info":
                    response = Form(
                        form_number=form_number,
                        form_title=form_title,
                        min_year=min_year,
                    ).to_dict()
                    print(response)
                    responses.append(response)

        return responses if self.cmd == "form name info" else [None]