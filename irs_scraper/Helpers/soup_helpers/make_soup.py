import requests
from bs4 import BeautifulSoup


def make_soup(product_number_query_arg: str, page: int = 0):
    queriable_product_number = product_number_query_arg.replace(" ", "+")
    search_endpoint = f"/app/picklist/list/priorFormPublication.html?sortColumn=sortOrder&indexOfFirstRow={page}&value={queriable_product_number}&criteria=formNumber&resultsPerPage=200&isDescending=false"
    base_url = f"https://apps.irs.gov{search_endpoint}"
    try:
        page = requests.get(base_url)
    except requests.exceptions.HTTPError as err:
        return print(err)
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup
