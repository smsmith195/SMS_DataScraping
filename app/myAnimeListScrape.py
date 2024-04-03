# Import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd


# Adds the appropriate element from top_anime to the appropriate lists
def get_anime_data(driver):
    top_anime = driver.find_elements(By.CLASS_NAME, "ranking-list")
    anime_data = []
    for anime in top_anime:
        rank = anime.find_element(By.XPATH, "./td[1]").text
        title = anime.find_element(By.XPATH, "./td[2]/div[1]/div[2]/h3[1]").text
        score = anime.find_element(By.XPATH, "./td[3]").text
        anime_data.append({'Rank': rank, 'Title': title, 'Score': score})
    return anime_data


# This function makes use of Pandas to write the extracted data to a csv file
def create_spreadsheet(anime_data, file_name='top_anime_data.csv'):
    df = pd.DataFrame(anime_data)
    df.to_csv(file_name, index=False)
    print(df)


# Code execution
def main():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://myanimelist.net/topanime.php")
    driver.implicitly_wait(5)

    anime_data = get_anime_data(driver)

    driver.quit()

    create_spreadsheet(anime_data)


if __name__ == "__main__":
    main()
