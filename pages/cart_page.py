from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object para la página del Carrito y Checkout."""

    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def proceed_to_checkout(self):
        """Inicia el proceso de checkout."""
        self.click_element(self.CHECKOUT_BUTTON)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Completa la información de envío."""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click_element(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        """Finaliza la compra."""
        self.click_element(self.FINISH_BUTTON)

    def get_complete_message(self):
        """Obtiene el mensaje de confirmación de orden."""
        return self.get_text(self.COMPLETE_HEADER)
