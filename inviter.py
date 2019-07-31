import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import requests
import re
from python3_anticaptcha import NoCaptchaTaskProxyless, NoCaptchaTask
#from python_rucaptcha import ReCaptchaV2, RuCaptchaControl
#import recaptcha
import unittest

import random

login = ''
pas = ''
mes = ['Добро пожаловать']

s = requests.Session()

driver = webdriver.Chrome(executable_path='/Users/jbloodless/Downloads/chromedriver')
driver.set_window_size(1366, 768)
driver.implicitly_wait(3)
driver.get('https://vk.com')
#time.sleep(random.randint(3,10))
username = driver.find_element_by_id('index_email')
username.clear()
username.send_keys(login)
password = driver.find_element_by_id('index_pass')
password.clear()
password.send_keys(pas)
log = driver.find_element_by_id('index_login_button')
time.sleep(random.randint(3,8))


log.click()

i = 0
driver.get('https://vk.com/away.php?utf=1&to=https%3A%2F%2Fvk.com%2Fsearch%3Fc%255Binvite%255D%3D130890678%26c%255Bsection%255D%3Dpeople%26from%3Devinv')

SCROLL_PAUSE_TIME = 0.75

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(3)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

time.sleep(3)

message_op = driver.find_elements_by_css_selector('.flat_button.button_small.button_wide')
print(message_op)
message_already = driver.find_elements_by_css_selector('.flat_button.button_small.button_wide.secondary')
print(message_already)
message_unclick = driver.find_elements_by_css_selector('.flat_button.button_small.button_wide.button_disabled')
print(message_unclick)
message_clickable=list(set(message_op)-set(message_unclick))
message_click = list(set(message_clickable)-set(message_already))
#message_click = sorted(message_click)
print(message_click)

api_key='d0b8ce8af338e44ee5789056c7c06107'
site_key='6Le00B8TAAAAACHiybbHy8tMOiJhM5vh88JVtP4c'
url = 'https://vk.com/away.php?utf=1&to=https%3A%2F%2Fvk.com%2Fsearch%3Fc%255Binvite%255D%3D130890678%26c%255Bsection%255D%3Dpeople%26from%3Devinv'

response = 0


time.sleep(random.randint(3,8))

for j in range(len(message_click)):       # iterator on all downloaded buttons
    try:
        actions = ActionChains(driver)
        actions.move_to_element(message_click[j]).perform()
        #location = message_click[j].location["y"] - 100
        #driver.execute_script("window.scrollTo(0, %d);" % location)
        #message_click[j].click()
        try:
            message_click[j].click()
        except WebDriverException:
            location = message_click[j].location["y"] - 100
            driver.execute_script("window.scrollTo(0, %d);" % location)
            time.sleep(3)
            try:
                message_click[j].click()
            except WebDriverException:
                result = NoCaptchaTaskProxyless.NoCaptchaTaskProxyless(anticaptcha_key=api_key) \
                    .captcha_handler(websiteURL=url,
                                     websiteKey=site_key)

                #result = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=api_key).captcha_handler(site_key=site_key,
                #                                                                        page_url=url)
                #gcap1 = requests.post(url, result)
                print(result)
                response_dict = result.get('solution')
                response = response_dict.get('gRecaptchaResponse')
                #response = result['captchaSolve']
                print(response)
                try:
                    driver.execute_script(
                        "document.getElementById('g-recaptcha-response').style.removeProperty('display');")
                    driver.find_element_by_id('g-recaptcha-response').send_keys(response)
                    token = '"' + response + '"'
                    driver.execute_script("___grecaptcha_cfg.clients[0].xd.O.callback(%s)" % token)
                    time.sleep(8)
                    message_click[j].click()
                    time.sleep(random.randint(3, 8))
                except WebDriverException:
                    try:
                        driver.execute_script(
                        "document.getElementById('g-recaptcha-response-1').style.removeProperty('display');")
                        driver.find_element_by_id('g-recaptcha-response-1').send_keys(response)
                        token = '"' + response + '"'
                        driver.execute_script("___grecaptcha_cfg.clients[1].xd.O.callback(%s)" % token)
                        time.sleep(8)
                        message_click[j].click()
                        time.sleep(random.randint(3, 8))
                    except WebDriverException:
                        try:
                            driver.execute_script(
                                "document.getElementById('g-recaptcha-response-2').style.removeProperty('display');")
                            driver.find_element_by_id('g-recaptcha-response-2').send_keys(response)
                            token = '"' + response + '"'
                            driver.execute_script("___grecaptcha_cfg.clients[2].xd.O.callback(%s)" % token)
                            time.sleep(8)
                            message_click[j].click()
                            time.sleep(random.randint(3, 8))
                        except WebDriverException:
                            try:
                                driver.execute_script(
                                    "document.getElementById('g-recaptcha-response-3').style.removeProperty('display');")
                                driver.find_element_by_id('g-recaptcha-response-3').send_keys(response)
                                token = '"' + response + '"'
                                driver.execute_script("___grecaptcha_cfg.clients[3].xd.O.callback(%s)" % token)
                                time.sleep(8)
                                message_click[j].click()
                                time.sleep(random.randint(3, 8))
                            except WebDriverException:
                                try:
                                    driver.execute_script(
                                        "document.getElementById('g-recaptcha-response-4').style.removeProperty('display');")
                                    driver.find_element_by_id('g-recaptcha-response-4').send_keys(response)
                                    token = '"' + response + '"'
                                    driver.execute_script("___grecaptcha_cfg.clients[4].xd.O.callback(%s)" % token)
                                    time.sleep(8)
                                    message_click[j].click()
                                    time.sleep(random.randint(3, 8))
                                except WebDriverException:
                                    try:
                                        driver.execute_script(
                                            "document.getElementById('g-recaptcha-response-5').style.removeProperty('display');")
                                        driver.find_element_by_id('g-recaptcha-response-5').send_keys(response)
                                        token = '"' + response + '"'
                                        driver.execute_script("___grecaptcha_cfg.clients[5].xd.O.callback(%s)" % token)
                                        time.sleep(8)
                                        message_click[j].click()
                                        time.sleep(random.randint(3, 8))
                                    except WebDriverException:
                                        try:
                                            driver.execute_script(
                                                "document.getElementById('g-recaptcha-response-6').style.removeProperty('display');")
                                            driver.find_element_by_id('g-recaptcha-response-6').send_keys(response)
                                            token = '"' + response + '"'
                                            driver.execute_script(
                                                "___grecaptcha_cfg.clients[6].xd.O.callback(%s)" % token)
                                            time.sleep(8)
                                            message_click[j].click()
                                            time.sleep(random.randint(3, 8))
                                        except WebDriverException:
                                            try:
                                                driver.execute_script(
                                                    "document.getElementById('g-recaptcha-response-7').style.removeProperty('display');")
                                                driver.find_element_by_id('g-recaptcha-response-7').send_keys(response)
                                                token = '"' + response + '"'
                                                driver.execute_script(
                                                    "___grecaptcha_cfg.clients[7].xd.O.callback(%s)" % token)
                                                time.sleep(8)
                                                message_click[j].click()
                                                time.sleep(random.randint(3, 8))
                                            except WebDriverException:
                                                pass
    except ElementNotVisibleException:
        result = NoCaptchaTaskProxyless.NoCaptchaTaskProxyless(anticaptcha_key=api_key) \
            .captcha_handler(websiteURL=url,
                             websiteKey=site_key)
        #gcap1 = requests.post(url, result)
        response_dict=result.get('solution')
        response=response_dict.get('gRecaptchaResponse')
        print(response)
        driver.execute_script(
            "document.getElementById('g-recaptcha-response').style.removeProperty('display');")
        driver.find_element_by_id('g-recaptcha-response').send_keys(response)
        token = '"' + response + '"'
        driver.execute_script("___grecaptcha_cfg.clients[0].xd.O.callback(%s)" % token)
        #gcap = requests.post(url, response_dict)
        #driver.find_element_by_id('g-recaptcha-response').submit()
        #recaptcha.process()
        time.sleep(15)
        message_click[j].click()
        time.sleep(random.randint(3, 10))




