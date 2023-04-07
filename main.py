# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox()
# driver.get("https://www.gmm-tv.com/shop/index.php?route=account/register")
# driver.set_window_size(1358, 782)
# driver.find_element(By.ID,'input-firstname').send_keys('ณาตหชา')
# driver.find_element(By.ID,'input-lastname').send_keys('มุมแดง')
# driver.find_element(By.ID,'input-email').send_keys('aummumdaeng@gmail.com')
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@value='Submit / ลงทะเบียน']").click()


# # elem = driver.find_element(By.NAME, "q")
# # elem.clear()
# # elem.send_keys("pycon")
# time.sleep(5)
# # elem.send_keys(Keys.RETURN)
# assert "Warning: You must agree to the ข้อตกลง!"  in driver.page_source
# assert "Telephone must be between 3 and 32 characters!"  in driver.page_source
# # time.sleep(5)
# driver.close()


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        # driver = self.driver
        # driver.get("http://www.python.org")
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element(By.NAME, "q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assertEqual("No results found.lllll", driver.page_source)
        self.driver.get(
            "https://www.gmm-tv.com/shop/index.php?route=account/register")
        self.driver.set_window_size(1358, 782)
        self.driver.find_element(By.ID, 'input-firstname').send_keys('ณาตหชา')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('มุมแดง')
        self.driver.find_element(
            By.ID, 'input-email').send_keys('aummumdaeng@gmail.com')
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, "//input[@value='Submit / ลงทะเบียน']").click()

        # elem = driver.find_element(By.NAME, "q")
        # elem.clear()
        # elem.send_keys("pycon")
        # time.sleep(5)
        # elem.send_keys(Keys.RETURN)
        self.assertEqual("Warning: You must agree to the ข้อตกลง!",self.driver.page_source)
    # self.assertEqual("Warning: You must agree to the ข้อตกลง!",self.driver.page_source)
    # assert "Telephone must be between 3 and 32 characters!"  in driver.page_source
    # time.sleep(5)
    def test_search_in_python_v1(self):
        # driver = self.driver
        # driver.get("http://www.python.org")
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element(By.NAME, "q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assertEqual("No results found.lllll", driver.page_source)
        self.driver.get(
            "https://www.gmm-tv.com/shop/index.php?route=account/register")
        self.driver.set_window_size(1358, 782)
        self.driver.find_element(By.ID, 'input-firstname').send_keys('ณาตหชา')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('มุมแดง')
        self.driver.find_element(
            By.ID, 'input-email').send_keys('aummumdaeng@gmail.com')
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, "//input[@value='Submit / ลงทะเบียน']").click()

        # elem = driver.find_element(By.NAME, "q")
        # elem.clear()
        # elem.send_keys("pycon")
        # time.sleep(5)
        # elem.send_keys(Keys.RETURN)
        self.assertEqual("Warning: You must agree to the ข้อตกลง!",self.driver.page_source)
    # self.assertEqual("Warning: You must agree to the ข้อตกลง!",self.driver.page_source)
    # assert "Telephone must be between 3 and 32 characters!"  in driver.page_source
    # time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
