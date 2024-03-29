import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from pro.useful_functions import new_tab, switch_to


class AccountDetail:

    def __init__(self):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        self.driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        #self.path = 'driver/chromedriver.exe'
        #self.driver = webdriver.Chrome(executable_path=self.path)
        self._firstname = None
        self._lastname = None
        self._phone_num = None
        

    def _generate_names(self):
        print("Generating names......")
        baseURL = 'https://www.randomlists.com/fake-name-generator'

        self.driver.get(baseURL)

        data = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Rand-stage')))

        list_of_names = data.find_elements_by_tag_name('li')
        num_of_names = len(list_of_names)
        index = random.choice(range(1, num_of_names))
        name = list_of_names[index].text.strip()

        index = random.choice(range(1, num_of_names))
        self._firstname = name.split()[0]
        self._lastname = name.split()[1]	
    def _adress(self):
        print("Generating adress......")
        baseURL = 'https://fakeaddressgenerator.com/World_Address/get_us_address/city/Detroit'
        new_tab(self.driver, baseURL)
        switch_to(self.driver, 'fakeaddressgenerator')
        self._street = WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div[3]/div[2]/strong/input'))).text
        self._city = 'Detroit'
        self._zip = WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div[7]/div[2]/strong/input'))).text		

      


    def _generate_phone_number(self):
        print("Generating phone numbers....")

        baseURL = 'https://www.fakephonenumber.org/UnitedStates/phone_number_generator?city=detroit'

        new_tab(self.driver, baseURL)
        switch_to(self.driver, 'fakephonenumber')

        self._phone_num = WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/ul[1]/li[1]/p[1]/a'))).text
        
    def getInfo(self):
        info = {}
        self._generate_names()
        self._adress()
        self._generate_phone_number()
        print("Done!")
        info["firstname"] = self._firstname
        info["lastname"] = self._lastname
        info["phone_num"] = self._phone_num
        info["street"] = self._street
        info["city"] = self._city
        info["zip"] = self._zip
        self.driver.quit()
        return info

    def _click_button_by_ID(self, button_ID):
        WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.ID, button_ID))).click()
			
	
  		

    def set_select(self, select_ID, value):
        box = WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.ID, select_ID)))

        option = Select(box)
        option.select_by_value(value)
