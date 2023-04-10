import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class testdata(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testdata(self):
        driver = self.driver
        driver.get("http://localhost:3000/index.php")
        driver.set_window_size(1358, 782)
        # driver.find_element(By.XPATH, "//*[@id='formGroupExampleInput2']").send_keys('ณาตหชา มุมแดง')
        driver.find_element(By.XPATH, "//form/input").send_keys('2023/4/9')
        # driver.find_element(By.XPATH, "//div[2]/input").send_keys('83')
        driver.find_element(By.XPATH, "//button[@name='submit']").click()
        time.sleep(6)
        # driver.find_element(By.XPATH, "//body").click()

        try:
           WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                          'กรุณากรอกชื่อสกุล!')

           alert = driver.switch_to.alert
           alert.accept()
           print("alert accepted")
           time.sleep(6)

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
