from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import requests
import getpass
import sys
import os.path

extension_dict = {
    'application/msword': '.doc',
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
    'application/pdf': '.pdf'
}

# Set platform-specific global variables
destination_folder = ''


def get_driver():
    # Sets the path to chrome and chromedriver executables
    if sys.platform == "win32":
        chromedriver_service = Service("chrome/cdriver/chromedriver.exe")
        path_chrome = "chrome/App/Chrome-bin/chrome.exe"
    elif sys.platform == "linux":
        chromedriver_service = Service("/usr/bin/chromedriver")
        if os.path.exists("/usr/bin/google-chrome"):
            path_chrome = "/usr/bin/google-chrome"
        elif os.path.exists("/usr/bin/chromium"):
            path_chrome = "/usr/bin/chromium"
        else:
            path_chrome = input('''ukeydl Chrome kurulumunu bulamadı. 
            Lütfen chrome çalıştırılabilir dosyasının tam konumunu giriniz: ''')
            if not os.path.exists(path_chrome):
                print("böyle bir dosya yok ki :(")
                sys.exit()

    # chrome settings for selenium
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # if activated browser is not shown to the end-user
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--incognito')
    chrome_options.binary_location = path_chrome

    return webdriver.Chrome(service=chromedriver_service, options=chrome_options,
                            desired_capabilities=DesiredCapabilities.CHROME)


def log_in(driver):
    student_num = input('[ukey-login]: Lütfen öğrenci numaranızı giriniz: ')
    passw = getpass.getpass('[ukey-login]: Lütfen şifrenizi giriniz: ')

    print('[ukey-login]: Giriş yapılıyor')

    username = driver.find_element(By.ID, "KullaniciKodu")
    pw = driver.find_element(By.ID, "sifre")
    check_student = driver.find_element(By.XPATH, "//input[@value='Student']")

    username.clear()
    pw.clear()

    username.send_keys(student_num)
    pw.send_keys(passw)
    check_student.click()
    pw.send_keys(Keys.RETURN)
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "metro"))).find_elements(
            By.TAG_NAME, "li")
        return True  # We should be on the Ukey Homepage now
    except:
        return False


def get_cookies(driver, session):
    time.sleep(0.5)
    cookies = driver.get_cookies()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])


def to_ascii(my_str):
    new_ascii = my_str.replace('\u0130', 'I').replace('\u0131', 'i')
    new_ascii = new_ascii.replace('\u011E', 'G').replace('\u011F', 'g')
    new_ascii = new_ascii.replace('\u015E', 'S').replace('\u015F', 's')
    new_ascii = new_ascii.replace('\u00C7', 'C').replace('\u00E7', 'c')
    new_ascii = new_ascii.replace('\u00DC', 'U').replace('\u00FC', 'u')
    new_ascii = new_ascii.replace('\u00D6', 'O').replace('\u00F6', 'o')
    new_ascii = new_ascii.replace('/', '_').replace('\\', '_')
    new_ascii = new_ascii.replace(':', '_').replace('?', '_')
    new_ascii = new_ascii.replace('<', '_').replace('>', '_')
    new_ascii = new_ascii.replace('!', '_').replace('*', '_')
    new_ascii = new_ascii.replace('|', '_')
    return new_ascii


def get_time_dif(start):
    elapsed_time = str(time.time() - start)
    seconds = elapsed_time.split(".")[0]
    mili_seconds = elapsed_time.split(".")[1][:3]
    return seconds + "." + mili_seconds + "s"


def download_for_current_class(driver, session, link_of_class, name_of_class):
    driver.get(link_of_class)
    driver.get("https://ukey.uludag.edu.tr/Ogrenci/DersMateryalleri")

    try:
        tr_list = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, "tbody"))).find_elements(By.TAG_NAME, "tr")
        
        # Creates directory for specified class
        class_n = [to_ascii(x) for x in name_of_class.split(" - ")]
        dest_dir = destination_folder + "-".join(class_n[1].split(" "))
        if not os.path.isdir(dest_dir):
            os.mkdir(dest_dir)

        for i in range(2, len(tr_list) + 1):
            td = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[7]")
            if td.text == "Dosyayı Aç":
                link = td.find_element(By.TAG_NAME, "a").get_attribute("href")
                week_num = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[4]").text
                name_str = driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[2]").text
                print('[download]: İndirilen dosya: ' + week_num + "_" + class_n[0] + "_" + name_str)

                # Get Request
                start = time.time()
                r = session.get(link, allow_redirects=True)
                print(f'[download]: GET isteği için geçen süre: {get_time_dif(start)}')
                
                try:
                    # gets file extension (for example:".pdf")
                    content_type = r.headers['content-type']
                    f_type = extension_dict[content_type]
                    print(f'[download]: Dosya uzantısı: {f_type}')
                    # writing to file
                    start = time.time()
                    with open(os.path.join(dest_dir, week_num + "_" + name_str + f_type), "wb") as file:
                        for chunk in r.iter_content(chunk_size=128):
                            file.write(chunk)
                    print(f'[download]: Dosya kaydı için geçen süre: {get_time_dif(start)}\n\n')
                except:
                    print("\nDosya Uzantisi desteklenmiyor veya site hata veriyor!\n")

    except:
        print('[download]: Bu sayfada indirilebilir içerik bulunamadı!')

    driver.back()
    driver.back()


def msg(message):
    print(f'[ukeydl]: {message}')


def main():
    start = time.time()

    # starts driver (selenium) and requests-session (for downloads)
    driver = get_driver()
    session = requests.Session()

    msg('Chrome başlatılıyor')
    driver.get('https://ukey.uludag.edu.tr')

    password_true = log_in(driver)
    while not password_true:
        msg('Öğrenci numarası veya şifre hatalı. Lütfen tekrar deneyin.')
        password_true = log_in(driver)

    msg("UKEY'e giriş başarılı!")

    get_cookies(driver, session)

    classes = driver.find_element(By.CLASS_NAME, "metro").find_elements(By.TAG_NAME, "li")
    class_links = []
    for my_class in classes:
        # finds all class links
        class_link = my_class.find_element(By.TAG_NAME, "a").get_attribute("href")
        class_name = my_class.find_element(By.TAG_NAME, "a").text
        class_links.append((class_link, class_name))

    msg('İlk indirme işlemi biraz vakit alabilir, işlem zamanla hızlanacaktır.')

    global destination_folder
    if sys.platform == "win32":
        destination_folder = os.path.expandvars('%userprofile%/Downloads/ukey-download/')
    elif sys.platform == "linux":
        destination_folder = os.path.expandvars('$HOME/Downloads/ukey-download/')
    else:
        destination_folder = input('''ukeydl işletim sistemini desteklemiyor.
        ancak yine de indirme işlemini deneyebilirsin.
        ders klasörlerinin yerleştirileceği klasörü belirt: ''')

    if not os.path.isdir(destination_folder):
        os.mkdir(destination_folder)

    for link, name in class_links:
        # iterates through all the classes and downloads
        download_for_current_class(driver, session, link, name)

    driver.quit()
    msg(f"UKEY'de bulunan tüm dersler indirildi! İndirme klasörü: {destination_folder}")
    msg(f"İndirme işlemi {get_time_dif(start)} saniyede tamamlandı.")
    print(f'ukeydl\'i kullandığın için teşekkür ederiz!')
    time.sleep(15)


if __name__ == "__main__":
    main()
