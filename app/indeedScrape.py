from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

jobName = input("What is the job title that you are looking for? ")
jobLocation = input("Where are you looking for work? ")

driver = webdriver.Firefox()
driver.get("https://uk.indeed.com/")
driver.implicitly_wait(5)

jobSearchField = "text-input-what"
jobLocationField = "text-input-where"
submitButton = "//*[@id='jobsearch']/div/div[2]/button"

job_title = []
link_ = []

def setupPage():
    driver.find_element(By.ID, jobSearchField).send_keys(jobName)
    driver.find_element(By.ID, jobLocationField).send_keys(jobLocation)
    driver.find_element(By.XPATH, submitButton).click()

def getJobs():
    links = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")

    for link in links:
        job_title.append(link.text)
        link_.append(link.get_attribute("href"))

def createSpreadsheet():
    df = pd.DataFrame({'Job Title': job_title, 'Link:': link_})
    df.to_csv('job_list.csv', index=False)
    print(df)

setupPage()
getJobs()
driver.quit()
createSpreadsheet()