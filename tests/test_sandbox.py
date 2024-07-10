import pytest


@pytest.mark.sandbox
def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_boton_id_dinamico()

    elemento_texto_oculto = sandbox_page.wait_for_element(
        sandbox_page.HIDDEN_TEXT_LABEL
    )

    texto_esperado = (
       "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    )

    assert (
        texto_esperado in elemento_texto_oculto.text
    ), "el texto esperado no coincide"


def test_boton_id_dinamico_cambiar_color_al_hacer_hover(sandbox_page):
    sandbox_page.navigate_sandbox()
    boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)
    color_before_hover = boton_id_dinamico.value_of_css_property("background-color")
    sandbox_page.hover_over_dynamic_id_button()
    color_after_hover = boton_id_dinamico.value_of_css_property("background-color")
    assert color_before_hover != color_after_hover
    

