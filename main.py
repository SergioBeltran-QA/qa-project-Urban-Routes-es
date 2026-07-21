import data
from selenium import webdriver

from pages import UrbanRoutesPage


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
