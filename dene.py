import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


sayi1 = 2
islemtekrari = 0

while int(sayi1) > islemtekrari:

    chrome_options = webdriver.ChromeOptions()

    chrome = webdriver.Chrome()
    chrome.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

    try:
        elem = chrome.find_element_by_xpath('//*[@id="code"]')

        if elem.is_displayed():
            print("var")

    except NoSuchElementException:
        print("yok")

