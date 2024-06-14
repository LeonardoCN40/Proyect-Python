from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    DYNAMIC_TO_BUTTON = (By.XPATH,"//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]",
    )

    HIDDEN_TEXT_LABEL = (
            By.XPATH,"//p[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]"
    )

    def navigate_sandbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
    )        

    def click_enviar(self):
        try:
            WebDriverWait(self.driver, 10).until(       # Esperar a que el botón sea clickable
            EC.element_to_be_clickable(self.ENVIAR_BUTTON)
    ).click()
        except ElementClickInterceptedException:         # Manejar la excepción si se produce
            print("El botón 'Enviar' está cubierto o no es clickable en este momento.")     
      # self.click(self.ENVIAR_BUTTON)
                            
    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_TO_BUTTON)
  