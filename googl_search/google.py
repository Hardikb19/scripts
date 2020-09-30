from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

while True:
    google_search = input('Enter your google search (000 to exit): ')
    if google_search == "000":
        print('Exiting....')
        time.sleep(1)
        break
    driver = webdriver.Chrome()

    driver.get('https://google.com/')
    searchbox = driver.find_element_by_xpath(
        '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    searchbox.send_keys(google_search)
    searchbox.send_keys(Keys.RETURN)  # hits enter
    '''
    this method clicks the mentioned buttoni

    button = driver.find_element_by_xpath(
        '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    button.click()
    '''
    driver.back()
    driver.forward()
    time.sleep(5)

    driver.quit()
