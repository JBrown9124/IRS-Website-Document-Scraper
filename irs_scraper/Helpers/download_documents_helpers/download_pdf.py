import urllib
import os


def download_pdf(download_url: str, filename: str, directory_name: str) -> None:

    response = urllib.request.urlopen(download_url)
    path = os.getcwd()
    pdf_path = f"{path}\\IRSDocuments\\{directory_name}"
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)

    file_path = f"{pdf_path}\\{filename}.pdf"
    if not os.path.exists(file_path):
        print(f"Downloading {filename}...")
        with open(f"{pdf_path}\\{filename}.pdf", "wb") as file:
            file.write(response.read())

        print(f"{filename} downloaded.")
    else:
        print(f"{filename} already exists.")
