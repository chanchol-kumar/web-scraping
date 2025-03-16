from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.daraz.com.bd/mens-eyeglasses/")

driver.maximize_window()

text = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a").text
print(f"text: ",text)

link = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a").get_attribute("href")
print(f"link: ",link)

text_list = []
for i in range(1,41):
    j = str(i)
    text = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div["+j+"]/div/div/div[2]/div[2]/a").text
    text_list.append(text)

print(f"text_list: ",text_list)
time.sleep(5)

driver.quit()
