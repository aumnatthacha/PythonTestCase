# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Firefox()

# driver.get('http://localhost:3000/index.php')
# driver.set_window_size(784, 816)
# # user = driver.find_element(By.XPATH, '//*[@id="formGroupExampleInput2"]')
# # user.send_keys('ณาตหชา มุมแดง')
# driver.find_element(By.XPATH, "//*[@id='formGroupExampleInput2']").send_keys('ณาตหชา มุมแดง')
# driver.find_element(By.XPATH, "//form/input").send_keys('9/4/2566')
# driver.find_element(By.XPATH, "//div[2]/input").send_keys('83')
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@name='submit']").click()
# time.sleep(5)
# assert "...done!" in driver.page_source
# driver.close()

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class testdata(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testdata(self):
        driver = self.driver
        driver.get("http://localhost:3000/index.php")
        driver.set_window_size(1358, 782)
        driver.find_element(
            By.XPATH, "//*[@id='formGroupExampleInput2']").send_keys('ณาตหชา มุมแดง')
        driver.find_element(By.XPATH, "//form/input").send_keys('2023/4/9')
        driver.find_element(By.XPATH, "//div[2]/input").send_keys('83')
        driver.find_element(By.XPATH, "//button[@name='submit']").click()
        # driver.find_element(By.XPATH, "//body").click()
        try:
           WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                           '...done!')

           alert = driver.switch_to.alert
           alert.accept()
           print("alert accepted")

        except TimeoutException:
            print("no alert")
            # self.assertIn("...done!", driver.page_source)
            # driver.find_element(By.XPATH,"//body").click()
        driver.close()

    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# browser = webdriver.Firefox()
# browser.get("url")
# browser.find_element_by_id("add_button").click()

# try:
#     WebDriverWait(browser, 3).until(EC.alert_is_present(),
#                                    'Timed out waiting for PA creation ' +
#                                    'confirmation popup to appear.')

#     alert = browser.switch_to.alert
#     alert.accept()
#     print("alert accepted")
# except TimeoutException:
#     print("no alert")
