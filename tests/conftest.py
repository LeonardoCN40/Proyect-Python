import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.sandbox_page import SandboxPage


@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    if os.getenv("CI"):
        chrome_options.add_argument("--headless=new")

    driver = _create_driver(chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def _create_driver(chrome_options):
    try:
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)
    except Exception as wdm_error:
        pass

    try:
        return webdriver.Chrome(options=chrome_options)
    except Exception:
        pass

    # Último recurso: limpiar cache de webdriver-manager y reintentar
    cache_path = os.path.expanduser("~/.wdm")
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)

    try:
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)
    except Exception as final_error:
        raise RuntimeError(f"No se pudo inicializar ChromeDriver: {final_error}") from final_error


@pytest.fixture(scope="function")
def sandbox_page(browser):
    return SandboxPage(browser)
