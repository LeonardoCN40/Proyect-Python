import csv
import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CSV_PATH = os.path.join(os.path.dirname(__file__), "TestData", "busquedaGoogle.csv")

_DATOS_POR_DEFECTO = [
    ("selenium python", "Selenium"),
    ("automatización web", "automation"),
    ("testing framework", "testing"),
    ("page object model", "POM"),
]


def _leer_terminos_busqueda():
    try:
        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            terminos = [
                (row["termino_busqueda"], row["resultado_esperado"])
                for row in reader
                if "termino_busqueda" in row and "resultado_esperado" in row
            ]
            return terminos if terminos else _DATOS_POR_DEFECTO
    except FileNotFoundError:
        return _DATOS_POR_DEFECTO


@pytest.mark.parametrize("termino_busqueda,resultado_esperado", _leer_terminos_busqueda())
@pytest.mark.parametrized
def test_busqueda_google_parametrizada(browser, termino_busqueda, resultado_esperado):
    """Test parametrizado de búsqueda en Google con datos CSV."""
    browser.get("https://www.google.com")

    try:
        accept_cookies = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Aceptar') or contains(text(), 'Accept') or contains(text(), 'I agree')]")
            )
        )
        accept_cookies.click()
    except Exception:
        pass  # Banner de cookies no apareció

    search_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(termino_busqueda)
    search_box.submit()

    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    page_source = browser.page_source.lower()
    assert resultado_esperado.lower() in page_source, (
        f"El término '{resultado_esperado}' no se encontró en los resultados "
        f"de búsqueda para '{termino_busqueda}'. "
        f"Página verificada: {browser.current_url}"
    )
