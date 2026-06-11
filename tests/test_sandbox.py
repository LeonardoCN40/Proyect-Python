"""
Tests de la página Sandbox de Free Range Testers.

Sitio bajo prueba: https://thefreerangetester.github.io/sandbox-automation-testing/

Fixture requerido: sandbox_page (scope=function) — definido en conftest.py.
Ejecutar con: pytest -m sandbox
"""

import pytest


@pytest.mark.sandbox
def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    """
    Verifica que el texto oculto aparezca tras hacer click en el botón de ID dinámico.

    Flujo:
        1. Navegar al sandbox.
        2. Hacer click en el botón de ID dinámico.
        3. Esperar a que el párrafo oculto se vuelva visible (aparece ~3 segundos después).
        4. Confirmar que el texto del párrafo coincide con el esperado.
    """
    sandbox_page.navigate_sandbox()
    sandbox_page.click_boton_id_dinamico()

    elemento_texto_oculto = sandbox_page.wait_for_element(
        sandbox_page.HIDDEN_TEXT_LABEL
    )

    texto_esperado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"

    assert texto_esperado in elemento_texto_oculto.text, (
        f"El texto esperado '{texto_esperado}' no se encontró. "
        f"Texto actual: '{elemento_texto_oculto.text}'"
    )


@pytest.mark.sandbox
def test_boton_id_dinamico_cambiar_color_al_hacer_hover(sandbox_page):
    """
    Verifica que el botón de ID dinámico reaccione visualmente al hover.

    El test acepta cualquiera de estas dos señales como evidencia de hover activo:
      - Cambio en background-color respecto al estado inicial.
      - Cursor cambia a 'pointer' (indica elemento interactivo).

    Flujo:
        1. Navegar al sandbox.
        2. Localizar el botón y capturar su color de fondo inicial.
        3. Mover el cursor sobre el botón (ActionChains).
        4. Leer color de fondo y tipo de cursor después del hover.
        5. Confirmar que al menos una propiedad cambió.
    """
    sandbox_page.navigate_sandbox()

    boton = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)

    color_inicial = boton.value_of_css_property("background-color")

    sandbox_page.hover_over_dynamic_id_button()

    color_hover = boton.value_of_css_property("background-color")
    cursor_hover = boton.value_of_css_property("cursor")

    color_cambio = color_inicial != color_hover
    cursor_es_pointer = cursor_hover == "pointer"

    assert color_cambio or cursor_es_pointer, (
        f"El hover no produjo cambios visuales en el botón. "
        f"Color antes: '{color_inicial}', Color hover: '{color_hover}', "
        f"Cursor hover: '{cursor_hover}'"
    )
