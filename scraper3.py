from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


options = webdriver.EdgeOptions()

cwd = os.getcwd()
prefs = {"download.default_directory" : cwd}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.use_chromium = True
# options.add_argument("headless")
options.add_argument("--guest")

browser = webdriver.Edge(options = options)

browser.get("https://www.instagram.com/")
browser.maximize_window()

#login
time.sleep(5)
username = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys("_username_")
password = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys("xxxx")

login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#save your login info?
time.sleep(10)
notnow = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div").click()
#turn on notif
time.sleep(10)
notnow2 = browser.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

#searchbox
time.sleep(10)
searchbutton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div").click()
time.sleep(5)
searchbox = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("bbcnewsindia")
time.sleep(10)
firstoption = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div").click()
time.sleep(5)

# scroll
# scrolldown = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
# time.sleep(5)
# match=False
# while(match==False):
#     last_count = scrolldown
#     time.sleep(3)
#     scrolldown = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#     if last_count==scrolldown:
#         match=True

#posts
posts = []
reels = []
links = browser.find_elements(By.TAG_NAME, 'a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
      posts.append(post)
    if '/reel/' in post:
       reels.append(post)
# print(posts)
# print(reels)

#get news text
text = []
for post in posts:
    browser.get(post)
    time.sleep(10)
    news = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span")
    text.append(news.text)
for reel in reels:
    browser.get(reel)
    time.sleep(10)
    news = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span")
    text.append(news.text)
# print(len(text))

for i in range(len(text)):
    # print(text[i])
    sentences = text[i].split(".")
    text[i] = ". ".join(s for s in sentences if "link in bio" not in s)
    text[i] = text[i].strip('\n')

# print(len(text))
# for i in text:
#     print(i,"\nnext\n")

with open('Extracted_News.txt', 'w') as textfile:
    for i in text:
        textfile.write(i)
