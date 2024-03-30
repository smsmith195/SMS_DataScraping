from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get("https://myanimelist.net/topanime.php")

time.sleep(3)

top_anime = driver.find_elements(By.CLASS_NAME, "ranking-list")

rank = []
anime_title = []
score = []


for anime in top_anime:
    rank.append(anime.find_element(By.XPATH, "./td[1]").text)
    anime_title.append(anime.find_element(By.XPATH, "./td[2]/div[1]/div[2]/h3[1]").text)
    score.append(anime.find_element(By.XPATH, "./td[3]").text)

driver.quit()

df = pd.DataFrame({'rank': rank, 'anime_title': anime_title, 'score': score})
df.to_csv('top_anime_data.csv', index=False)
print(df)