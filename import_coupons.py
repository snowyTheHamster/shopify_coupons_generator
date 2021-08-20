from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui as pag
import traceback
import csv
from getpass import getpass

# start loop here
def import_coupons(percentage, minimum, datestart, timestart, dateend, timeend, coupon_csv, site_url, username, password):

    # pyautogui select and delete element
    def pag_delete_element():
        sleep(0.5)
        pag.hotkey('ctrl', 'a')
        sleep(0.5)
        pag.hotkey('delete')
        sleep(0.5)

    # webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='C:\\webdrivers\\chromedriver.exe', options=options) # win10
    driver.set_window_position(420, 0)
    driver.set_window_size(1120, 1000)

    url_login = f'https://{site_url}/admin/discounts'
    print(f'attempt access to: {url_login}')


    # start here
    driver.get(url_login)

    driver.find_element_by_id('account_email').send_keys(username)
    sleep(3)
    driver.find_element_by_css_selector('.ui-button.ui-button--primary.ui-button--size-large.captcha__submit').click()
    sleep(3)
    driver.find_element_by_css_selector('.ui-password__input.next-input.next-input--invisible.js-password-input.transferable-input').click()
    driver.find_element_by_css_selector('.ui-password__input.next-input.next-input--invisible.js-password-input.transferable-input').send_keys(password)
    sleep(3)
    driver.find_element_by_css_selector('.ui-button.ui-button--primary.ui-button--size-large.captcha__submit').click()
    sleep(10)

    # coupon codes to import
    with open(coupon_csv, mode='r') as csv_file:
        coupons = csv.reader(csv_file)

        for index, coupon in enumerate(coupons, 1):
            print(f'importing coupon no.{index}, code:{coupon}')
            driver.find_element_by_css_selector('.Polaris-Button_r99lw.Polaris-Button--primary_7k9zs').click() # click Create discount btn
            sleep(2)

            driver.find_element_by_css_selector('._2686F').click() # click "Discount code" link
            sleep(2)

            # paste code (unique code per iteration)
            driver.find_element_by_xpath("//input[@placeholder='e.g. SPRINGSALE']").send_keys(coupon) # add unique coupon code
            sleep(3)

            # select percentage or fixed amount (optional) # skip

            # enter discount e.g.: 15 (variable)
            driver.find_element_by_css_selector('#percentageValueField').send_keys(percentage) # add percentage here
            sleep(2)

            # select applies to (optional) # skip

            # select minimum amout hkd
            driver.execute_script("window.scrollTo(0, 500)") # scroll down 500 pixels
            sleep(1)
            driver.find_element_by_xpath("//label[@for='PolarisRadioButton9']").click()
            sleep(1)

            # input minimum amount if clicked previous e.g.: 500 (variable)
            driver.find_element_by_css_selector('#discountPrerequisiteSubtotal').send_keys(minimum) # add minimum value here
            sleep(1)
            driver.execute_script("window.scrollTo(0, 1080)") # scroll down
            sleep(1)

            # limit no of times use (optional)

            # enter start date 2021-09-01 (variable)
            driver.find_element_by_css_selector('#StartEmbeddedDatePicker').click()
            pag_delete_element()
            driver.find_element_by_css_selector('#StartEmbeddedDatePicker').send_keys(datestart) # add start time

            # enter start time 12:00 am
            driver.find_element_by_css_selector('#StartTimeField').click()
            pag_delete_element()
            driver.find_element_by_css_selector('#StartTimeField').send_keys(timestart) # add start time
            sleep(1)


            # click set end date
            btns = driver.find_elements_by_xpath("//*[contains(text(), 'Set end date')]")
            for btn in btns:
                btn.click()
            sleep(1)
            driver.execute_script("window.scrollTo(0, 1080)") # scroll down
            sleep(1)

            # enter end date 2021-09-01 (variable)
            driver.find_element_by_css_selector('#EndEmbeddedDatePicker').click()
            pag_delete_element()
            driver.find_element_by_css_selector('#EndEmbeddedDatePicker').send_keys(dateend) # add end date
            sleep(1)

            # enter end time 11:59 pm
            driver.find_element_by_css_selector('#EndTimeField').click()
            pag_delete_element()
            driver.find_element_by_css_selector('#EndTimeField').send_keys(timeend) # add end time
            sleep(1)

            # click 'save discount code'
            btns = driver.find_elements_by_xpath("//*[contains(text(), 'Save discount code')]")
            for btn in btns:
                btn.click()
            sleep(7)
            print(f'done no.{index}')

            # click back to discounts main page
            driver.get(f'https://{site_url}/admin/discounts/')
            sleep(7)

    print('finished importing coupons, you may now close the program')