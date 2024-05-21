from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path # this will get you the path variable

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
# Navigate to my blog
driver.get("https://cerebro1.github.io/")
# Click on the About button
about = driver.find_element(By.LINK_TEXT, 'About')
about.click()
# Close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
