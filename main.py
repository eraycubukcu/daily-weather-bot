import tweepy
import requests
import os
import sys
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
weather_api_key = os.getenv("WEATHER_API_KEY")

if not weather_api_key:
    print("❌ HATA: .env dosyasında WEATHER_API_KEY bulunamadı!")
    sys.exit()

SEHIRLER = ["Istanbul", "Ankara", "Izmir", "Samsun", "Bursa", "Antalya"]

def hava_durumu_getir(sehir):
    """OpenWeatherMap'ten detaylı veri çeker"""
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': sehir,
        'appid': weather_api_key,
        'units': 'metric',
        'lang': 'tr'
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 401:
            print("⚠️ UYARI: Weather API Key henüz aktif değil veya hatalı.")
            print("   -> Yeni aldıysan 10-15 dk beklemen gerekebilir.")
            return None
            
        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠️ {sehir} için veri alınamadı. Kod: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Bağlantı hatası: {e}")
        return None

def tweet_at(icerik):
    """Hazırlanan metni Twitter'a gönderir"""
    if not icerik:
        return

    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret
        )
        
        response = client.create_tweet(text=icerik)
        print(f"\n✅ BAŞARILI! Tweet gönderildi. ID: {response.data['id']}")
        print("-" * 30)
        print(icerik)
        print("-" * 30)
        
    except Exception as e:
        print(f"\n❌ TWITTER HATASI: {e}")
        if "403" in str(e):
            print("👉 İpucu: Developer Portal'da 'App Permissions' kısmını 'Read and Write' yaptın mı?")

def botu_calistir():
    print("📡 Hava durumu verileri toplanıyor...")
    
    bugun = datetime.now().strftime("%d.%m.%Y")
    
    # Tweet Başlığı
    tweet_metni = f"📅 {bugun} - Günlük Hava Durumu 🇹🇷\n\n"
    basarili_sehir_sayisi = 0
    
    for sehir in SEHIRLER:
        veri = hava_durumu_getir(sehir)
        if veri:
            # Verileri ayrıştır
            sicaklik = round(veri['main']['temp'])
            hissedilen = round(veri['main']['feels_like'])
            durum = veri['weather'][0]['description'].title()
            
            satir = f"📍 {sehir}: {sicaklik}°C (His:{hissedilen}) {durum}\n"
            tweet_metni += satir
            basarili_sehir_sayisi += 1
    
    if basarili_sehir_sayisi == 0:
        print("❌ Hiçbir şehir için veri alınamadı, tweet atılmıyor.")
        return

    # tweet_metni += "\n#HavaDurumu #Yazılım #Bot"
    
    uzunluk = len(tweet_metni)
    print(f"📝 Tweet Uzunluğu: {uzunluk}/280")
    
    if uzunluk <= 280:
        print("🚀 Tweet gönderiliyor...")
        tweet_at(tweet_metni)
    else:
        print("⚠️ HATA: Tweet 280 karakteri aştı! Şehir sayısını azaltmalısın.")

if __name__ == "__main__":
    botu_calistir()