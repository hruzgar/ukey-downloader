## Bu dosyay覺 ba??ka dillerde de okuyabilirsin:
<a href="README.tr.md"><img src="https://img.shields.io/badge/-T%C3%9CRK%C3%87E-red?style=for-the-badge"></a>
<a href="README.md"><img src="https://img.shields.io/badge/-ENGLISH-red?style=for-the-badge"></a>

## ??妝 ukey-downloader

ukey-downloader UKEY hesab覺ndaki t羹m ders i癟eriklerini tek t覺kla indirmeni sa??lar.

D繹nemin sonuna geldin ve ders notlar覺n覺, slaytlar覺 indirmek mi istiyorsun? Biz istiyorduk ve her bir dersin her bir i癟eri??ine teker teker t覺klayarak indiriyor, dosyalar覺 yeniden isimlendiriyor ve klas繹rlere yerle??tiriyorduk. Ama art覺k gerek yok! ??羹nk羹 ukey-downloader yard覺m覺n覺za yeti??ti.

## ??? ??zellikler
 - UKEY hesab覺n覺zdaki t羹m ders notlar覺n覺 ve slaytlar覺 indirir
 - Dersler i癟in otomatik olarak klas繹r olu??turur ve dosyalar覺 yerle??tirir
 - Dosyalar覺 ASCII karakter setini kullanarak yeniden isimlendirir ve ba??lar覺na hafta numaras覺n覺 ekler

## ???????領?????? Nas覺l Kullan覺l覺r

### Windows

1. En g羹ncel s羹r羹m羹 indir (bir zip dosyas覺 olacak)
2. Zip ar??ivini 癟覺kart
3. run.exe dosyas覺na 癟ift t覺kla
4. ????renci numaran覺 ve ??ifreni gir
5. 襤ndirme i??lemi 5 ila 10 dakika aras覺nda de??i??ebilir, beklerken 癟ay kahve al

Her ??ey bu kadar! Tad覺n覺 癟覺kart

Herhangi bir Python paketi kurmana gerek yok 癟羹nk羹 t羹m gereksinimler tek bir 癟al覺??t覺r覺labilir dosyada topland覺!. Hatta Python interpreter'覺n覺 kurmu?? olmana bile gerek yok. ??al覺??an bir Windows makine yeterli olacakt覺r!

### GNU/Linux

1. Repository'i lokaline klonla ```git clone https://github.com/hruzgar/ukey-downloader.git```
2. selenium gereksinimini ```pip install selenium``` komutunu 癟al覺??t覺rarak 癟繹z羹mle
3. [ChromeDriver](https://chromedriver.chromium.org/downloads) 癟al覺??t覺r覺labilir dosyas覺n覺 indir ve /usr/bin klas繹r羹ne yerle??tir
> ??nemli Uyar覺: Maj繹r s羹r羹m羹 98 olan ChromeDriver paketinin ??ifrelerdeki 繹zel karakterler ile sorun 癟覺kartmas覺ndan 繹t羹r羹 kullan覺lmamas覺 gerekmektedir. ChromeDriver v97 ile Chromium v98 test edilmi?? ve 癟al覺??t覺??覺 onaylanm覺??t覺r
4. Scripti ```python3 run.py``` komutu ile 癟al覺??t覺r
5. ????renci numaran覺 ve ??ifreni gir
6. 襤ndirme i??lemi 5 ila 10 dakika aras覺nda de??i??ebilir, beklerken [UngoogledChromium'u](https://github.com/Eloston/ungoogled-chromium) kaynak kodundan derle

## ???? Kullan覺lan Python K羹t羹phaneleri
 - selenium (Web istemcisini sim羹le eder)
 - pyinstaller (Python interpreter'覺n覺 ve t羹m gereksinimleri i癟inde bar覺nd覺ran bir Windows 癟al覺??t覺r覺labilir dosyas覺 olu??turur)

## ???????? Katk覺da Bulunmak

Katk覺lar覺n覺za a癟覺??覺z ve takdir ederiz. Biraz Python bilginiz varsa, Selenium Framework hakk覺nda video izleyebilir ve projenin geli??tirilmesine yard覺mc覺 olabilirsiniz. Te??ekk羹rler!

 - ukey-downloader'覺n v1-v1.2 aras覺nda kulland覺??覺 README dosyas覺n覺n 癟evirisini yapt覺??覺 i癟in [Sabir S羹leymanl覺'ya](https://www.linkedin.com/in/sabirs/) te??ekk羹r ederiz.
