from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://uk.indeed.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID, "text-input-what").send_keys("software tester")
driver.find_element(By.ID, "text-input-where").send_keys("fareham")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

links = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")

job_title = []
link_ = []

for link in links:
    job_title.append(link.text)
    link_.append(link.get_attribute("href"))

driver.quit()

df = pd.DataFrame({'Job Title': job_title, 'Link:': link_})
df.to_csv('job_list.csv', index=False)
print(df)
