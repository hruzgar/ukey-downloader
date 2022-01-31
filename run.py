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
		first_class = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "metro"))).find_element(By.TAG_NAME, "li").find_element(By.TAG_NAME, "a")		
	except:
		print("Please check you Internet connection!")
		driver.quit()

	first_class.click()
	time.sleep(1)
	download_for_current_class()
	time.sleep(1)
	driver.quit()
	
	
	
	






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

def download_for_current_class():
	driver.get("https://ukey.uludag.edu.tr/Ogrenci/DersMateryalleri")
	try:
		download_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "dosya")))		
	except:
		print("Please check you Internet connection!")
		driver.quit()
	for down_link in download_links:
		down_link.click()
		time.sleep(10)


if __name__ == "__main__":
	main()