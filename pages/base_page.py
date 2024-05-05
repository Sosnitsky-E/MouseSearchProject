from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        """ Open page link ."""
        self.driver.get(self.link)

    def go_to_element(self, element):
        """
        Make a scroll to selected element
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_present(self, locator, timeout=5):
        """
        Expects to check that the element is present in the DOM tree, but not necessarily,
         what is visible and displayed on the page.
         Returns WebElement.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator, timeout=5):
        """
        Waiting for verification that the element present in DOM
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_not_element_present(self, locator, timeout=5):
        try:
            self.element_is_present(locator)
        except TimeoutException:
            return True

        return False

    def elements_are_visible(self, locator, timeout=5):
        """
        Waits to verify that the elements are present in the DOM tree, visible, and rendered on the page.
         Visibility means that elements are not only displayed,
         but also has height and width greater than 0.
         Locator - used to find elements. Returns WebElements.
         Timeout - the time during which it will wait. The default is 5 seconds,
         can be changed if necessary.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def alert_is_present(self):
        """Waits for Alert to open on the page."""
        wait(self.driver, 10).until(EC.alert_is_present())

    def search_table_data(self, teble_rows_locator):
        """Returns mice Search table data."""

        rows = self.elements_are_visible(teble_rows_locator, 15)

        mouse_data_list = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            rank = cells[0].text
            name = cells[1].text
            weight = cells[2].text
            size = cells[3].text
            length_cm = cells[4].text
            grip_width_cm = cells[5].text
            review = cells[6].text

            # Creating a dictionary with data for the current row
            mouse_data = {
                "Name": name,
                "Weight (g)": weight,
                "Size": size,
                "Length (cm)": length_cm,
                "Rank": rank,
                "Grip Width (cm)": grip_width_cm,
                "Review": review
            }
            # Adding a dictionary to the list
            mouse_data_list.append(mouse_data)

        return mouse_data_list
