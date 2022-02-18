## Bu dosyayı başka dillerde de okuyabilirsin:
<a href="README.tr.md"><img src="https://img.shields.io/badge/-T%C3%9CRK%C3%87E-red?style=for-the-badge"></a>
<a href="README.md"><img src="https://img.shields.io/badge/-ENGLISH-red?style=for-the-badge"></a>

## 🧩 ukey-downloader

ukey-downloader UKEY hesabındaki tüm ders içeriklerini tek tıkla indirmeni sağlar.

Dönemin sonuna geldin ve ders notlarını, slaytları indirmek mi istiyorsun? Biz istiyorduk ve her bir dersin her bir içeriğine teker teker tıklayarak indiriyor, dosyaları yeniden isimlendiriyor ve klasörlere yerleştiriyorduk. Ama artık gerek yok! Çünkü ukey-downloader yardımınıza yetişti.

## ✨ Özellikler
 - UKEY hesabınızdaki tüm ders notlarını ve slaytları indirir
 - Dersler için otomatik olarak klasör oluşturur ve dosyaları yerleştirir
 - Dosyaları ASCII karakter setini kullanarak yeniden isimlendirir ve başlarına hafta numarasını ekler

## 🧑🏻‍💻 Nasıl Kullanılır

### Windows

1. En güncel sürümü indir (bir zip dosyası olacak)
2. Zip arşivini çıkart
3. run.exe dosyasına çift tıkla
4. Öğrenci numaranı ve şifreni gir
5. İndirme işlemi 5 ila 10 dakika arasında değişebilir, beklerken çay kahve al

Her şey bu kadar! Tadını çıkart

Herhangi bir Python paketi kurmana gerek yok çünkü tüm gereksinimler tek bir çalıştırılabilir dosyada toplandı!. Hatta Python interpreter'ını kurmuş olmana bile gerek yok. Çalışan bir Windows makine yeterli olacaktır!

### GNU/Linux

1. Repository'i lokaline klonla ```git clone https://github.com/hruzgar/ukey-downloader.git```
2. selenium gereksinimini ```pip install selenium``` komutunu çalıştırarak çözümle
3. [ChromeDriver](https://chromedriver.chromium.org/downloads) çalıştırılabilir dosyasını indir ve /usr/bin klasörüne yerleştir
> Önemli Uyarı: Majör sürümü 98 olan ChromeDriver paketinin şifrelerdeki özel karakterler ile sorun çıkartmasından ötürü kullanılmaması gerekmektedir. ChromeDriver v97 ile Chromium v98 test edilmiş ve çalıştığı onaylanmıştır
4. Scripti ```python3 run.py``` komutu ile çalıştır
5. Öğrenci numaranı ve şifreni gir
6. İndirme işlemi 5 ila 10 dakika arasında değişebilir, beklerken [UngoogledChromium'u](https://github.com/Eloston/ungoogled-chromium) kaynak kodundan derle

## 🐍 Kullanılan Python Kütüphaneleri
 - selenium (Web istemcisini simüle eder)
 - pyinstaller (Python interpreter'ını ve tüm gereksinimleri içinde barındıran bir Windows çalıştırılabilir dosyası oluşturur)

## 🤝🏻 Katkıda Bulunmak

Katkılarınıza açığız ve takdir ederiz. Biraz Python bilginiz varsa, Selenium Framework hakkında video izleyebilir ve projenin geliştirilmesine yardımcı olabilirsiniz. Teşekkürler!

 - ukey-downloader'ın v1-v1.2 arasında kullandığı README dosyasının çevirisini yaptığı için [Sabir Süleymanlı'ya](https://www.linkedin.com/in/sabirs/) teşekkür ederiz.
