import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_service)

def test_prueba():
    driver.get("https://www.freerangetesters.com/")
    titulo = driver.title
    assert titulo == "Free Range Testers"

