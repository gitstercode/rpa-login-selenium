from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1557722430&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fRpsCsrfState%3df374953e-f31d-f751-a9c8-23841931793a&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')

userElem = browser.find_element_by_id('i0116')
userElem.send_keys('me@hotmail.com') #admn no here

#nextElem = browser.find_element_by_xpath("//*[@data-reactid='22']")
nextElem = browser.find_element_by_id('idSIButton9')
nextElem.click()

# Wait for 2 seconds
time.sleep(2)

passElem = browser.find_element_by_id('i0118')
passElem.send_keys('my-pass')

loginElem = browser.find_element_by_id('idSIButton9')
loginElem.click()