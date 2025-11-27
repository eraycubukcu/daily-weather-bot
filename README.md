# 🌦️ Twitter Daily Weather Bot (Regional Automation)

**Python ve GitHub Actions ile geliştirilmiş, sunucusuz (serverless) çalışan tam otomatik hava durumu asistanı.**

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Twitter API](https://img.shields.io/badge/Twitter_API-v2-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://developer.twitter.com/)
[![GitHub Actions](https://img.shields.io/badge/Infrastructure-GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com/features/actions)

> 🔗 **Canlı Bot Hesabı:** [https://x.com/HavaRaporcusu](https://x.com/HavaRaporcusu)

---

## 📖 Proje Hakkında

Bu proje, Türkiye'nin **7 coğrafi bölgesi** için günlük hava durumu verilerini analiz eden ve her sabah otomatik olarak Twitter üzerinde raporlayan bir otomasyon yazılımıdır.

Herhangi bir fiziksel sunucuya ihtiyaç duymadan, **GitHub Actions** üzerinde planlanmış görevler (Cron Jobs) mantığıyla çalışır.

### ✨ Temel Özellikler
* ⏰ **Tam Otomatik:** Her sabah **13:00** saatinde sistem uyanır.
* 🌍 **Bölgesel Kapsam:** Türkiye'nin 7 bölgesi için (Marmara, Ege, İç Anadolu vb.) ayrı ayrı raporlar oluşturur.

---

## ⚙️ Teknik Mimari

Proje aşağıdaki teknoloji yığınını kullanmaktadır:

| Teknoloji | Kullanım Amacı |
| :--- | :--- |
| **Python 3.10** | Ana programlama dili ve veri işleme. |
| **GitHub Actions** | Cron Job yönetimi ve CI/CD süreçleri (Serverless çalışma). |
| **Tweepy** | Twitter API v2 ile OAuth kimlik doğrulama ve tweet gönderimi. |
| **OpenWeatherMap** | Anlık sıcaklık, hissedilen sıcaklık ve hava durumu açıklaması verileri. |

---

## 💻 Kurulum (Yerel Ortam)

Projeyi kendi bilgisayarınızda çalıştırmak veya geliştirmek isterseniz:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone https://github.com/eraycubukcu/daily-weather-bot.git
    cd daily-weather-bot
    ```

2.  **Gerekli Paketleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ortam Değişkenlerini Tanımlayın:**
    Ana dizinde `.env` adında bir dosya oluşturun ve API anahtarlarınızı girin:
    ```ini
    API_KEY=twitter_consumer_key
    API_SECRET=twitter_consumer_secret
    ACCESS_TOKEN=twitter_access_token
    ACCESS_SECRET=twitter_access_token_secret
    WEATHER_API_KEY=openweather_app_id
    ```

4.  **Test Edin:**
    ```bash
    python main.py
    ```

---

## 📢 Örnek Tweet Çıktısı

Botun paylaştığı içerik formatı aşağıdaki gibidir:

> 📅 **25.11.2025 - Karadeniz Bölgesi** 🇹🇷
>
> 📍 **Samsun:** 14°C, Parçalı Bulutlu
> 📍 **Trabzon:** 13°C, Hafif Yağmurlu
> 📍 **Rize:** 12°C, Sağanak Yağışlı
> 📍 **Zonguldak:** 11°C, Açık
>
> #HavaDurumu #Türkiye

---

* LinkedIn: [Profilim](https://linkedin.com/in/eraycubukcu)
