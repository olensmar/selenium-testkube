from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)
# Maximize the window size
driver.maximize_window()
print("Timer1")
time.sleep(5)
# Navigate to my blog
driver.get("https://cerebro1.github.io/")
print("Get Successful")
time.sleep(5)
# Click on the About button
about = driver.find_element(By.LINK_TEXT, 'About')
about.click()
print("Click Successful")
time.sleep(5)
# Close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
