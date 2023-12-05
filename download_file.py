import os.path
import time

import requests
from selene import query
from selene.support.shared import browser
from find_dir import TMP_DIR

def download_pdf():
    browser.open("/TestPdf.pdf")
    browser.element("[data-testid='download-raw-button']").click()
    time.sleep(5)

def download_xlsx():
    browser.open("/import_ou_xlsx.xlsx")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(url=download_url).content
    with open(os.path.join(TMP_DIR, "XLSX_test.xlsx"), "wb") as file:
        file.write(content)

def download_csv():
    browser.open("/csv_for_test.csv")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(url=download_url).content
    with open(os.path.join(TMP_DIR, "CSV_test.CSV"), "wb") as file:
        file.write(content)

def open_file():
    with open("XLSX_test.xlsx") as download_file:
        file_content = download_file.read()
        print(file_content)
        assert "test_answer" in file_content


