
import json

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.edge.options import Options as EdgeOptions


from locators.mice_page_locators import MiceLocators




def save_data_to_file():
    options = EdgeOptions()
    options.add_argument('--headless')
    driver = webdriver.Edge(options=options)
    driver.get("https://www.rocketjumpninja.com/products/mice")
    # Find all rows in a table
    rows = wait(driver, 15).until(EC.visibility_of_all_elements_located(MiceLocators.ALL_MICE_TBL))
    mouse_data_list = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        name = cells[0].text
        weight = cells[1].text
        size = cells[2].text
        length_cm = cells[3].text
        length_inches = cells[4].text
        grip_width_cm = cells[5].text
        grip_width_inches = cells[6].text

        # Creating a dictionary with data for the current row
        mouse_data = {
            "Name": name,
            "Weight (g)": weight,
            "Size": size,
            "Length (cm)": length_cm,
            "Length (inches)": length_inches,
            "Grip Width (cm)": grip_width_cm,
            "Grip Width (inches)": grip_width_inches
        }
        # Adding a dictionary to the list
        mouse_data_list.append(mouse_data)

    # Path to the file where you want to save the JSON
    file_path = "data.json"

    # Saving a list of dictionaries to a JSON file
    with open(file_path, "w") as json_file:
        json.dump(mouse_data_list, json_file)

    driver.close()
    driver.quit()
