# Proyecto Final de Automation Testing - Marcos Escandon

Este proyecto es un framework de automatización de pruebas desarrollado en Python, que combina pruebas de UI con Selenium WebDriver y pruebas de API con la librería Requests.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Pytest**: Framework de ejecución de pruebas.
- **Selenium WebDriver**: Para la automatización de la interfaz de usuario (UI).
- **Requests**: Para la automatización de pruebas de API.
- **Page Object Model (POM)**: Patrón de diseño para estructurar las pruebas de UI.
- **Pytest-HTML**: Para la generación de reportes visuales.

## Estructura del Proyecto

```
proyecto-final-automation-testing/
├── data/               # Archivos de datos de prueba (JSON, CSV)
├── pages/              # Clases del Page Object Model
├── tests/              # Scripts de prueba (UI y API)
├── utils/              # Utilidades y configuración (Logging, Driver)
├── reports/            # Reportes generados (HTML)
├── logs/               # Archivos de log
├── conftest.py         # Configuración global de Pytest y Hooks
├── pytest.ini          # Configuración de Pytest
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyecto
```

## Instalación

1.  Clona este repositorio.
2.  Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de Pruebas

Para ejecutar todas las pruebas y generar el reporte:

```bash
pytest
```

Para ejecutar solo pruebas de UI:

```bash
pytest -m ui
```

Para ejecutar solo pruebas de API:

```bash
pytest -m api
```

## Reportes

Al finalizar la ejecución, se generará un archivo `reports/report.html`. Este reporte contiene:
- Resumen de pruebas ejecutadas.
- Estado de cada prueba (Pasó/Falló).
- Capturas de pantalla para las pruebas de UI que fallen.
