#IMPORT LIBRARIES FROM SELENIUM
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from parsel import Selector
#ASK FOR TERM TO FIND
termtofind = raw_input("Term to find: ")

#READ ACCOUNTS ON FILE
file = open("accounts.txt", "r")
line = file.readline()
account = line.split(" // ")

#EXTRACT USER AND PASSWORD OF ONE ACCOUNT
usernameStr = account[0]
passwordStr = account[1]

#SHOW ACCOUNT
print("Account selected: " + usernameStr)

#OPEN NEW WINDOW ON FIREFOX
print("Initializing components")
driver = webdriver.Firefox()

#OPEN URL ON BROWSER
print("Connecting")
driver.get(('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin'))

#INSERT LOGGING DATA ON LINKEDIN
print("Logging in")
username = driver.find_element_by_id('username')
username.send_keys(usernameStr)
password = driver.find_element_by_id('password')
password.send_keys(passwordStr)
driver.find_element_by_css_selector('.btn__primary--large.from__button--floating').click()

#SEARCH ON LINKEDIN
print("Searching")
driver.find_element_by_css_selector('.search-global-typeahead__input').send_keys(termtofind, Keys.ENTER)

driver.find_element_by_id('network-F').click()

#linkedin_urls = driver.find_elements_by_css_selector('.search-result__result-link.ember-view')

#linkedin_urls = driver.find_elements_by_xpath("//div[@class='search-result__result-link ember-view']")

#linkedin_urls = driver.find_elements_by_class_name('search-result__result-link')

#print(linkedin_urls)

#sel = Selector(text = driver.page_source)
#name = sel.xpath('//*[starts-with(@class,"search-result__result-link ember-view")]/text()').extract_first()
#print(name)
#https://linuxhint.com/selenium-web-automation-python/