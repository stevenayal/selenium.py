import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\driver_chromechromedriver.exe')

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=s)

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        #buscar_por_xpath = driver.find_element_by_xpath("//*[@id='q']")
        buscar_por_xpath = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
        time.sleep(3)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

#xpath es una estructura de objetos
#xpath relativo = busca en todo el arbol
#ejemplo: //*[@id="q"]

#xpath absoluto = se define la ruta del objeto de manera fija