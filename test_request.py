import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
import requests
import re
import time


chromedriver_PATH = "chrome/cdriver/chromedriver.exe"
chrome_PATH = "chrome/App/Chrome-bin/chrome.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.binary_location = chrome_PATH

session = requests.Session()


driver = webdriver.Chrome(executable_path=chromedriver_PATH, options=chrome_options, desired_capabilities=DesiredCapabilities.CHROME)

url = "https://stackoverflow.com/questions/32817962/selenium-not-starting-portable-chrome-but-local-installation"
headers = {"Cookie":"BIGipServerukey.app~ukey_pool=553718956.20480.0000; _ga=GA1.3.1998165752.1643706547; _gid=GA1.3.1230881967.1643706547; _gat=1; _KEY_Rses=89596ccd64764a5abe01c90ca67fd494; _KEY_Proxy=F477D79A0AC5F83FD742C8C03BB4B0B435C18D88",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Host":"ukey.uludag.edu.tr"}


# url="https://speed.hetzner.de/100MB.bin"
r = driver.get("https://ukey.uludag.edu.tr/Home?ReturnUrl=%2f")
time.sleep(5)
# filename = getFilename_fromCd(r.headers.get('content-disposition'))
"""
with open("test3.ppt", "wb") as f:
	for chunk in r.iter_content(chunk_size=128):
		f.write(chunk)
print(filename)
"""
print(r.text)