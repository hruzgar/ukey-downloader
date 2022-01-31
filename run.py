from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\prog\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def main():
	log_in()
	try:
		dersler_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "metro")))
		
	except:
		driver.quit()
	dersler = dersler_div.find_elements(By.TAG_NAME, "li")
	for ders in dersler:
		print(ders.text)
	
	#dersler_div = driver.find_element(By.CLASS_NAME, "metro")
	






def log_in():
	driver.get("https://ukey.uludag.edu.tr")
	username = driver.find_element(By.ID, "KullaniciKodu")
	pw = driver.find_element(By.ID, "sifre")
	check_student = driver.find_element(By.XPATH, "//input[@value='Student']");
	username.send_keys("032190148")
	pw.send_keys("GuzSifre99")
	check_student.click()
	pw.send_keys(Keys.RETURN)
	# We should be inside Ukey on our Homepage right now


if __name__ == "__main__":
	main()