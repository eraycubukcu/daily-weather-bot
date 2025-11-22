import tweepy
import requests
import os
import sys
import time
from dotenv import load_dotenv
from datetime import datetime

# --- AYARLAR ---
load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
weather_api_key = os.getenv("WEATHER_API_KEY")

if not weather_api_key:
    print("❌ HATA: API Key bulunamadı!")
    sys.exit()

# BÖLGELER VE ŞEHİRLER SÖZLÜĞÜ
# Her bölgeye 4-5 önemli şehir koyduk ki 280 karakteri aşmasın.
BOLGELER = {
    "Marmara": ["Istanbul", "Bursa", "Edirne", "Kocaeli", "Canakkale"],
    "Ege": ["Izmir", "Mugla", "Aydin", "Denizli", "Manisa"],
    "Akdeniz": ["Antalya", "Adana", "Mersin", "Hatay", "Isparta"],
    "İç Anadolu": ["Ankara", "Konya", "Eskisehir", "Kayseri", "Sivas"],
    "Karadeniz": ["Samsun", "Trabzon", "Rize", "Zonguldak", "Ordu"],
    "Doğu Anadolu": ["Erzurum", "Van", "Malatya", "Elazig", "Kars"],
    "G.Doğu Anadolu": ["Gaziantep", "Sanliurfa", "Diyarbakir", "Mardin", "Batman"]
}

def hava_durumu_getir(sehir):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': sehir,
        'appid': weather_api_key,
        'units': 'metric',
        'lang': 'tr'
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

def tweet_at(icerik):
    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret
        )
        client.create_tweet(text=icerik)
        print("✅ Tweet başarıyla gönderildi!")
    except Exception as e:
        print(f"❌ Tweet atılamadı: {e}")

def botu_calistir():
    print("📡 Bölgesel rapor sistemi başlatılıyor...")
    bugun = datetime.now().strftime("%d.%m.%Y")

    # Sözlükteki her bölge için döngü başlat
    for bolge_adi, sehirler_listesi in BOLGELER.items():
        
        print(f"\n--- {bolge_adi} Bölgesi Hazırlanıyor ---")
        tweet_metni = f"📅 {bugun} - {bolge_adi} Bölgesi 🇹🇷\n\n"
        
        veri_var_mi = False
        
        for sehir in sehirler_listesi:
            veri = hava_durumu_getir(sehir)
            if veri:
                sicaklik = round(veri['main']['temp'])
                durum = veri['weather'][0]['description'].title()
                # Şehir ismini Türkçe karakter düzeltmesi ile yazdırabiliriz ama şimdilik basit tutalım
                # Gelen verideki şehir adını (name) kullanmak daha şık olabilir
                sehir_adi = veri['name'] 
                
                tweet_metni += f"📍 {sehir_adi}: {sicaklik}°C, {durum}\n"
                veri_var_mi = True
        
        tweet_metni += "\n#HavaDurumu #Türkiye"
        
        if veri_var_mi:
            # Karakter kontrolü
            if len(tweet_metni) <= 280:
                tweet_at(tweet_metni)
            else:
                print(f"⚠️ {bolge_adi} tweeti çok uzun, atılamadı!")
            
            # ⏳ ÖNEMLİ: Her tweet arası 30 saniye bekle (Spam koruması)
            print("⏳ Diğer bölge için 30 saniye bekleniyor...")
            time.sleep(30)
        else:
            print(f"❌ {bolge_adi} için veri alınamadı.")

if __name__ == "__main__":
    botu_calistir()
