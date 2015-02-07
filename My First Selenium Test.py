__author__ = 'tasmiahchoudhury'
import unittest
from selenium import webdriver
class MyFirstSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)

    def test_ProductVisibility(self):
        driver = self.driver
        success = True

        driver.get("http://www.amazon.com/")

        cart = driver.find_element_by_css_selector("#nav-cart").is_displayed()
        if cart:

            print "cart is visible"
        else:
            print "cart is not visible"

        self.assertTrue(success)

        """if cart.is_displayed():
            print "cart is visible"
        else:
            print "cart is not visible"

        logo = driver.find_element_by_css_selector(".nav-logo-base.nav-sprite")

        if logo.is_displayed():
            print "logo is there"
        else:
            print "logo is not there"

        account = driver.find_element_by_css_selector("#nav-your-account")

        if account.is_displayed():
            print "account is ok"
        else:
            print "account is not ok"""



    def teardown(self):
        self.driver.close()
        self.driver.quit()

if __name__=="__main__":
    unittest.main()