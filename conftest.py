import shutil
import pytest

import ZIP_files
import download_file
import os
from find_dir import TMP_DIR, RES_DIR
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene.support.shared import browser

@pytest.fixture(scope='class', autouse=True)
def download_files():

    browser.config.base_url = "https://github.com/rollnicker/main/blob/master"
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)
    download_file.download_csv()
    download_file.download_pdf()
    download_file.download_xlsx()

    yield
    shutil.rmtree(TMP_DIR)

@pytest.fixture(scope='class', autouse=True)
def zip_files():
    if not os.path.exists(RES_DIR):
        os.mkdir(RES_DIR)
        ZIP_files.make_zip()

        yield
        shutil.rmtree(RES_DIR)