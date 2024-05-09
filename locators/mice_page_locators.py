from selenium.webdriver.common.by import By


class MiceLocators:
    ALL_MICE_TBL = By.CSS_SELECTOR, " table.top.sortable tbody tr"
    ELEMENT = By.TAG_NAME, "td"

class MouseSearchLocators:
    HAND_LANGTH_FIELD = By.CSS_SELECTOR, "input[name='h_length']"
    HAND_WIDTH_FIELD = By.CSS_SELECTOR, "input[name='h_width']"
    SEARCH_BUTTON = By.CSS_SELECTOR, "#searchButton"
    TABLE_CELLS = By.TAG_NAME, "td"
    TABLE_ROWS = By.CSS_SELECTOR, "#resultsTable tr"

    def ler(self, value=2):
        return By.CSS_SELECTOR, f"input[name='leniency'][value='{value}']"

    LENIENCY_RADIO = By.CSS_SELECTOR,"input[name = 'leniency'][value = '3']"

    SELECT_MEASUREMENT = By.ID, "measurement"
    SORT_BY_NAME = By.ID,"nameHeader"