## You can read this file in other languages:
<a href="README.tr.md"><img src="https://img.shields.io/badge/-T%C3%9CRK%C3%87E-red?style=for-the-badge"></a>
<a href="README.md"><img src="https://img.shields.io/badge/-ENGLISH-red?style=for-the-badge"></a>

## 🧩 ukey-downloader

ukey-downloader lets you download all available course materials from your UKEY account with the push of a button.

The semester has finished and you want to download all the lecture notes and slides? Normally you would click each and every download link, categorize and rename the files manually. Well, not anymore. These days are now over thanks to ukey-downloader!

## ✨ Features
- Downloads all the lecture-notes and slides available to access in your UKEY account
- Automatically creates folders for courses, and places the files
- Renames files using ASCII-supported characters and appends week number

## 🧑🏻‍💻 How to use

### Windows

1. Download the latest release (a zip file will be provided)
2. Extract the zip file
3. Double click on run.exe
4. Enter you student number and password
5. The downloading process may take between 5 to 10 minutes, grab a tea or coffee while you wait

That's all! Enjoy

You don't need to install any Python packages, all dependencies are packed into one executable! You don't even need the Python interpreter installed. Just a working Windows machine will get you going!

### GNU/Linux

1. Download and install [python](https://www.python.org/) if you haven't already (preferably v3.9)
2. Resolve dependency selenium by running command ```pip install selenium```
3. Download and install chrome (google-chrome or chromium)(preferably v97)
4. Download and place [ChromeDriver](https://chromedriver.chromium.org/downloads) executable to /usr/bin
> Important Warning: Do not use ChromeDriver major version 98 as it has issues regarding special characters. Use of v97 with Chromium v98 is tested 
5. Clone the repository to your local with 
```bash
git clone https://github.com/hruzgar/ukey-downloader.git
```
6. Install ukey-downloader by running the installer script with ```./install.sh```
7. You should be able to find ukeydl on your applications-list now. If you are not using any window manager just run ukeydl which you can find at /usr/local/bin/ukeydl


## 🐍 Dependencies for developing
- selenium (simulates a web client)
- pyinstaller (creates the Windows executable which includes Python interpreter and all the dependencies)

## 🤝🏻 Contributing
Contributions are welcome and will be much appreciated. If you know some Python you could watch some videos about the Selenium Framework and help improving the project. Thank you!
