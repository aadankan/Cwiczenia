from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

html = browser.find_element_by_tag_name('html')
for i in range(100):
    for j in range(1000):
        html.send_keys(Keys.UP)
        html.send_keys(Keys.RIGHT)
        html.send_keys(Keys.DOWN)
        html.send_keys(Keys.LEFT)
        try:
            retry = browser.find_element_by_class_name('retry-button')
            retry.click()
        except:
            continue
