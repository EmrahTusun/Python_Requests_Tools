# Python_Requests_Tools
Bu proje, temel web keşfi (web reconnaissance) tekniklerini öğrenmek ve pratik yapmak amacıyla hazırlanmış basit bir Python çalışmasıdır.

Projede şu anda aşağıdaki araçlar yer almaktadır:
- Subdomain (alt alan adı) tarama
- Directory brute-force (dizin tarama)
- Temel web spider (site içi link tarama)

Tüm scriptler Python ile yazılmıştır ve ağırlıklı olarak `requests` kütüphanesi kullanılmıştır.  
Projenin amacı, bu tekniklerin **nasıl çalıştığını öğrenmek** ve temel seviyede uygulamaktır.

## Özellikler
- Basit ve okunabilir Python kodları
- HTTP / HTTPS desteği
- Bağlantı hatalarını güvenli şekilde yakalama
- Aynı domain içinde temel link taraması
- Yeni başlayanlar için uygun yapı

## Kullanım
Gerekli kütüphaneleri kurun:
```bash
pip install -r requirements.txt
python subdomainFinder.py
python directoryFinder.py
python basicSpider.py

