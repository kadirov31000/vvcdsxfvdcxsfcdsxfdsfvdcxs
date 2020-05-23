import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from pro.useful_functions import new_tab, switch_to
from pro.useful_functions import clear_text_box, username_generator, password_Generator, \
    random_four_digit_PIN
import random

class Kadirov:
    
    def __init__(self, info):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        self.firstname = info.get("firstname")
        self.lastname = info.get("lastname")
        self.phone_num = info.get("phone_num")
        self.alter_phone = info.get("parent_phone")
        self.emailid = self.firstname+ self.lastname+ "@grr.la"
        self.sex = info.get("sex")
        self.emaildd = self.firstname+ self.lastname
        self.birth_month = str(random.choice(range(1, 12)))
        self.birth_day = str(random.choice(range(1, 30)))
        self.birth_year = str(random.choice(range(85, 99)))
        self.street_address = info.get("street")
        self.city = info.get("city")
        self.state = 'MD'
        self.zipcode = info.get("zip")
        self.brth = self.birth_month+ "/"+ self.birth_day+ "/"+ self.birth_year
        self.emailid = self.firstname+ self.lastname

    def genbb(self):
        baseURL = 'https://www.guerrillamail.com/'
        self.driver.get(baseURL)
        self._click_button_by_ID("inbox-id")
        self._set_input_by_XPATH('//*[@id="inbox-id"]/input', self.emaildd)
        self._click_button_by_XPATH('//*[@id="inbox-id"]/button[1]')
        self._click_button_by_XPATH('//*[@id="use-alias"]')
        self.control_bb = "grr.la"
        self.set_select("gm-host-select", self.control_bb)
        time.sleep(2)
    def aek(self):
        self.baseURL = 'https://detp.ent.sirsi.net/client/en_US/default/search/registration/$N/SYMWS/true?'
        new_tab(self.driver, self.baseURL)
        switch_to(self.driver, 'sirsi')
        self.driver.get(self.baseURL)
        WebDriverWait(self.driver, 30)
        self._set_input_by_id('registrationTextField', self.firstname)
        self._set_input_by_id('registrationTextField_1', self.lastname)
        self.emailid = self.firstname+ self.lastname+ "@grr.la"
        self._set_input_by_id('registrationTextField_3', self.brth)
        WebDriverWait(self.driver, 30)
        self._set_input_by_id('confirmField1', self.emailid)
        self._set_input_by_id('confirmField2', self.emailid)
        self.Province = "Michigan"
        self._set_input_by_id('registrationTextField_6', self.Province)
        self._set_input_by_id('registrationTextField_8', self.phone_num)
        time.sleep(2)
        self._set_input_by_id('registrationTextField_4', self.street_address)
        self._set_input_by_id('registrationTextField_5', self.city)
        self._set_input_by_id('registrationTextField_7', self.zipcode)
        time.sleep(1)
        self.PIN = random_four_digit_PIN()
        WebDriverWait(self.driver, 30)
        self._set_input_by_id('pwdField1', self.PIN)
        self._set_input_by_id('pwdField2', self.PIN)
        movie_list = ['BRBO', 'BRCB', 'BRCH', 'BRDG', 'BRJE', 'MAIN', 'BRSF', 'BRSK', 'BRCo', ]
        self.control_Ib = random.choice(movie_list)
        self.set_select("registrationDropDown", self.control_Ib)
        WebDriverWait(self.driver, 30)
	self._click_button_by_XPATH('//*[@id="registrationSubmit"]')
        time.sleep(5)
        self.cardnumber = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="content"]/div[1]/p[2]'))).text
        self.txtx = str(self.cardnumber)
        self.testt = self.txtx[38:45]
        print(self.testt)
    def lynda(self):
        self.baseURL = 'https://www.lynda.com/portal/sip?org=detroitpubliclibrary.org'
        new_tab(self.driver, self.baseURL)
        switch_to(self.driver, 'lynda')
        self.driver.get(self.baseURL)
        WebDriverWait(self.driver, 30)
        self._set_input_by_id('card-number', self.testt)
        self._set_input_by_id('card-pin', self.PIN)
        self._click_button_by_XPATH('//*[@id="submit-library-card"]')
        time.sleep(7)
        self._click_button_by_XPATH('//*[@id="sso_profile"]/div[2]/div[1]/form[2]/input[1]')
        time.sleep(7)
        self._set_input_by_id('f_name', self.firstname)
        self._set_input_by_id('l_name', self.lastname)
        self._set_input_by_id('email_addr', self.emailid)
        self._click_button_by_XPATH('//*[@id="btn_save"]').click()
        time.sleep(7)
        print('success')

    ################################################################################################
    #                                                                                              #
    #                                   useful function                                            #
    #                                                                                              #
    #################################################################################################

    # for selecting date works only if...select and options are availble!
    def set_date_box(self, month=None, day=None, year=None, month_id=None, day_id=None, year_id=None):

        if month_id != None:
            select_month_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, month_id)))
            select_month = Select(select_month_box)
            select_month.select_by_value(month)

        if day_id != None:
            select_day_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, day_id)))
            select_day = Select(select_day_box)
            select_day.select_by_value(day)

        if year_id != None:
            select_year_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, year_id)))
            select_year = Select(select_year_box)
            select_year.select_by_value(year)

    def _click_button_by_XPATH(self, button_XPATH):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, button_XPATH))).click()

    def _click_button_by_ID(self, button_ID):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, button_ID))).click()

    def _set_input_by_id(self, input_box_id, input_value):
        input_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, input_box_id))
        )
        clear_text_box(input_box)
        input_box.send_keys(input_value)

    def _set_input_by_XPATH(self, input_box_XPATH, input_value):
        input_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, input_box_XPATH))
        )
        clear_text_box(input_box)
        input_box.send_keys(input_value)

    def _click_by_link_text(self, text):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text))
        ).click()

    def set_select(self, select_ID, value):
        box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, select_ID)))

        option = Select(box)
        option.select_by_value(value)

    def set_select_by_class(self, class_name, value):
        box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name)))

        option = Select(box)
        option.select_by_value(value)

    #################################################################################################
        
	
    def save_info(self):
	    
			
        print("======================")
        print("https://www.lynda.com/portal/sip?org=detroitpubliclibrary.org")
        print("cardnumber ==> {}".format(self.testt))
        print("PIN number ==> {}".format(self.PIN))
        print("emailID ==> {}".format(self.emailid))
        print("=========================")
        print("all info are saved!")

        with open("accountinfo.txt", 'a') as txtFile:
            txtFile.writelines("===================================================\n")
            txtFile.writelines("Firstname ==> {}\n".format(self.firstname))
            txtFile.writelines("Lastname ==> {}\n".format(self.lastname))
	    txtFile.writelines("https://www.lynda.com/portal/sip?org=detroitpubliclibrary.org")
            txtFile.writelines("cardnumber ==> {}".format(self.testt))                                                                            #self.lastname[0].lower()))
            txtFile.writelines("PIN number ==> {}\n".format(self.PIN))
            txtFile.writelines("emailID ==> {}\n".format(self.emailid))
            txtFile.writelines("===================================================\n")

		
    def logout(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Return'))).click()
