import pytest
from pages.sandbox_page import SandboxPage

def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_boton_id_dinamico()

    elemento_texto_oculto = sandbox_page.wait_for_element(
        sandbox_page.HIDDEN_TEXT_LABEL
    )

    texto_esperado = (
        "OMG, aparezco mnmnmnmdespués de 3 segundos de haber hecho click en el botón"
    )

    assert (
        texto_esperado in elemento_texto_oculto.text
    ), "el texto esperado no coincide"