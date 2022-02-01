import selenium
import seleniumwire
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
extension_dict = {'application/msword': '.doc',
				'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',
				'application/vnd.openxmlformats-officedocument.wordprocessingml.template': '.dotx',
				'application/vnd.ms-word.document.macroEnabled.12': '.docm',
				'application/vnd.ms-word.template.macroEnabled.12': '.dotm',
				'application/vnd.ms-excel': '.xls',
				'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': '.xlsx',
				'application/vnd.openxmlformats-officedocument.spreadsheetml.template': '.xltx',
				'application/vnd.ms-excel.sheet.macroEnabled.12': '.xlsm',
				'application/vnd.ms-excel.template.macroEnabled.12': '.xltm',
				'application/vnd.ms-excel.addin.macroEnabled.12': '.xlam',
				'application/vnd.ms-excel.sheet.binary.macroEnabled.12': '.xlsb',
				'application/vnd.ms-powerpoint': '.ppt',
				'application/vnd.openxmlformats-officedocument.presentationml.presentation': '.pptx',
				'application/vnd.ms-powerpoint.addin.macroEnabled.12': '.ppam',
				'application/vnd.ms-powerpoint.presentation.macroEnabled.12': '.pptm',
				'application/vnd.ms-powerpoint.template.macroEnabled.12': '.potm',
				'application/vnd.ms-powerpoint.slideshow.macroEnabled.12': '.ppsm',
				'application/vnd.ms-access': '.mdb',
				'application/pdf':'.pdf'
				}

dest_folder = os.path.expandvars('%userprofile%/Downloads/ukey-download')
if not os.path.isdir(dest_folder):
	os.mkdir(dest_folder)


def main():
	start = time.time()
	driver = get_driver()
	log_in(driver)
	try:
		classes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "metro"))).find_elements(By.TAG_NAME, "li")		
	except:
		print("Please check you Internet connection!")
		driver.quit()
	
	get_cookies(driver)
	
	class_links = [];
	for my_class in classes:
		# finds all class links
		class_link = my_class.find_element(By.TAG_NAME, "a").get_attribute("href")
		class_name = my_class.find_element(By.TAG_NAME, "a").text
		class_links.append((class_link, class_name))

	print("Birinci indirme 20 saniye sürüyor. Sonra hizlanacak\n")
	session = requests.Session()
	for link, name in class_links:
		# iterates through all the classes and downloads
		download_for_current_class(link, name)

	print("Indirme Süresi:", str(time.time() - start) + "s")
	print("\n\nSüpeeer! Indirme basarili!\nindirilen dosyalari 'Downloads' klasöründe bulabilirsin.\n\n\nHayirli calismalar ve iyi günler dilerim (:")
	
	
	
	
def get_driver():
	# Path to chrome and chromedriver
	chromedriver_PATH = "chrome/cdriver/chromedriver.exe"
	chrome_PATH = "chrome/App/Chrome-bin/chrome.exe"

	# chrome settings for selenium
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--ignore-ssl-errors')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-software-rasterizer')
	chrome_options.add_argument('--incognito')
	chrome_options.binary_location = chrome_PATH

	return webdriver.Chrome(executable_path=chromedriver_PATH, options=chrome_options, desired_capabilities=DesiredCapabilities.CHROME)

def log_in(driver):
	# get Student-Number and Password as Input
	student_num = input("\n\nLütfen ögrenci numaranizi giriniz: ")
	passw = input("Lütfen sifrenizi giriniz: ")

	print("\nGiris yapiliyor... (20 saniye sürüyor. Lütfen bekle)\n\nTüm indirme yaklasik olarak 5 dakika sürecek. Git kendine bir kahve yap (;\n")
	driver.get("https://ukey.uludag.edu.tr")
	print("\nGiris yapildi!\n")

	username = driver.find_element(By.ID, "KullaniciKodu")
	pw = driver.find_element(By.ID, "sifre")
	check_student = driver.find_element(By.XPATH, "//input[@value='Student']");
	
	username.send_keys(student_num)
	pw.send_keys(passw)
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
					
					# Get Request
					start = time.time()
					r = session.get(link, allow_redirects=True, headers=headers)
					print("Get-Request elapsed time:", str(time.time() - start) + "s")
					
					# gets file extension (for example:".pdf")
					content_type = r.headers['content-type']
					f_type = extension_dict[content_type]
					print(f_type)
					
					# writing to file
					start = time.time()
					with open(os.path.join(dest_dir, week_num + "_" + name_str + f_type), "wb") as file:
						for chunk in r.iter_content(chunk_size=128):
							file.write(chunk)
					print("Writing-File elapsed time:", str(time.time() - start) + "s", "\n\n\n")


	except:
		print("\n\nNo Download on this Page!\n")
		# driver.quit()
	
		# time.sleep(3)
	driver.back()
	driver.back()

def get_cookies(driver):
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