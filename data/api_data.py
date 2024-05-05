import json

import requests


class ApiData:
    def response_mouse_search(self, h_width=9.0, h_length=15.0, grip_type='CLAW', leniency=2, wireless='false',
                              lefthanded='false', buttons=-1, shape='both'):
        """The function returns all data about mice in accordance with the entered parameters."""
        url = f"https://www.rocketjumpninja.com/api/search/mice?h_width={h_width}&h_length={h_length}&grip_type={grip_type}&leniency={leniency}&wireless={wireless}&lefthanded={lefthanded}&buttons={buttons}&shape={shape}"
        response = requests.get(url)
        search_data = json.loads(response.text)

        return search_data

    def hand_parameters(self, h_width: float, h_length: float, grip_type: str, leniency: int, wireless: str,
                        lefthanded: str, buttons: int, shape: str):
        """The function returns the minimum and maximum hand parameters in accordance with the entered parameters."""

        response = self.response_mouse_search(h_width, h_length, grip_type, leniency, wireless,
                                              lefthanded, buttons, shape)

        hand_parameters = response["search_parameters"]

        return hand_parameters

    def buttons_number(self, h_width=10, h_length=19, grip_type=-1, leniency=-1, buttons=6):
        """The function returns a sorted list of the number of buttons existing in this search."""

        table_d = self.response_mouse_search(h_width, h_length, grip_type, leniency, buttons)
        buttons = []
        for item in table_d["mice"]:
            button = item.get('buttons')
            if button:
                buttons.append(int(button))
        check = []
        for i in buttons:
            if i not in check:
                check.append(i)
        return sorted(check)
