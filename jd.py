import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start_time = "2021:01:05 10:00:00"

start_time = time.mktime(time.strptime(start_time, "%Y:%m:%d %H:%M:%S"))


def seckill(login_url, login_name, login_passwd, item_url):
    driver = webdriver.Chrome()
    driver.get(login_url)

    login_tab_right = driver.find_element_by_class_name('login-tab-r')  # login
    login_tab_right.click()

    account = driver.find_element_by_id('loginname')
    password = driver.find_element_by_id('nloginpwd')

    account.clear()  # clear
    password.clear()
    account.send_keys(login_name)  # fill with name and password
    password.send_keys(login_passwd)

    submit = driver.find_element_by_id('loginsubmit')
    submit.click()
    time.sleep(10)
    driver.get(item_url)

    if time.time() > start_time:
        exit(0)
    time.sleep(abs(start_time - time.time() - 1))
    while time.time() + 0.3 < start_time:
        time.sleep(0.1)

    try:
        element = WebDriverWait(driver, timeout=10, poll_frequency=0.1).until(
            EC.presence_of_element_located((By.ID, "btn-reservation"))  #modify button ID 
        )
        element.click()
    finally:
        # driver.quit()
        time.sleep(60 * 10)

    driver.close()


if __name__ == '__main__':
    login_url = 'https://passport.jd.com/new/login.aspx'
    item_url = "https://item.jd.com/100017354068.html#crumb-wrap" #item url
    name = 'user_name'
    password = 'password'
    seckill(login_url, name, password, item_url)
