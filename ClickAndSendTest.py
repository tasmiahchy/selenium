from lib2to3.pgen2 import driver

__author__ = 'tasmiahchoudhury'

import unittest
from selenium import webdriver
class ClickAndSendTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicity_wait(15)
    def test_ClickAndSend(self):
        driver = self.driver
    driver.get("http://www.amazon.com/")
    #verification.......................................................

    logo = driver.find_element_css_selector(".nav-logo-base.nav-sprite")
    #1
    if logo is None:
        print "logo is not visible"
    else:
        print "logo is visible"
    #2
    if logo.text =="Amazon":
        print "logo is Visible through text method"
    else:
        print "logo is not Visible through text method"
    #3
    if logo.is_displayed():
        print "logo is visible through is_displayed method"
    else:
        print "logo is not visible through is_displayed method"






    def tearDown(self):
        self.driver.close()
        self.driver.quit()
if __name__=="__main__":
    unittest.main()