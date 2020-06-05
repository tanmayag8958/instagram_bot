from __future__ import print_function
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = ''
PASSWORD = ''
USERNAME_TO_FOLLOW_FOLLOWING = ''

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.set_window_size(100, 900)
driver.implicitly_wait(10)

def login(username, password):
    driver.get(f"https://www.instagram.com/")
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
    time.sleep(2)
    # username_element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input')))
    username_element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input')
    username_element.send_keys(username)
    password_element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/div/label/input')
    password_element.send_keys(password)
    login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button/div')
    driver.execute_script("arguments[0].click();", login)
    time.sleep(2)

def follow(username):
    driver.get(f"https://www.instagram.com/{username}/")

    # opening following
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[3]/a').click()
    time.sleep(10)

    # following
    follow = driver.find_elements_by_class_name("sqdOP")
    print(len(follow))
    i = 0
    j = 0
    while i <= 20 and j < len(follow):
        if follow[j].text == 'Following' or follow[j].text == 'Requested':
            j += 1
        else:
            driver.execute_script("arguments[0].click();", follow[j])
            j += 1
            i += 1
            # print(follow[i].text)

def dont_follow_back(username):
    driver.get(f"https://www.instagram.com/{username}")
    # time.sleep(5)

    # getting following username
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[3]/a').click()
    time.sleep(20)
    follow = driver.find_elements_by_class_name("notranslate")
    following = []
    for i in  follow:
        following.append(i.text)

    driver.execute_script("window.history.go(-1)")

    # getting followers username
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()
    time.sleep(20)
    follow = driver.find_elements_by_class_name("notranslate")
    followers = []
    for i in  follow:
        followers.append(i.text)

    final = []
    for i in following:
        if i not in followers:
            final.append(i)
    print(len(final))
    print(final)


login(USERNAME, PASSWORD)
dont_follow_back(USERNAME)
follow(USERNAME_TO_FOLLOW_FOLLOWING)
time.sleep(5)


