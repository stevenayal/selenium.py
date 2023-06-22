import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\driver_chromechromedriver.exe')
class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=s)

    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google",driver.title)
        elemento = driver.find_element('name','q')
        elemento.send_keys("Banco Continental")
        elemento.send_keys(Keys.RETURN)
        time.sleep(15)
        assert "No se encontro el elemento." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()