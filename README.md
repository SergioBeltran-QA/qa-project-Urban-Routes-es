# Proyecto Urban Routes — Pruebas automatizadas

## Descripción

Este proyecto automatiza el flujo completo para solicitar un taxi en la aplicación web Urban Routes.

Las pruebas comprueban la configuración de una ruta, la selección de la tarifa Comfort, el registro del teléfono, la incorporación de un método de pago y la configuración de requisitos adicionales para el viaje.

El proyecto fue desarrollado como parte del Sprint 9 del programa de QA Engineer de TripleTen.

## Escenarios automatizados

El proyecto contiene nueve pruebas automatizadas:

1. Configurar las direcciones de origen y destino.
2. Seleccionar la tarifa Comfort.
3. Registrar un número de teléfono y confirmar el código SMS.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Solicitar una manta y pañuelos.
7. Pedir dos helados.
8. Comprobar que aparece el modal de búsqueda de taxi.
9. Esperar a que aparezca la información del conductor.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- pytest
- Google Chrome
- ChromeDriver
- Git y GitHub
- PyCharm

## Técnicas utilizadas

- Page Object Model (POM) para separar los localizadores, las acciones de la página y las pruebas.
- Localizadores CSS, XPath, ID y nombre de clase.
- Esperas explícitas con `WebDriverWait` y `expected_conditions`.
- Interacción con campos, botones, interruptores y contadores.
- Uso de `Keys.TAB` para cambiar el enfoque del campo CVV.
- Recuperación del código SMS mediante los registros de rendimiento del navegador.
- Validaciones con sentencias `assert`.
- Automatización de un flujo end-to-end.

## Estructura del proyecto

- `data.py`: contiene la URL del servidor y los datos de prueba.
- `main.py`: contiene la clase `UrbanRoutesPage`, los localizadores, los métodos y las pruebas automatizadas.
- `README.md`: contiene la documentación del proyecto.

## Requisitos

Antes de ejecutar las pruebas, es necesario tener instalado:

- Python 3
- Google Chrome
- Una versión de ChromeDriver compatible con Google Chrome
- Selenium 4.9.1
- pytest

ChromeDriver debe estar disponible en la variable de entorno `PATH`.

## Instalación

Clona el repositorio:

```bash
git clone git@github.com:SergioBeltran-QA/qa-project-Urban-Routes-es.git
```

Accede al directorio del proyecto:

```bash
cd qa-project-Urban-Routes-es
```

Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instala las dependencias:

```bash
python -m pip install selenium==4.9.1 pytest
```

## Configuración del servidor

Inicia el servidor de Urban Routes desde la plataforma de TripleTen.

Copia la URL completa, incluyendo `?lng=es`, y reemplaza el valor de `urban_routes_url` en `data.py`.

Ejemplo:

```python
urban_routes_url = 'URL_DEL_SERVIDOR?lng=es'
```

La URL del servidor es temporal y debe actualizarse cuando expire.

## Ejecución de las pruebas

Ejecuta todas las pruebas con:

```bash
python -m pytest main.py -v
```

El resultado esperado es:

```text
9 passed
```