import requests
import re


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


url = "https://ukey.uludag.edu.tr/p!IFNGXVYrBX4sVl06FFVWXzAxXltbUDMKBllbQFxeQngmWEwfWVd7ICJSUwAMIFwacFNech8CW1R1blMCAgVsBSZSAlEAUQUGJQAAHw!/"
headers = {"Cookie":"BIGipServerukey.app~ukey_pool=687936684.20480.0000; _KEY_Rses=41b2140402ae44f2b370d50aa38b76a2; _KEY_Proxy=A0249E87B28B2691DC1775A7E6549065A58903FE",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Host":"ukey.uludag.edu.tr"}


# url="https://speed.hetzner.de/100MB.bin"
r = requests.get(url, headers=headers, allow_redirects=True)
# filename = getFilename_fromCd(r.headers.get('content-disposition'))
with open("test3.ppt", "wb") as f:
	for chunk in r.iter_content(chunk_size=128):
		f.write(chunk)
print(filename)
