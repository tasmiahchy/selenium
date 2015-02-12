__author__ = 'tasmiahchoudhury'

import unittest
from selenium import webdriver
class SeleniumPractice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)

    def test_productVisibility(self):
        driver = self.driver
        success = True
        driver.get("http://oldnavy.gap.com/?")

        logo = driver.find_element_by_css_selector("#siteMastheadLogo")

        if logo.is_displayed():
            print "logo is there"
        else:
            print "logo is not there"


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=="__main__":
    unittest.main