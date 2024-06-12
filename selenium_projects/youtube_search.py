from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

video_title = input("Enter the video title to search : ")
youtuber = input("Enter the specific creator : ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#----taking user input----


driver.get("https://www.youtube.com/")

search_field = driver.find_element(By.NAME, "search_query")
search_field.send_keys(f"{video_title} by {youtuber}")
search_button = driver.find_element(By.ID, "search-icon-legacy")
search_button.click()

time.sleep(3)
first_video = driver.find_element(By.ID, 'video-title')
first_video.click()