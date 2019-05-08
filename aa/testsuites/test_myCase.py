#!/usr/bin/env python
# _*_ coding:utf-8 _*_
 
import unittest
import selenium
import time,os
from appium import webdriver
 
class test_myCase(unittest.TestCase):

	@classmethod
	def setUp(self):
		# super().setUp()
		print('selenium version = ', selenium.__version__)
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.4.2'
		desired_caps['deviceName'] = 'Q8W0215324021858'
		desired_caps['appPackage'] = 'com.soufun.app'
		#desired_caps['app'] = 'F:// debug.apk'
		desired_caps['appActivity'] = 'com.soufun.app.activity.MainSplashActivity'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


	def test_something(self):
		now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
		# fname3=base_dir+'/result_file/'+now+str(i)+r"test.png"
		dir_path = os.path.dirname(os.path.abspath('.')) + '\\screen_img\\'
		print(dir_path)
		fname3 = dir_path + now + r"test.png"

		print('test_something click ------ ')
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_name('立即更新').click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_name('买新房').click()
		self.driver.implicitly_wait(10)
		self.driver.save_screenshot(fname3)
		time.sleep(10)


	@classmethod
	def tearDown(self):
		time.sleep(5)
		print('tearDown ------ ')
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
