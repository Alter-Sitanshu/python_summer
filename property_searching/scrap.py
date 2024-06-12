from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSd6Vp_p4pKCNECxlBCuOeYvYOAP0olPixeZV7r6bviy7JbqMA/viewform?usp=sf_link"
driver = None
def prices(pricetag_list: list[str]) -> list[int]:
    price_list = []
    for tags in pricetag_list:
        numstr = ""
        for char in tags.text:
            if char.isdigit():
                numstr += char
        price_list.append(int(numstr))
    return price_list

def formFiller(address: str, price: int, link: str) -> None:
    time.sleep(0.25)
    addr = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    pri = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    lin = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    addr.send_keys(address)
    pri.send_keys(price)
    lin.send_keys(link)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(0.25)
    another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()
    
def openForm() -> None:
    global driver
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(FORM_LINK)

def closeForm() -> None:
    global driver
    driver.quit()
