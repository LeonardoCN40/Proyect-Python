import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_navegacion_basica_freerange(browser):
    """Verifica la navegación básica al sitio Free Range Testers"""
    browser.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
    
    # Esperar a que el título contenga texto específico
    WebDriverWait(browser, 10).until(
        EC.title_contains("Automation")
    )
    
    assert "Automation" in browser.title, f"Título esperado no encontrado. Título actual: {browser.title}"


@pytest.mark.smoke  
def test_verificar_elementos_principales(browser):
    """Verifica que los elementos principales estén presentes en la página"""
    browser.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
    
    # Verificar que el botón de ID dinámico esté presente
    boton_dinamico = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Hacé click para generar un ID dinámico')]"))
    )
    
    assert boton_dinamico.is_displayed(), "Botón de ID dinámico no está visible"


@pytest.mark.smoke
def test_titulo_pagina_correcto(browser):
    """Verifica que el título de la página sea el esperado"""
    browser.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
    
    titulo_esperado = "Automation Sandbox"
    titulo_actual = browser.title
    
    assert titulo_esperado == titulo_actual, (
        f"El título esperado '{titulo_esperado}' no coincide. "
        f"Título actual: '{titulo_actual}'"
    )