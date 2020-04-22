from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random

#Load the webdriver (using chromdedriver in this case) and maximise the window. this helps makes all elements clickable)
driver = webdriver.Chrome()
driver.maximize_window()

def websitepassword(url, password):
    #log in to passworded shopify stores
    driver.get(url)
    password_element = driver.find_element_by_id('password')
    password_element.send_keys(password)
    submit = driver.find_element_by_xpath('/html/body/div/div[1]/form/div/input')
    submit.click()


def item_to_cart(url):
    #add the product to the cart from the direct product url
    driver.get(url)
    add_to_cart = driver.find_element_by_xpath('//*[@id="purchase"]')
    #unit_qty = driver.find_element_by_xpath('//*[@id="quantity"]')
    #unit_qty.send_keys(Keys.BACK_SPACE)
    #unit_qty.send_keys('1')
    add_to_cart.click()

    #sleep catches delay between adding items to cart and clicking to cart
    time.sleep(2)

    #cart URL still hardcoded..
    driver.get('https://amsp.wasteheadquarters.com/cart')
    driver.implicitly_wait(10)
    terms_checkbox = driver.find_element_by_xpath('//*[@id="agree"]')
    terms_checkbox.click()

    checkout = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div[2]/div[2]/input')
    checkout.click()

def shipping_details():
    #shipping details page
    checkout_email = driver.find_element_by_xpath('//*[@id="checkout_email"]')
    checkout_first = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
    checkout_last = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
    checkout_address = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]')
    checkout_city = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]')
    checkout_postcode = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]')
    checkout_phone = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]')

    checkout_email.send_keys('jack.rooney@sandbaguk.com')
    checkout_first.send_keys('Jack')
    checkout_last.send_keys('Rooney')
    checkout_address.send_keys('50 milford rd')
    checkout_city.send_keys('Reading')
    checkout_postcode.send_keys('RG1 8LJ')
    checkout_phone.send_keys('07377385538')

    #scroll to bottom of page to get to submit button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button')
    submit.click()
    time.sleep(1)

def payment():
    continue_to_pay = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button')
    continue_to_pay.click()
    time.sleep(3)

    driver.switch_to.frame(0)
    driver.find_element_by_xpath('//*[@id="number"]').send_keys('1')
    driver.switch_to.default_content()
    driver.switch_to.frame(1)
    driver.find_element_by_xpath('/html/body/form/input[2]').send_keys('Bogus Gateway')
    driver.switch_to.default_content()
    driver.switch_to.frame(2)
    driver.find_element_by_xpath('/html/body/form/input[5]').send_keys('1121')
    driver.switch_to.default_content()
    driver.switch_to.frame(3)
    driver.find_element_by_xpath('/html/body/form/input[6]').send_keys('333')  

    driver.switch_to.default_content()

    time.sleep(1)

    #scroll to bottom of page to get to submit button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[3]/div[1]/button')
    submit.click()


websitepassword('https://amsp.wasteheadquarters.com/password', 'sandbagwhq2016')


for i in range(0,3):
    item_to_cart('https://amsp.wasteheadquarters.com/products/cd')
    shipping_details()
    payment()
    time.sleep(6)
