# 🔐 CyberEnigma - Spam Aniqlash Tizimi

**CyberEnigma** - bu sun'iy intellekt va mashinali o'rganish texnologiyalari yordamida spam xabarlarni aniqlaydigan Flask asosidagi web ilova.

## 📋 Loyiha Haqida

Bu loyiha xabar matnlarini tahlil qilib, ularning spam yoki spam emasligini aniqlaydi. Tizim Naive Bayes algoritmi va scikit-learn kutubxonasidan foydalangan holda xabarlarni klassifikatsiya qiladi. 

## ✨ Asosiy Xususiyatlar

- 🤖 **Spam Aniqlash** - Matnli xabarlarni tahlil qilish va spam/ham klassifikatsiyasi
- 📊 **Machine Learning** - Naive Bayes algoritmi asosida o'qitilgan model
- 🗄️ **Ma'lumotlar Bazasi** - MySQL bilan integratsiya
- 🔐 **Autentifikatsiya** - Foydalanuvchilarni ro'yxatdan o'tkazish va kirish tizimi
- 🌐 **RESTful API** - Flask orqali yaratilgan API endpointlar
- 🚀 **CORS Qo'llab-quvvatlash** - Frontend bilan oson integratsiya

## 🛠️ Texnologiyalar

- **Backend:** Flask (Python)
- **Machine Learning:** scikit-learn, pandas, numpy
- **Ma'lumotlar Bazasi:** MySQL
- **ORM:** SQLAlchemy
- **Autentifikatsiya:** Flask-Login, Flask-Bcrypt
- **Server:** Gunicorn

## 📁 Loyiha Strukturasi

```
cyberenigma/
├── controller/           # Controllerlar (biznes logika)
│   ├── sitecontroller.py    # Asosiy sahifa va spam tekshirish
│   └── authcontroller.py    # Autentifikatsiya
├── model/               # Ma'lumotlar bazasi modellari
│   ├── spam.py             # Spam modeli
│   └── user. py             # Foydalanuvchi modeli
├── routes/              # URL marshrutlar
│   ├── site. py             # Asosiy marshrutlar
│   └── auth.py             # Auth marshrutlar
├── services/            # Servislar va yordamchi funksiyalar
│   └── spamanalizer.py     # Spam tahlil qilish servisi
├── main.py              # Asosiy kirish nuqtasi
├── db.py                # Ma'lumotlar bazasi konfiguratsiyasi
├── spam.csv             # O'qitish uchun dataset
├── requirements.txt     # Python kutubxonalari
└── req.txt              # To'liq kutubxonalar ro'yxati
```

## 🚀 O'rnatish va Ishga Tushirish

### 1. Repozitoriyani Klonlash

```bash
git clone https://github.com/root0x7/cyberenigma.git
cd cyberenigma
```

### 2. Virtual Muhitni Yaratish

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows
```

### 3. Kerakli Kutubxonalarni O'rnatish

```bash
pip install -r requirements.txt
```

### 4. Ma'lumotlar Bazasini Sozlash

MySQL ma'lumotlar bazasini yarating:

```sql
CREATE DATABASE enigma;
```

`main.py` faylida ma'lumotlar bazasi ulanishini sozlang:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://foydalanuvchi:parol@localhost/enigma'
```

### 5. Ilovani Ishga Tushirish

```bash
python main.py
```

Ilova `http://localhost:5000` manzilida ishga tushadi.

## 📡 API Endpointlar

### Asosiy Endpointlar

#### 1. Asosiy Sahifa
```
GET /
```
**Javob:** Flask ilovasi ishlayotganligini tasdiqlaydi

#### 2. Spam Tekshirish (CSV ma'lumotlari asosida)
```
GET /analiz? msg=your_message_here
```
**Parametrlar:**
- `msg` - Tekshiriladigan xabar matni

**Javob:**
```json
{
  "status": "spam"  // yoki "not-spam"
}
```

#### 3. Spam Tekshirish (Bazadagi ma'lumotlar asosida)
```
GET /spam? msg=your_message_here
```
**Parametrlar:**
- `msg` - Tekshiriladigan xabar matni

**Javob:**
```json
{
  "status": "spam"  // yoki "not-spam"
}
```

### Autentifikatsiya Endpointlar

#### 1. Kirish
```
GET /auth/login? login=username&password=password
```
**Parametrlar:**
- `login` - Foydalanuvchi nomi
- `password` - Parol

**Javob:**
```json
{
  "login": "username",
  "pass": "password"
}
```

#### 2. Profil
```
GET /auth/profile
```
**Javob:** Foydalanuvchi profili ma'lumotlari

## 🧠 Machine Learning Modeli

Loyihada **Multinomial Naive Bayes** algoritmi qo'llanilgan:

1. **Dataset:** `spam.csv` fayli - spam va ham xabarlar to'plami
2. **Feature Extraction:** CountVectorizer - matnni raqamli ko'rinishga o'tkazish
3. **Train/Test Split:** 67% o'qitish, 33% test
4. **Model:** MultinomialNB klassifikatori

### Model Ishlash Prinsipi

```python
1. Matnni vektorlarga aylantirish (CountVectorizer)
2. Modelni o'qitish (train data)
3. Yangi xabarni tahlil qilish
4. Natija:  spam yoki ham
```

## 💾 Ma'lumotlar Bazasi Modellari

### Spam Modeli
```python
- id: Integer (Primary Key)
- status: String (spam/ham)
- message: Text (xabar matni)
- date: Date (sana)
```

### User Modeli
```python
- id: Integer (Primary Key)
- login: String (foydalanuvchi nomi)
- password: String (parol - hash qilingan)
- role: String (foydalanuvchi roli)
```

## 🔧 Konfiguratsiya

### CORS Sozlamalari
```python
CORS(app, origins=["http://localhost:8080"])
```

### Ma'lumotlar Bazasi
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://phpmyadmin:xroot@localhost/enigma'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### Secret Key
```python
app.secret_key = 'juda_ishonchli_parol'
```

## 📊 Foydalanish Misollari

### cURL yordamida

```bash
# Spam tekshirish
curl "http://localhost:5000/analiz?msg=Congratulations!  You won $1000"

# Kirish
curl "http://localhost:5000/auth/login?login=admin&password=123456"
```

### Python yordamida

```python
import requests

# Spam tekshirish
response = requests.get('http://localhost:5000/analiz', 
                       params={'msg': 'Free money click here'})
print(response.json())
```

## 🤝 Hissa Qo'shish

1. Repozitoriyani fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. O'zgarishlarni commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Branchga push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

## 📝 Litsenziya

Bu loyiha ochiq kodli loyiha hisoblanadi. 

## 👨‍💻 Muallif

**root0x7** - [GitHub Profile](https://github.com/root0x7)

## 📧 Aloqa

Savollar yoki takliflar uchun GitHub Issues orqali murojaat qiling.

---

⭐ Agar loyiha yoqsa, repo'ga yulduzcha qo'yishni unutmang!
