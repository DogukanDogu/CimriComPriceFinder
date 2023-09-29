from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cimri.com")
time.sleep(2)

page_title = driver.find_element(By.CLASS_NAME,"WidgetBlock_title__zjHOg")

prices = driver.find_element((By.CLASS_NAME,"swiper-container swiper-container-initialized swiper-container-horizontal swiper-container-pointer-events ProductCardSlider_productCardSlider__NFlVR"))



print(page_title.text)
print(prices.text)

