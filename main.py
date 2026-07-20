import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_tariff = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']/..")
    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_input = (By.ID, 'phone')
    phone_next_button = (By.XPATH, "//button[text()='Siguiente']")
    phone_code_input = (By.ID, 'code')
    phone_confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']/..")
    card_number_input = (By.ID, 'number')
    card_code_input = (By.CSS_SELECTOR, '#code.card-input')
    card_add_button = (By.XPATH, "//button[text()='Agregar']")
    saved_card = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
    payment_method_close_button = (By.CSS_SELECTOR, '.payment-picker.open .section.active .section-close')
    message_for_driver_input = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//span")
    blanket_and_tissues_checkbox = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//input")
    ice_cream_plus_button = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/following-sibling::div//div[contains(@class, 'counter-plus')]")
    ice_cream_counter = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/following-sibling::div//div[@class='counter-value']")
    search_taxi_button = (By.CLASS_NAME, 'smart-button')
    search_taxi_modal = (By.CLASS_NAME, 'order')
    driver_information = (By.CSS_SELECTOR, '.order-buttons img')


    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_route_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.from_field))

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.order_taxi_button)).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.comfort_tariff)).click()

    def get_comfort_tariff_class(self):
        return self.driver.find_element(*self.comfort_tariff).get_attribute('class')

    def click_phone_number_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)
        ).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_input)
        ).send_keys(phone_number)

    def click_phone_next_button(self):
        self.driver.find_element(*self.phone_next_button).click()

    def set_phone_code(self, phone_code):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_code_input)
        ).send_keys(phone_code)

    def click_phone_confirm_button(self):
        self.driver.find_element(*self.phone_confirm_button).click()

    def set_phone(self, phone_number):
        self.click_phone_number_button()
        self.set_phone_number(phone_number)
        self.click_phone_next_button()
        phone_code = retrieve_phone_code(self.driver)
        self.set_phone_code(phone_code)
        self.click_phone_confirm_button()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                self.phone_number_button, phone_number ))

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).text

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)
        ).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        ).click()

    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.card_number_input)
        ).send_keys(card_number)

    def set_card_code(self, card_code):
        code_input = self.driver.find_element(*self.card_code_input)
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

    def click_card_add_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.card_add_button)
        ).click()

    def get_saved_card(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.saved_card)
        ).text

    def close_payment_method(self):
        self.driver.find_element(*self.payment_method_close_button).click()

    def add_card(self, card_number, card_code):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_card_add_button()

    def set_message_for_driver(self, message):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.message_for_driver_input)
        ).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_input).get_property('value')

    def click_blanket_and_tissues_switch(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_tissues_switch)).click()

    def get_blanket_and_tissues_checkbox(self):
        return self.driver.find_element(*self.blanket_and_tissues_checkbox).is_selected()

    def click_ice_cream_plus_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.ice_cream_plus_button)).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def click_search_taxi_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.search_taxi_button)).click()

    def get_search_taxi_modal(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.search_taxi_modal)).is_displayed()

    def get_driver_information(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(self.driver_information)).is_displayed()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_route_page()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_button()
        routes_page.select_comfort_tariff()
        assert 'active' in routes_page.get_comfort_tariff_class()

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone_number() == phone_number

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_card(card_number, card_code)
        assert routes_page.get_saved_card() == 'Tarjeta'
        routes_page.close_payment_method()

    def test_set_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.set_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message

    def test_order_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_tissues_switch()
        assert routes_page.get_blanket_and_tissues_checkbox()

    def test_order_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ice_cream_plus_button()
        routes_page.click_ice_cream_plus_button()
        assert routes_page.get_ice_cream_count() == '2'

    def test_search_taxi_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_search_taxi_button()
        assert routes_page.get_search_taxi_modal()

    def test_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_driver_information()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
