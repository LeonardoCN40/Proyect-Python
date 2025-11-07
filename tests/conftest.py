import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.sandbox_page import SandboxPage
import os


@pytest.fixture(scope="session")
def browser():
    """Fixture de browser con manejo robusto de ChromeDriver compatibility issues"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = None
    
    try:
        # Intentar con webdriver-manager primero
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
    except Exception as wdm_error:
        print(f"Error con webdriver-manager: {wdm_error}")
        
        # Fallback: intentar con ChromeDriver en PATH del sistema
        try:
            driver = webdriver.Chrome(options=chrome_options)
            print("Usando ChromeDriver del PATH del sistema")
            
        except Exception as system_error:
            print(f"Error con ChromeDriver del sistema: {system_error}")
            
            # Último recurso: usar una versión específica compatible
            try:
                # Limpiar cache de webdriver-manager
                cache_path = os.path.expanduser("~/.wdm")
                if os.path.exists(cache_path):
                    import shutil
                    shutil.rmtree(cache_path)
                    print("Cache de webdriver-manager limpiado")
                
                # Instalar versión específica compatible
                service = Service(ChromeDriverManager(version="114.0.5735.90").install())
                driver = webdriver.Chrome(service=service, options=chrome_options)
                print("Usando ChromeDriver versión 114.0.5735.90")
                
            except Exception as final_error:
                raise Exception(f"No se pudo inicializar ChromeDriver. Errores: WDM: {wdm_error}, Sistema: {system_error}, Final: {final_error}")
    
    if driver:
        driver.maximize_window()
        yield driver
        driver.quit()
    else:
        raise Exception("No se pudo crear instancia de ChromeDriver")


@pytest.fixture(scope="function")
def sandbox_page(browser):
    """Fixture de página con scope de función siguiendo patrones POM del proyecto"""
    return SandboxPage(browser)