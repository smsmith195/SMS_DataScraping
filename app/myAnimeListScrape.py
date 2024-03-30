# Import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Open Firefox and load 'Top Anime' page of MyAnimeList
driver = webdriver.Firefox()
driver.get("https://myanimelist.net/topanime.php")
driver.implicitly_wait(5)

# Where the data is being extracted from
top_anime = driver.find_elements(By.CLASS_NAME, "ranking-list")

# XPATH references for the data being extracted
rank_element = "./td[1]"
title_element = "./td[2]/div[1]/div[2]/h3[1]"
score_element = "./td[3]"

# Lists for containing the extracted data
rank = []
title = []
score = []

# Name of the file the data is being saved to
fileName = "top_anime_data.csv"

# getData adds the appropriate element from top_anime to the appropriate lists
def getData():
    for anime in top_anime:
        rank.append(anime.find_element(By.XPATH, rank_element).text)
        title.append(anime.find_element(By.XPATH, title_element).text)
        score.append(anime.find_element(By.XPATH, score_element).text)

# This function makes use of Pandas to write the extracted data to a csv file
def createSpreadhseet():
    df = pd.DataFrame({'Rank': rank, 'Title': title, 'Score': score})
    df.to_csv(fileName, index=False)
    print(df)

# Code execution starts here
getData()
driver.quit()
createSpreadhseet()
