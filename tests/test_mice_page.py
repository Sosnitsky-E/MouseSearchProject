import time
from data.data_for_tests import ValuesForVerification, ExpectedResults

import pytest


class TestMicePage:
    @pytest.mark.positive
    @pytest.mark.parametrize('length, width',
                             list(zip(ValuesForVerification.parameters_cm["length"],
                                      ValuesForVerification.parameters_cm["width"])))
    def test_search_mouse_by_width_and_length_cm(self, mouse_search_page_fixture, length, width):
        mouse_search_page_fixture.open_page()
        mouse_search_page_fixture.fill_length(length)
        mouse_search_page_fixture.fill_width(width)
        mouse_search_page_fixture.click_search()
        assert mouse_search_page_fixture.check_results_are_within_range_search_hand_parameters(h_width=width,
                                                                                               h_length=length), \
            "Some of the mice found are not within the search range."

    @pytest.mark.positive
    @pytest.mark.parametrize('length, width',
                             list(zip(ValuesForVerification.parameters_inches["length"],
                                      ValuesForVerification.parameters_inches["width"])))
    def test_search_mouse_by_width_and_length_inches(self, mouse_search_page_fixture, length, width):
        mouse_search_page_fixture.open_page()
        mouse_search_page_fixture.select_measurement()
        mouse_search_page_fixture.fill_length(length)
        mouse_search_page_fixture.fill_width(width)
        mouse_search_page_fixture.click_search()
        assert mouse_search_page_fixture.check_results_are_within_range_search_hand_parameters(h_width=width,
                                                                                               h_length=length),\
            "Some of the mice found are not within the search range."

    @pytest.mark.negative
    def test_search_mouse_empty_fields(self, mouse_search_page_fixture):
        mouse_search_page_fixture.open_page()
        mouse_search_page_fixture.click_search()
        assert (mouse_search_page_fixture.check_field_filling_notification() ==
                ExpectedResults.expected_warning_about_empty_fields), \
            "The text of the warning message does not match the expected text."

    @pytest.mark.negative
    def test_search_mouse_by_min_hand_parameters_low_leniency(self, mouse_search_page_fixture,
                                                              length=ValuesForVerification.parameters_inches["length"][
                                                                  0],
                                                              width=ValuesForVerification.parameters_inches["width"][0],
                                                              leniency=ValuesForVerification.leniency_values[0]):
        mouse_search_page_fixture.open_page()
        mouse_search_page_fixture.select_measurement()
        mouse_search_page_fixture.fill_length(length)
        mouse_search_page_fixture.fill_width(width)
        mouse_search_page_fixture.select_leniency(leniency)
        mouse_search_page_fixture.click_search()
        assert (mouse_search_page_fixture.check_field_filling_notification() ==
                ExpectedResults.expected_no_mice_warning_text), \
            "The text of the warning message does not match the expected text"

    @pytest.mark.positive
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_t(self, mouse_search_page_fixture, width=ValuesForVerification.parameters_inches["width"][1],
               length=ValuesForVerification.parameters_inches["length"][1]):
        mouse_search_page_fixture.open_page()
        mouse_search_page_fixture.fill_length(length)
        mouse_search_page_fixture.fill_width(width)
        mouse_search_page_fixture.click_search()

        assert mouse_search_page_fixture.check_search_results(h_length=length,
                                                              h_width=width), \
            ("The number of mice found according to the entered criteria does not match the number of mice from the "
             "database")
