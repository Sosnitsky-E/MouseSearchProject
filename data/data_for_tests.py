import json


class ValuesForVerification:
    # Values and data passed to tests for verification.

    parameters_cm = {"length": [24.6, 11.7, 18.5], "width": [11.0, 8.9, 9.95]}
    parameters_inches = {"length": [9.68, 4.60629, 7.28346], "width": [4.33, 3.50394, 3.91732]}
    leniency_values = [0, 1, 2, 3, 4]
    measurement = ["cm", "inches"]


class ExpectedResults:
    # Expected results transferred to tests for verification.

    expected_warning_about_empty_fields = "Please enter values for length and width"
    expected_no_mice_warning_text =  "Unfortunately there are no mice in the database that fit your measurements!\nMore mice are being made so try again later. For now you can increase the Leniency setting to expand your search range"


    def get_mauses_by_hand_parameters(self, max_length, min_length, max_width, min_width):
        """
        The function returns data taken from an improvised database based on a table in accordance with the entered hand parameters.
        """


        with open("data.json", "r") as f:
            mice_data = json.load(f)

        search_list = []

        for mice in mice_data:
            if min_length <= float(mice["Length (cm)"]) and float(
                    mice["Length (cm)"]) <= max_length and min_width <= float(mice["Grip Width (cm)"]) and float(
                mice["Grip Width (cm)"]) <= max_width:
                search_list.append(mice)

        return search_list
