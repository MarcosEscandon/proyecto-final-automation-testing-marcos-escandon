import pytest
import os
from selenium import webdriver
from datetime import datetime

@pytest.fixture(scope="function")
def driver(request):
    """Inicializa el WebDriver para cada test."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Descomentar para ejecución sin interfaz gráfica
    options.add_argument("--window-size=1920,1080")
    
    # Selenium 4.x maneja el driver automáticamente
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura screenshot si el test falla y lo adjunta al reporte HTML."""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Generar nombre de archivo único
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            # Limpiar caracteres inválidos
            file_name = file_name.replace("/", "_").replace("\\", "_").replace("::", "_")
            
            # Asegurar directorio de screenshots
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            
            screenshot_path = os.path.join(screenshots_dir, file_name)
            
            # Obtener driver del fixture
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                driver.save_screenshot(screenshot_path)
                
                # Adjuntar al reporte HTML (ruta relativa)
                relative_path = os.path.join("screenshots", file_name)
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:200px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        
        report.extra = extra
