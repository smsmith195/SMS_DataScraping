from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

# Prompts user to select which country they wish to get the data from before launching Selenium
countryChoice = input("Choose a Country, this is case-sensitive: ")
print(countryChoice)

# Opens Firefox on the Adam Choi website
driver = webdriver.Firefox()
driver.get("https://www.adamchoi.co.uk/overs/detailed")
driver.implicitly_wait(5)

# Create variables for page setup
all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
dropdown = Select(driver.find_element(By.ID, "country"))

# XPATH references for table columns
date_element = "./td[1]"
home_element = "./td[2]"
score_element = "./td[3]"
away_element = "./td[4]"

# Lists for containing the extracted data
date = []
home_team = []
score = []
away_team = []

# Name of the file the data is being saved to
fileName = "football_data.csv"

# Set up page for extracting data, using country entered by the user. If the country is invalid, stop the application
def setUpPage():
    all_matches_button.click()
    try:
        dropdown.select_by_visible_text(countryChoice)
    except:
        print("Invalid country choice, closing program down")
        driver.quit()
        quit()

# Gets the table on the page and extracts data
def getMatchData():
    matches = driver.find_elements(By.TAG_NAME, "tr")

    for match in matches:
        date.append(match.find_element(By.XPATH, date_element).text)
        home_team.append(match.find_element(By.XPATH, home_element).text)
        score.append(match.find_element(By.XPATH, score_element).text)
        away_team.append(match.find_element(By.XPATH, away_element).text)

# This function makes use of Pandas to write the extracted data to a csv file
def createSpreadsheet():
    df = pd.DataFrame({'Date': date, 'Home Team': home_team, 'Score': score, 'Away Team': away_team})
    df.to_csv(fileName, index=False)
    print(df)

# Code execution starts here
setUpPage()
getMatchData()
driver.quit()
createSpreadsheet()
