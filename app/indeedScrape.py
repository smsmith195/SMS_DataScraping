from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Gets user input and returns the value
def get_user_input():
    job_title = input("What is the job title that you are looking for? ")
    job_location = input("Where are you looking for work? ")
    return job_title, job_location

# Takes the user input and conducts the search
def setup_page(driver, job_name, job_location):
    job_search_field = driver.find_element(By.ID, "text-input-what")
    job_search_field.send_keys(job_name)
    job_location_field = driver.find_element(By.ID, "text-input-where")
    job_location_field.send_keys(job_location)
    submit_button = driver.find_element(By.XPATH, "//*[@id='jobsearch']/div/div[2]/button")
    submit_button.click()

# Gets the data returned by the search results and creates the data to be returned in the spreadsheet
def extract_job_data(driver):
    job_title_elements = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
    location_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='text-location']")
    company_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='company-name']")

    job_data = []
    for title_element, location_element, company_element in zip(job_title_elements, location_elements,
                                                                company_elements):
        job_data.append({
            'Job Title': title_element.text,
            'Location': location_element.text,
            'Company': company_element.text,
            'Link': title_element.get_attribute("href")
        })
    return job_data

# Takes in the data from extractJobData and creates a spreadsheet using Pandas
def create_spreadsheet(job_data, file_name='job_list.csv'):
    df = pd.DataFrame(job_data)
    df.to_csv(file_name, index=False)
    print(df)

# Code execution
def main():
    job_name, job_location = get_user_input()
    driver = webdriver.Firefox()
    driver.get("https://uk.indeed.com/")

    setup_page(driver, job_name, job_location)
    job_data = extract_job_data(driver)

    driver.quit()

    create_spreadsheet(job_data)


if __name__ == "__main__":
    main()
