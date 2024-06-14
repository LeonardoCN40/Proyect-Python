import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def read_search_terms():
    with open('TestData/busquedaGoogle.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return [row[0] for row in data[1:]]

@pytest.fixture(params=read_search_terms())
def termino_de_busqueda(request):
    return request.param 

def test_google_busqueda(browser, termino_de_busqueda):
    search_box = browser.find_element("name","q")
    search_box.send_keys(termino_de_busqueda + Keys.RETURN)

    results = browser.find_element("id","search")
    assert (
       len(results.find_elements("xpath",".//div")) > 0 
    ), "hay resultado de busqueda"