from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import pymongo
from pymongo import MongoClient
import json
from mouse_tracker import mouse_tracker
import csv
import time

# move mouse like human
def move_like_human(driver):
    '''
    move mouse by give offset
    '''
    l = []
    with open('track.txt','r') as f:
        l = json.load(f)

    for offset, t in l:
        x, y = offset
        ActionChains(driver).move_by_offset(x,y).perform()
        time.sleep(t)

    ActionChains(driver).click().perform()


def crack(driver):
    ''' move the mouse like human, crack the geetest!'''

    # Waiting for page loading.
    class button():
        def __call__(self, driver):
            if driver.find_element_by_xpath('//div[@aria-label="点击按钮进行验证"]'):
                return True
            else:
                return False
    WebDriverWait(driver, 10, 0.5).until(button())

    # find button and move to the button
    btn = driver.find_element_by_xpath('//div[@aria-label="点击按钮进行验证"]')
    ActionChains(driver).move_to_element(btn).perform()
    
    move_like_human(driver)

    # Crack it!!!
    ActionChains(driver).click().perform()

    time.sleep(5)

    # Waiting for login success.
    driver.implicitly_wait(10)

    while True:
        if driver.current_url.find('m.weibo.cn'):
            break
        if driver.current_url.find('https://weibo.cn/'):
            break

    # return cookies
    return driver.get_cookies()


def get_cookies(username, password):
    ''' get cookies by selenium'''

    # start Chrome headless, need to add --headless arguments.
    driver = webdriver.Chrome()

    # Get entrance
    driver.implicitly_wait(5)
    driver.get('https://passport.weibo.cn/signin/login')

    # Waiting for page loading.
    class button():
        def __call__(self, driver):
            if driver.find_element_by_xpath('//*[@id="loginAction"]'):
                return True
            else:
                return False
    WebDriverWait(driver,10, 0.5).until(button())

    # Input username and password
    username_area = driver.find_element_by_xpath('//*[@id="loginName"]')
    username_area.send_keys(username)
    time.sleep(3)
    psw_area = driver.find_element_by_xpath('//*[@id="loginPassword"]')
    psw_area.send_keys(password)

    # Submit
    btn = driver.find_element_by_xpath('//*[@id="loginAction"]')
    btn.click()
        

    # if their is a CAPTCHA, then crack it.
    if driver.current_url.find('CAPTCHA'):
        print('need crack')
        cookies = crack(driver)
    else:
        cookies = driver.get_cookies()

    cookies_dict = {}
    for d in cookies:
        cookies_dict[d['name']] = d['value']
    print('---------------------------------')
    print(username)
    print(cookies_dict)
    print('---------------------------------')
    driver.quit()
    return cookies_dict


def get_Account(filename, delimiter):
    ''' get account from csv files'''
    l = []
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=delimiter)
        for i in lines:
            yield i

if __name__ == '__main__':
    l = get_Account('account2.csv', '-')
    client = MongoClient()
    db = client['accounts']
    collection = db['cookies']
    for account_tuple in l:
        username, password = account_tuple
        cookies = get_cookies(username, password)
        d = {}
        d['username'] = username
        d['password'] = password
        d['cookies'] = json.dumps(cookies)
        result = collection.insert_one(d)
        print(username, ',  Write down to db success')

