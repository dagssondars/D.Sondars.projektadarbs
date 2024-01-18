import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AlcoholScraper:
    def __init__(self, url):
        self.url = url
        self.service = Service()
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.option)
    def fetch_data(self, drink_choice):
        pass
    def parse_data(self, data):
        pass
class SpiritsnWine(AlcoholScraper):
    def fetch_data(self, drink_choice):
        self.driver.get(self.url)
        time.sleep(2)
        find = self.driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonAccept")
        find.click()
        find = self.driver.find_element(By.CLASS_NAME, "btn-close")
        find.click()
        find = self.driver.find_element(By.CLASS_NAME, "form-control")
        find.send_keys(drink_choice)
        find.send_keys(Keys.ENTER)
        time.sleep(2)
        find = self.driver.find_element(By.CLASS_NAME, "btn-close")
        find.click()

        elements1 = self.driver.find_elements(By.CLASS_NAME, "product-title")
        elements2 = self.driver.find_elements(By.CLASS_NAME, "product-details")
        elements3 = self.driver.find_elements(By.CLASS_NAME, "product-price-sale")

        data = []
        for title, details, price in zip(elements1, elements2, elements3):
            title_text = title.text
            details_text = details.text.split(',')[-1].strip()
            sale_price = price.text.split('\n')[0].strip()

            data.append({
                'Nosaukums': title_text,
                'Details': details_text,
                'Cena': sale_price
            })
        return data
    
    def parse_data(self, data):
        for item in data:
            print("Veikals: Spirits and Wine")
            print(f"Nosaukums: {item['Nosaukums']}")
            print(f"Tilpums: {item['Details']}")
            print(f"Cena: {item['Cena']}")
            print("-" * 50)

class LatvijasBalzams(AlcoholScraper):
    def fetch_data(self, drink_choice):
        self.driver.get(self.url)
        time.sleep(2)
        find = self.driver.find_element(By.ID, "ac_yes")
        find.click()
        find = self.driver.find_element(By.ID, "search")
        find.send_keys(drink_choice)
        find.send_keys(Keys.ENTER)

        elements1 = self.driver.find_elements(By.CLASS_NAME, "product-item-link")
        elements2 = self.driver.find_elements(By.CLASS_NAME, "product-additional-attributes")
        elements3 = self.driver.find_elements(By.CSS_SELECTOR, ".special-price")

        data = []
        for title, details, price in zip(elements1, elements2, elements3):
            title_text = title.text
            details_text = details.text
            special_price_text = price.text
            special_price = special_price_text.split(',')[1].strip()

            data.append({
                'Nosaukums': title_text,
                'Details': details_text,
                'Cena': special_price
            })
        return data
    
    def parse_data(self, data):
        for item in data:
            print("Veikals: Latvijas Balzams")
            print(f"Nosaukums: {item['Nosaukums']}")
            print(f"Procenti,Tilpums: {item['Details']}")
            print(f"Cena: {item['Cena']}")
            print("-" * 50)

store1_scraper = SpiritsnWine("https://www.spiritsandwine.lv/en/")
store2_scraper = LatvijasBalzams("https://www.lbveikali.lv/")
drink_choice = input("Ievadiet dzēriena nosaukumu:")

store1_data = store1_scraper.fetch_data(drink_choice)
store1_scraper.parse_data(store1_data)
store2_data = store2_scraper.fetch_data(drink_choice)
store2_scraper.parse_data(store2_data)
