from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class Transfers_Scraping:
    def __init__(self, from_location_enter, to_location_enter, date_enter, adults_enter):
        self.from_location_enter = from_location_enter
        self.to_location_enter = to_location_enter
        self.date_enter = date_enter
        self.adults_enter = adults_enter

    def scrape_trasfer(self):
        # Connection to Website
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.suntransfers.com/')
        time.sleep(5)

        # From location input
        from_location = driver.find_element(By.ID, 'outward_location')
        from_location.send_keys(self.from_location_enter)

        from_location_complete = driver.find_element(By.XPATH, '//*[@id="vanilla-search-form-container"]/div/div[1]/div[1]/div/div/div/div/a[1]')
        from_location_complete.click()

        # To location input
        to_location_label = driver.find_element(By.CLASS_NAME, 'c-switch__container') # search parent div
        to_location_label.click() # focus to parent div

        to_location = driver.find_element(By.XPATH, '//*[@id="return_location"]')
        to_location.send_keys(self.to_location_enter)
        time.sleep(5)

        to_location_complete = driver.find_element(By.XPATH, '//*[@id="vanilla-search-form-container"]/div/div[1]/div[2]/div[2]/div/div/div/div/a[1]')
        to_location_complete.click()

        # Date selection input
        date_selection_input = driver.find_element(By.XPATH, '//*[@id="vanilla-search-form-container"]/div/div[3]/div[1]')
        date_selection_input.click()

        year_selection = Select(driver.find_element(By.CLASS_NAME, 'pika-select-year'))
        year_selection.select_by_value(self.date_enter[0])

        date_selection = driver.find_element(By.ID, 'date_span_outward_date')
        driver.execute_script(f'arguments[0].innerHTML = "{self.date_enter[1]} {self.date_enter[2]} {self.date_enter[3]} {self.date_enter[4]}";', date_selection) # 2025 May 12 - 12:00

        # Passengers count input
        passengers_count = driver.find_element(By.ID, 'passengers-count')
        driver.execute_script(f'arguments[0].innerHTML = "{self.adults_enter} adults";', passengers_count)

        # Search button click
        search_btn = driver.find_element(By.ID, 'submit-form').click()
        time.sleep(5)

        # Show more button click
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="step_form"]/section/div[7]/a'))))
        time.sleep(5)

        # Get info
        cars = []
        max_passengers = []
        prices = []

        get_cars = driver.find_elements(By.CLASS_NAME, 'c-media__title')
        get_max_passengers = driver.find_elements(By.CLASS_NAME, 'c-feature__text')
        get_prices = driver.find_elements(By.CLASS_NAME, 'c-pricing__highlight')
        get_currency = driver.find_element(By.ID, 'currency-prominent')
        currency = get_currency.text

        len_list_info = len(get_cars)
        print(f'List length: {len_list_info}')
        print()

        for car in get_cars:
            cars.append(car.text)
        for passenger in get_max_passengers:
            if passenger.text[0] == 'U':
                max_passengers.append(passenger.text)
        for price in get_prices:
            prices.append(price.text)

        # Completion of scraping
        time.sleep(10)
        driver.close()

        return [cars, max_passengers, prices, currency]

       