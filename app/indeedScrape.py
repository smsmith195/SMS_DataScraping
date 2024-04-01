from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# User input variables for searching a job title and location
jobName = input("What is the job title that you are looking for? ")
jobLocation = input("Where are you looking for work? ")

# Launch Firefox on the Indeed homepage
driver = webdriver.Firefox()
driver.get("https://uk.indeed.com/")

# Variables for search fields and submit button
jobSearchField = "text-input-what"
jobLocationField = "text-input-where"
submitButton = "//*[@id='jobsearch']/div/div[2]/button"

# Lists for extracted data for the spreadsheet
job_title = []
link_ = []
location_ = []
company_ = []

# File name for the spreadsheet
fileName = 'job_list.csv'

# Takes in initial user input and searches it in Indeed
def setupPage():
    driver.find_element(By.ID, jobSearchField).send_keys(jobName)
    driver.find_element(By.ID, jobLocationField).send_keys(jobLocation)
    driver.find_element(By.XPATH, submitButton).click()

# Gets link text and hyperlinks and gets it ready for the spreadsheet
def getJobs():
    links = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
    locations = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='text-location']")
    companies = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='company-name']")
    for link, location, company in zip(links, locations, companies):
        job_title.append(link.text)
        link_.append(link.get_attribute("href"))
        location_.append(location.text)
        company_.append(company.text)

# Puts extracted data into a spreadsheet and saves the file
def createSpreadsheet():
    df = pd.DataFrame({'Job Title': job_title, 'Company': company_, 'Location': location_, 'Link:': link_})
    df.to_csv(fileName, index=False)
    print(df)

# Code execution starts here
setupPage()
getJobs()
driver.quit()
createSpreadsheet()