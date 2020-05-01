from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Znaleziono element <%s> wraz z taka nazwa klasy!' % (elem.tag_name))
except:
    print('Nie udalo sie znalezc elementu wraz z podana nazwa klasy.')
