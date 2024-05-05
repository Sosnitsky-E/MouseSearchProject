import time

from selenium.webdriver.support.select import Select

from data.api_data import ApiData
from data.data_for_tests import ExpectedResults, ValuesForVerification
from locators.mice_page_locators import MouseSearchLocators
from pages.base_page import BasePage


class MiceSearchPage(BasePage):
    def fill_length(self, length_val: int):
        """Filling the length field."""
        self.element_is_present(MouseSearchLocators.HAND_LANGTH_FIELD).send_keys(length_val)

    def fill_width(self, width_val: int):
        """Filling the width field."""
        self.element_is_present(MouseSearchLocators.HAND_WIDTH_FIELD).send_keys(width_val)

    def click_search(self):
        """Clicking the search button."""
        self.element_is_present(MouseSearchLocators.SEARCH_BUTTON).click()
        time.sleep(1)

    def select_leniency(self, value):
        """Click the radio button 'leniency'."""
        radio_button = self.element_is_present(MouseSearchLocators.ler(self, value))
        radio_button.click()

    def table_result(self):
        """Get search table data."""
        table_data = self.search_table_data(MouseSearchLocators.TABLE_ROWS)
        return table_data

    def get_expected_hand_parameters(self, h_width=9.0, h_length=15.0, grip_type='CLAW', leniency=2, wireless='false',
                                     lefthanded='false', buttons=-1, shape='both'):
        """Get the range of search hand values."""
        h_params = ApiData()
        params = h_params.hand_parameters(h_width, h_length, grip_type, leniency, wireless,
                                          lefthanded, buttons, shape)

        return params

    def check_results_are_within_range_search_hand_parameters(self, h_width=9.0, h_length=15.0, grip_type='CLAW',
                                                              leniency=2, wireless='false',
                                                              lefthanded='false', buttons=-1, shape='both'):
        """Checks that the data in the table is within the required hand values."""

        table_d = self.table_result()

        lengths = []
        widths = []

        for item in table_d:
            length = item.get('Length (cm)')
            width = item.get('Grip Width (cm)')
            lengths.append(float(length))
            widths.append(float(width))

        hand_parameters_from_responce = self.get_expected_hand_parameters(h_width, h_length, grip_type, leniency,
                                                                          wireless,
                                                                          lefthanded, buttons, shape)

        result_l = True
        result_w = True

        if max(lengths) > float(hand_parameters_from_responce["max_length"]) and min(lengths) < float(
                hand_parameters_from_responce["min_length"]):
            result_l = False

        if max(widths) > float(hand_parameters_from_responce["max_width"]) and min(widths) < float(
                hand_parameters_from_responce["min_width"]):
            result_w = False

        if result_w and result_l:
            return True
        else:
            return False

    def select_measurement(self):
        """Select units of measurement."""
        show_entries = self.element_is_present(MouseSearchLocators.SELECT_MEASUREMENT)
        dropdown = Select(show_entries)
        dropdown.select_by_value(ValuesForVerification.measurement[1])

    def check_field_filling_notification(self):
        """Returns the notification text if the fields are not filled in"""
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        actua_alert_text = alert.text
        return actua_alert_text

    def check_search_results(self, h_width=9.0, h_length=15.0, grip_type='CLAW', leniency=2, wireless='false',
                             lefthanded='false', buttons=-1, shape='both'):
        """Checks that the mice search table results match the database search results."""

        h_params = self.get_expected_hand_parameters(h_width, h_length, grip_type, leniency, wireless,
                                                     lefthanded, buttons, shape)

        expect_res = ExpectedResults()
        expected_mice_list = expect_res.get_mauses_by_hand_parameters(h_params.get("max_length"),
                                                                      h_params["min_length"], h_params["max_width"],
                                                                      h_params["min_width"])

        actual_table_results = self.table_result()

        return len(actual_table_results) == len(expected_mice_list)
