from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=Chrome_options)

driver.get("https://www.speedtest.net/tr")

start_button = driver.find_element(By.CLASS_NAME, "start-text")
start_button.click()
while True:
    time.sleep(10)
    try:
        download_speed = driver.find_element(By.CLASS_NAME, "download-speed")
        upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed")
        
        if download_speed.text != "—" and upload_speed.text != "—":
            print(f"Your Download speed is: {download_speed.text}\nYour Upload Speed is: {upload_speed.text}")
        else:
            raise NoSuchElementException
    except NoSuchElementException:
        continue
    else:
        break
driver.quit()