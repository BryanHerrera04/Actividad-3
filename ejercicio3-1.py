from pip import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest
from warnings import filterwarnings
filterwarnings("ignore")

class TestSe(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

	def test_load(self):
		self.browser.get("https://demo.guru99.com/test/login.html")
		email = self.browser.find_element_by_id('email')
		email.send_keys('supplier@phptravels.com')
		password = self.browser.find_element_by_id('passwd')
		password.send_keys('demosupplier')
		ButtonLogin = self.browser.find_element_by_css_selector('#SubmitLogin')
		ButtonLogin.send_keys(Keys.ENTER)
		success = self.browser.find_element_by_css_selector('body > div:nth-child(14) > div')
		print(success)
		self.assertEqual(success.text, "Successfully Logged in...")

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
    main()


	