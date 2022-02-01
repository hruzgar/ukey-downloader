import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
import time
import requests
import re
import sys
import os.path
import mimetypes

chromedriver_PATH = "chrome/cdriver/chromedriver.exe"
chrome_PATH = "chrome/App/Chrome-bin/chrome.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument('--incognito')
chrome_options.binary_location = chrome_PATH

session = requests.Session()


driver = webdriver.Chrome(executable_path=chromedriver_PATH, options=chrome_options, desired_capabilities=DesiredCapabilities.CHROME)
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
dest_folder = os.path.expandvars('%userprofile%/Downloads/ukey-download')
if not os.path.isdir(dest_folder):
	os.mkdir(dest_folder)


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

	print("Lütfen bekle! Birinci indirme 20 saniye sürüyor. Sonra hizlanacak\n")
	for link, name in class_links:
		# iterates through all the classes and downloads
		download_for_current_class(link, name)

	print("Süpeeer! Indime basarili!\nindirilen dosyalari 'Downloads' klasorunde bulabilirsiniz.\nHayirli calismalar ve iyi günler (:")
	
	
	
	



def log_in():
	# student_num = input("\n\nLütfen ögrenci numaranizi giriniz: ")
	# passw = input("Lütfen sifrenizi giriniz: ")
	print("\nGiris yapiliyor... (20 saniye sürüyor. Lütfen bekle)\n")
	driver.get("https://ukey.uludag.edu.tr")
	print("\nGiris yapildi!\n")
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
			diger = True
			td_list = tr.find_elements(By.TAG_NAME, "td")
			for td in td_list:
				if(td.text == "Haftalık Ders Notu"):
					diger = False

				if(td.text == "Dosyayı Aç"):
					class_n = [to_ascii(x) for x in name_of_class.split(" - ")]
					dest_dir = os.path.expandvars('%userprofile%/Downloads/ukey-download/' + "-".join(class_n[1].split(" ")))
					if not os.path.isdir(dest_dir):
						os.mkdir(dest_dir)

					link = td.find_element(By.TAG_NAME, "a").get_attribute("href")
					if diger == True:
						name_list = tr.text.split(" ")[:-4]
					else:
						name_list = tr.text.split(" ")[:-6]
						
					name_str = to_ascii("-".join(name_list))
					week_num = tr.text.split(" ")[-3]

					print("\nDownloading...\n" + week_num + "_" + class_n[0] + "_" + name_str)
					start = time.time()
					# Get Request
					r = session.get(link, allow_redirects=True, headers=headers)
					print("Get-Request elapsed time:", time.time() - start)
					
					content_type = r.headers['content-type']
					f_type = mimetypes.guess_extension(content_type)
					start = time.time()
					# writing to file
					with open(os.path.join(dest_dir, week_num + "_" + name_str + f_type), "wb") as file:
						for chunk in r.iter_content(chunk_size=128):
							file.write(chunk)
					print("Writing-File elapsed time:", time.time() - start, "\n\n\n")
					
					# print(week_num + "_" + name_of_class.split(" ")[0] + "_" + name_str, "\n", link,"\n\n\n")


	except:
		print("\n\nNo Download on this Page!\n")
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


def to_ascii(my_str):
	new_ascii = my_str.replace('\u0130', 'I').replace('\u0131', 'i')
	new_ascii = new_ascii.replace('\u011E', 'G').replace('\u011F', 'g')
	new_ascii = new_ascii.replace('\u015E', 'S').replace('\u015F', 's')
	new_ascii = new_ascii.replace('\u00C7', 'C').replace('\u00E7', 'c')
	new_ascii = new_ascii.replace('\u00DC', 'U').replace('\u00FC', 'u')
	new_ascii = new_ascii.replace('\u00D6', 'O').replace('\u00F6', 'o')
	new_ascii = new_ascii.replace('/', '_').replace('\\', '_')
	return new_ascii

if __name__ == "__main__":
	main()