from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.gmm-tv.com/shop/index.php?route=account/register")
driver.set_window_size(1358, 782)
driver.find_element(By.ID,'input-firstname').send_keys('ณาตหชา')
driver.find_element(By.ID,'input-lastname').send_keys('มุมแดง')
driver.find_element(By.ID,'input-email').send_keys('aummumdaeng@gmail.com')
driver.find_element(By.ID,'input-telephone').send_keys('0656375524')
# driver.find_element(By.ID,'input-password').send_keys('natthacha2002')
# driver.find_element(By.ID,'input-confirm').send_keys('natthacha2002')
driver.find_element(By.XPATH,"//input[@name='agree']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='Submit / ลงทะเบียน']").click()


# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
time.sleep(5)
# elem.send_keys(Keys.RETURN)
assert "Password must be between 4 and 20 characters!"  in driver.page_source
# assert "Telephone must be between 3 and 32 characters!"  in driver.page_source
# time.sleep(5)
driver.close()