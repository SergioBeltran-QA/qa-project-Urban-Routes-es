[English version](README.en.md)

# Urban Routes — Automatización de pruebas web

Proyecto de automatización end-to-end desarrollado durante el programa de QA Engineer de TripleTen.

## Descripción

Este proyecto automatiza el flujo completo para solicitar un taxi en la aplicación web Urban Routes. La suite valida desde la configuración de la ruta hasta la aparición de la información del conductor, utilizando una estructura basada en Page Object Model.

## Resultado

**9 pruebas automatizadas aprobadas**, incluido el escenario opcional de información del conductor.

## Escenarios automatizados

1. Configurar las direcciones de origen y destino.
2. Seleccionar la tarifa Comfort.
3. Registrar un número de teléfono y confirmar el código SMS.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Solicitar una manta y pañuelos.
7. Pedir dos helados.
8. Comprobar que aparece el modal de búsqueda de taxi.
9. Esperar a que aparezca la información del conductor.

## Competencias de QA demostradas

- Automatización de pruebas end-to-end
- Page Object Model
- Diseño de escenarios funcionales
- Localizadores CSS, XPath, ID y nombre de clase
- Esperas explícitas
- Validaciones con assertions
- Métodos reutilizables
- Interacción con formularios, modales, interruptores y contadores
- Recuperación del código SMS mediante registros de rendimiento
- Control de versiones con Git y GitHub

## Tecnologías

- Python
- Selenium WebDriver
- pytest
- Google Chrome
- ChromeDriver
- Git y GitHub
- PyCharm

## Estructura del proyecto

- `data.py` — URL del servidor y datos de prueba
- `pages.py` — clase `UrbanRoutesPage`, localizadores y métodos de interacción
- `helpers.py` — función `retrieve_phone_code()`
- `main.py` — clase `TestUrbanRoutes`, escenarios y validaciones
- `README.md` — documentación en español
- `README.en.md` — documentación en inglés

## Instalación

```bash
git clone https://github.com/SergioBeltran-QA/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
python -m venv .venv
source .venv/bin/activate
python -m pip install selenium==4.9.1 pytest
```

ChromeDriver debe ser compatible con la versión instalada de Google Chrome y estar disponible en la variable de entorno `PATH`.

## Configuración del servidor

Inicia el servidor de Urban Routes desde la plataforma de TripleTen. Copia la URL completa, incluido `?lng=es`, y sustituye el valor de `urban_routes_url` en `data.py`:

```python
urban_routes_url = "SERVER_URL?lng=es"
```

La URL de prueba es temporal y debe actualizarse cuando expire.

## Ejecución

```bash
python -m pytest main.py -v
```

Resultado esperado:

```text
9 passed
```

## Datos de prueba

Los nombres, teléfonos, direcciones y datos de pago incluidos en el repositorio son valores ficticios utilizados exclusivamente para pruebas.

## Autor

**Sergio Beltrán**  
Junior QA Engineer especializado en pruebas web, móviles, API y bases de datos.

- [GitHub](https://github.com/SergioBeltran-QA)
- [LinkedIn](https://www.linkedin.com/in/sergio-beltr%C3%A1n-/)
