from selenium import webdriver
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)
#maximize the window size
driver.maximize_window()
time.sleep(10)
#navigate to testkube.io
driver.get("https://testkube.io//")
time.sleep(10)
#click on the Get started button
driver.find_element_by_link_text("Get Started").click()
time.sleep(10)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
