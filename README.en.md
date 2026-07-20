[Versión en español](README.md)

# Urban Routes — Automated Testing Project

## Description

This project automates the complete process of requesting a taxi through the Urban Routes web application.

The automated tests validate route configuration, Comfort fare selection, phone verification, payment method setup, and additional ride requirements.

The project was developed as part of Sprint 9 of the TripleTen QA Engineer program.

## Automated Test Scenarios

The project contains nine automated tests:

1. Set the origin and destination addresses.
2. Select the Comfort fare.
3. Enter a phone number and confirm the SMS code.
4. Add a credit card.
5. Enter a message for the driver.
6. Request a blanket and tissues.
7. Order two ice creams.
8. Verify that the taxi search modal appears.
9. Wait for the driver information to appear.

## Technologies

- Python
- Selenium WebDriver
- pytest
- Google Chrome
- ChromeDriver
- Git and GitHub
- PyCharm

## Techniques

- Page Object Model (POM) to separate page locators, interactions, and automated tests.
- CSS, XPath, ID, and class name locators.
- Explicit waits using `WebDriverWait` and `expected_conditions`.
- Interaction with input fields, buttons, switches, and counters.
- Use of `Keys.TAB` to move focus away from the CVV field.
- SMS confirmation code retrieval through browser performance logs.
- Assertions for validating expected results.
- End-to-end test automation.

## Project Structure

- `data.py`: contains the server URL and test data.
- `main.py`: contains the `UrbanRoutesPage` class, locators, methods, and automated tests.
- `README.md`: Spanish project documentation.
- `README.en.md`: English project documentation.

## Requirements

Before running the tests, install:

- Python 3
- Google Chrome
- A ChromeDriver version compatible with Google Chrome
- Selenium 4.9.1
- pytest

ChromeDriver must be available through the system `PATH`.

## Installation

Clone the repository:

```bash
git clone git@github.com:SergioBeltran-QA/qa-project-Urban-Routes-es.git
```

Open the project directory:

```bash
cd qa-project-Urban-Routes-es
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install selenium==4.9.1 pytest
```

## Server Configuration

Start the Urban Routes server through the TripleTen platform.

Copy the complete server URL, including `?lng=es`, and replace the value of `urban_routes_url` in `data.py`.

Example:

```python
urban_routes_url = 'SERVER_URL?lng=es'
```

The server URL is temporary and must be updated when it expires.

## Running the Tests

Run the complete automated test suite with:

```bash
python -m pytest main.py -v
```

Expected result:

```text
9 passed
```