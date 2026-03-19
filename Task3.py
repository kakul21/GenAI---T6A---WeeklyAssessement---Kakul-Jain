from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"name").send_keys("Kakul")
sleep(2)
driver.find_element(By.ID,"email").send_keys("ABC@gmail.com")
sleep(2)
driver.find_element(By.ID,"password").send_keys("1234567")
sleep(2)
driver.close()