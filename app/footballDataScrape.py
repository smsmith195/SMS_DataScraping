from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import pandas as pd


# Prompts user to select which country they wish to get the data from before launching Selenium
def get_user_input():
    country_choice = input("Choose a Country, this is case-sensitive: ")
    league_choice = input("Choose a League. This is also case-sensitive: ")
    return country_choice, league_choice


# Set up page for extracting data, using country entered by the user. If the country is invalid, stop the application
def set_up_page(driver, country_choice, league_choice):
    driver.get("https://www.adamchoi.co.uk/overs/detailed")
    driver.implicitly_wait(5)
    all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
    all_matches_button.click()
    try:
        country_dropdown_select(driver, country_choice)
        league_dropdown_select(driver, league_choice)
    except:
        close_on_fail(driver)


# Selects country chosen by the user
def country_dropdown_select(driver, country_choice):
    c_dropdown = Select(driver.find_element(By.ID, "country"))
    c_dropdown.select_by_visible_text(country_choice)


# Selects league chosen by user
def league_dropdown_select(driver, league_choice):
    l_dropdown = Select(driver.find_element(By.ID, "league"))
    l_dropdown.select_by_visible_text(league_choice)


# Closes down application if selections are invalid
def close_on_fail(driver):
    print("Invalid selection, closing program down")
    driver.quit()
    quit()


# Gets the table on the page and extracts data
def get_match_data(driver):
    matches = driver.find_elements(By.TAG_NAME, "tr")
    match_data = []
    for match in matches:
        date = match.find_element(By.XPATH, "./td[1]").text
        home_team = match.find_element(By.XPATH, "./td[2]").text
        score = match.find_element(By.XPATH, "./td[3]").text
        away_team = match.find_element(By.XPATH, "./td[4]").text
        match_data.append({'Date': date, 'Home Team': home_team, 'Score': score, 'Away Team': away_team})
    return match_data


# This function makes use of Pandas to write the extracted data to a csv file
def create_spreadsheet(match_data, file_name='football_data.csv'):
    df = pd.DataFrame(match_data)
    df.to_csv(file_name, index=False)
    print(df)


# Code execution starts here
def main():
    country_choice, league_choice = get_user_input()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    set_up_page(driver, country_choice, league_choice)
    match_data = get_match_data(driver)
    driver.quit()
    create_spreadsheet(match_data)


if __name__ == "__main__":
    main()
