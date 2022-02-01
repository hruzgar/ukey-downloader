#using vscode-env envoirement
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver
import time
import requests
import re

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

PATH = "C:\\prog\\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
class_links = [];

def main():
	log_in()
	try:
		classes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "metro"))).find_elements(By.TAG_NAME, "li")		
	except:
		print("Please check you Internet connection!")
		driver.quit()

	for request in driver.requests:
		if(request.url == "https://ukey.uludag.edu.tr/Images/ukeyuser.jpg"):
  			print(request.url) # <--------------- Request url
  			print(request.headers) #


	for my_class in classes:
		class_link = my_class.find_element(By.TAG_NAME, "a").get_attribute("href")
		class_links.append(class_link)
	for link in class_links:
		download_for_current_class(link)
	print(class_links)
	
	
	
	






def log_in():
	driver.get("https://ukey.uludag.edu.tr")
	username = driver.find_element(By.ID, "KullaniciKodu")
	pw = driver.find_element(By.ID, "sifre")
	check_student = driver.find_element(By.XPATH, "//input[@value='Student']");
	username.send_keys("032190148")
	pw.send_keys("GuzSifre99")
	check_student.click()
	pw.send_keys(Keys.RETURN)
	# We should be on the Ukey Homepage now

def download_for_current_class(link_of_class): 
	driver.get(link_of_class)
	driver.get("https://ukey.uludag.edu.tr/Ogrenci/DersMateryalleri")
	try:
		download_links = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "dosya")))
		for down_link in download_links:
			link = down_link.get_attribute("href")
			print(link)
			#for request in driver.requests:
			#	if(request.url == "https://ukey.uludag.edu.tr/Ogrenci/DersMateryalleri"):
  			#		print(request.url) # <--------------- Request url
  			#		print(request.headers) #
			# r = requests.get(link, allow_redirects=True)
			# print(r)
			# filename = getFilename_fromCd(r.headers.get('content-disposition'))
			# print(filename)
			# down_link.click()		
	except:
		print("No Download on this Page!")
		# driver.quit()
	
		# time.sleep(3)
	driver.back()
	driver.back()

def getFilename_fromCd(cd):
	"""
	Get filename from content-disposition
	"""
	if not cd:
		return None
	fname = re.findall('filename=(.+)', cd)
	if len(fname) == 0:
		return None
	return fname[0]

if __name__ == "__main__":
	main()