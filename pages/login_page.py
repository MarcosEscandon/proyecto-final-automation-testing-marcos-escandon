from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object para la página de Login de SauceDemo."""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        """Realiza el login con usuario y contraseña."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Obtiene el mensaje de error si el login falla."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_button_displayed(self):
        """Verifica si el botón de login está visible."""
        try:
            self.find_element(self.LOGIN_BUTTON)
            return True
        except:
            return False
