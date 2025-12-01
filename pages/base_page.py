from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Clase base para todos los Page Objects."""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    def open_url(self, url):
        """Abre una URL en el navegador."""
        self.driver.get(url)

    def find_element(self, locator):
        """Encuentra un elemento web con espera explícita."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        """Espera a que un elemento sea clicable."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_element(self, locator):
        """Hace clic en un elemento."""
        element = self.wait_for_clickable(locator)
        element.click()

    def enter_text(self, locator, text):
        """Ingresa texto en un campo."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Obtiene el texto de un elemento."""
        element = self.find_element(locator)
        return element.text
