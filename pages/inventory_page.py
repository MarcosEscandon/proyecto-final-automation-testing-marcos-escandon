from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object para la página de Inventario."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_title(self):
        """Obtiene el título de la página."""
        return self.get_text(self.PAGE_TITLE)

    def add_backpack_to_cart(self):
        """Añade la mochila al carrito."""
        self.click_element(self.ADD_TO_CART_BACKPACK)

    def get_cart_badge_count(self):
        """Obtiene el número de items en el carrito."""
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        """Navega al carrito de compras."""
        self.click_element(self.CART_LINK)

    def logout(self):
        """Cierra la sesión."""
        self.click_element(self.MENU_BUTTON)
        # Esperar a que el enlace de logout sea clicable
        logout_link = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        # Usar JS click para evitar problemas de intercepción
        self.driver.execute_script("arguments[0].click();", logout_link)
