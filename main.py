from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")


email =driver.find_element(By.NAME, value="session_key")
email.send_keys("xxxxxxxxx")
email.send_keys(Keys.ENTER)


password = driver.find_element(By.NAME,value="session_password")
password.send_keys("xxxxxxxx")
password.send_keys(Keys.ENTER)

time.sleep(10)

offre_emploi = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
offre_emploi.click()


time.sleep(3)


delete_message_input = driver.find_element(By.XPATH, value='//*[@id="recentSearchesIndex__0"]')
delete_message_input.click()

time.sleep(3)

post1 = driver.find_element(By.CSS_SELECTOR, value='.jobs-apply-button--top-card button')
post1.click()

time.sleep(3)

apply = driver.find_element(By.CSS_SELECTOR, value='.justify-flex-end button')
apply.click()
