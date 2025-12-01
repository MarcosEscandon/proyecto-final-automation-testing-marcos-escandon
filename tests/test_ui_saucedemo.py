import pytest
import json
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import get_logger

logger = get_logger()

def load_user_data():
    """Carga datos de usuarios desde el archivo JSON."""
    data_path = os.path.join("data", "users.json")
    with open(data_path, "r") as f:
        return json.load(f)

class TestSauceDemoUI:
    
    @pytest.mark.ui
    def test_login_success(self, driver):
        """Test de login exitoso con usuario estándar."""
        logger.info("Iniciando test_login_success")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        login_page.open_url("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        assert inventory_page.get_title() == "Products"
        logger.info("Login exitoso verificado")

    @pytest.mark.ui
    @pytest.mark.parametrize("user_data", [u for u in load_user_data() if u["type"] == "locked"])
    def test_login_locked_user(self, driver, user_data):
        """Test de login fallido con usuario bloqueado (Data Driven)."""
        logger.info(f"Iniciando test_login_locked_user con {user_data['username']}")
        login_page = LoginPage(driver)
        
        login_page.open_url("https://www.saucedemo.com/")
        login_page.login(user_data["username"], user_data["password"])
        
        error_msg = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_msg
        logger.info("Mensaje de error verificado para usuario bloqueado")

    @pytest.mark.ui
    def test_add_to_cart(self, driver):
        """Test para agregar un producto al carrito."""
        logger.info("Iniciando test_add_to_cart")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        login_page.open_url("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"
        logger.info("Producto agregado al carrito correctamente")

    @pytest.mark.ui
    def test_checkout_flow(self, driver):
        """Test de flujo completo de compra."""
        logger.info("Iniciando test_checkout_flow")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        # Login
        login_page.open_url("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        # Add to cart
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        
        # Checkout
        cart_page.proceed_to_checkout()
        cart_page.fill_checkout_info("Juan", "Perez", "12345")
        cart_page.finish_checkout()
        
        assert cart_page.get_complete_message() == "Thank you for your order!"
        logger.info("Flujo de checkout completado exitosamente")

    @pytest.mark.ui
    def test_logout(self, driver):
        """Test de cierre de sesión."""
        logger.info("Iniciando test_logout")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        login_page.open_url("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page.logout()
        
        # Verificar que volvimos al login
        assert login_page.is_login_button_displayed()
        logger.info("Logout exitoso verificado")
