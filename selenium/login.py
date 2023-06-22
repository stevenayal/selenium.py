from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\driver_chromechromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://gmail.com")
time.sleep(3)

usuario = driver.find_element("id","identifierId")
usuario.send_keys("stevengilbertayala@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(5)

siguiente = driver.find_element("aria-label","Try again")
siguiente.send_keys(Keys.ENTER)

clave = driver.find_element("name","password")
clave.send_keys("kiokkcokp1")
clave.send_keys(Keys.ENTER)