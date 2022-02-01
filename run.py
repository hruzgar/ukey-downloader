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
import sys

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-software-rasterizer')

session = requests.Session()

PATH = "C:\\prog\\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
class_links = [];
headers = {"Host":"ukey.uludag.edu.tr",
	"Connection":"keep-alive",
	"Cache-Control":"max-age=0",
	"sec-ch-ua":'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
	"sec-ch-ua-platform":'"Windows"',
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Sec-Fetch-Site":"same-origin",
	"Sec-Fetch-Mode":"navigate",
	"Sec-Fetch-User":"?1",
	"Sec-Fetch-Dest":"document",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language": "de-DE,de;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6,en;q=0.5"
	}

def main():
	log_in()
	try:
		classes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "metro"))).find_elements(By.TAG_NAME, "li")		
	except:
		print("Please check you Internet connection!")
		driver.quit()
	
	get_cookies()
	
	for my_class in classes:
		# finds all class links
		class_link = my_class.find_element(By.TAG_NAME, "a").get_attribute("href")
		class_name = my_class.find_element(By.TAG_NAME, "a").text
		class_links.append((class_link, class_name))

	print(class_links)

	for link, name in class_links:
		# iterates through all the classes and downloads
		download_for_current_class(link, name)
	
	
	
	



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

def download_for_current_class(link_of_class, name_of_class): 
	driver.get(link_of_class)
	driver.get("https://ukey.uludag.edu.tr/Ogrenci/DersMateryalleri")
	try:
		tr_list = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, "tbody"))).find_elements(By.TAG_NAME, "tr")
		for tr in tr_list:
			td_list = tr.find_elements(By.TAG_NAME, "td")
			for td in td_list:
				if(td.text == "Dosyayı Aç"):
					link = td.find_element(By.TAG_NAME, "a").get_attribute("href")

					name_list = tr.text.split(" ")[:-4]
					name_str = "-".join(name_list)
					
					week_num = tr.text.split(" ")[-3]
					
					print(week_num + "_" + name_of_class.split(" ")[0] + "_" + name_str, "\n", link,"\n\n\n")


		"""
		download_links = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "dosya")))
		for i, down_link in enumerate(download_links):
			link = down_link.get_attribute("href")
			print("\nDownloading:", link)

			start = time.time()
			# Get Request
			r = session.get(link, allow_redirects=True, headers=headers)
			print("Get-Request elapsed time:", time.time() - start)
			
			start = time.time()
			# writing to file
			with open(str(i) + "_" + name_of_class.split(" ")[0] + ".txt", "wb") as file:
				for chunk in r.iter_content(chunk_size=128):
					file.write(chunk)
			print("Writing-File elapsed time:", time.time() - start, "\n")

			time.sleep(1)	
		"""
	except:
		print("No Download on this Page!")
		# driver.quit()
	
		# time.sleep(3)
	driver.back()
	driver.back()

def get_cookies():
	time.sleep(0.5)
	for request in driver.requests:
		if request.url == "https://ukey.uludag.edu.tr/Images/ukeyuser.jpg":
			headers["Cookie"] = request.headers["Cookie"]
			print("\nusing Cookies:",request.headers["Cookie"], "\n\n\n") 

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