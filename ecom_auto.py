import random
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver


# initialize webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

# Open URL and maximize window
driver.get("http://www.tutorialsninja.com/demo/")
driver.maximize_window()

# phones button
phones = driver.find_element_by_xpath('//a[text()="Phones & PDAs"]')
phones.click()

# iphone
iphone = driver.find_element_by_xpath('//a[text()="iPhone"]')
iphone.click()
time.sleep(5)

# first picture
first_pic = driver.find_element_by_xpath('//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

# next picture
next_click = driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')

for i in range(0, 5):
    next_click.click()
    time.sleep(2)

# save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

close_btn = driver.find_element_by_xpath('//button[@title="Close (Esc)"]')
close_btn.click()
time.sleep(2)

# select quantity in input fields
qty = driver.find_element_by_id("input-quantity")
qty.click()
time.sleep(2)

qty.clear()
time.sleep(2)
qty.send_keys("2")
time.sleep(2)

# add to cart
add_button = driver.find_element_by_id("button-cart")
add_button.click()
time.sleep(2)

laptops = driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2 = driver.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]')
laptops_2.click()

# click on HP Laptop
HP = driver.find_element_by_xpath('//a[text()="HP LP3065"]')
HP.click()
time.sleep(2)

# scroll
cart_button = driver.find_element_by_id("button-cart")
cart_button.location_once_scrolled_into_view
time.sleep(1)

# calender
calender = driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
calender.click()
time.sleep(1)

next_click_calender = driver.find_element_by_xpath('//th[@class="next"]')
month_year = driver.find_element_by_xpath('//th[@class="picker-switch"]')

# year 2021, month: december
while month_year.text != 'December 2022':
    next_click_calender.click()
time.sleep(2)

# day 31
calender_date = driver.find_element_by_xpath('//td[text()="31"]')
calender_date.click()
time.sleep(2)

# add to button
cart_button.click()
time.sleep(2)

# checkout
go_to_cart = driver.find_element_by_id('cart-total')
go_to_cart.click()
time.sleep(1)

checkout = driver.find_element_by_xpath('//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(2)

# click on guest acct
guest = driver.find_element_by_xpath('//input[@value="guest"]')
guest.click()

# clicking continue button
cont_button = driver.find_element_by_id('button-account')
cont_button.click()
time.sleep(1)

# scrolling
billing_acct = driver.find_element_by_xpath('//a[text()="Step 2: Billing Details "]')
billing_acct.location_once_scrolled_into_view
time.sleep(2)

# first name
first_name = driver.find_element_by_id('input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test-name1')
time.sleep(1)

# last name
last_name = driver.find_element_by_id('input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test-last1')
time.sleep(1)

# email
email_name = driver.find_element_by_id('input-payment-email')
email_name.click()
time.sleep(1)
email_name.send_keys('test-email1@yahoo.com')
time.sleep(1)

# telephone
telephone = driver.find_element_by_id('input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('09556678676')
time.sleep(1)

# address
address = driver.find_element_by_id('input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 1567')
time.sleep(1)

# city
city = driver.find_element_by_id('input-payment-city')
city.click()
time.sleep(1)
city.send_keys('London')
time.sleep(1)

# postcode
postcode = driver.find_element_by_id('input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('33688')
time.sleep(1)

# country
country = driver.find_element_by_id('input-payment-country')
dropdown = Select(country)
time.sleep(1)
dropdown.select_by_visible_text('United Kingdom')
time.sleep(1)

# region
region = driver.find_element_by_id('input-payment-zone')
zone = Select(region)
time.sleep(1)
zone.select_by_visible_text('Essex')
time.sleep(1)

cont_button2 = driver.find_element_by_id('button-guest')
cont_button2.click()
time.sleep(2)

cont_button3 = driver.find_element_by_id('button-shipping-method')
cont_button3.click()
time.sleep(1)

# accept terms and conditions
terms = driver.find_element_by_xpath('//input[@name = "agree"]')
terms.click()

cont_button4 = driver.find_element_by_id('button-payment-method')
cont_button4.click()
time.sleep(1)

# final price
final_price = driver.find_element_by_xpath('//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("The final price is:" + final_price.text)
time.sleep(2)

# clicking on the confirmation button
confirm_button = driver.find_element_by_id('button-confirm')
confirm_button.click()

# success text
success_text = driver.find_element_by_xpath('//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

driver.close()





