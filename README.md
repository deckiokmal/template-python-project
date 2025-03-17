# My Flask API Project

## 📌 Overview
Proyek ini adalah **Flask API** dengan **JWT Authentication**, database **PostgreSQL**, dan logging untuk **System & User Activity**. Proyek ini di-deploy menggunakan **Docker**.

## 🚀 Features
- 🔐 **JWT Authentication** untuk keamanan
- 📦 **PostgreSQL** sebagai database utama
- 📊 **Logging System & User Activity** tersimpan di database
- 🐳 **Docker & Docker Compose** untuk deployment

## 🛠️ Installation & Setup
### 1️⃣ Clone Repository
```sh
git clone https://github.com/deckiokmal/project-template.git
cd project-template
```

### 2️⃣ Setup Environment Variables
Buat file `.env` di root proyek berdasarkan `.env.example` dan isi dengan konfigurasi yang sesuai.

### 3️⃣ Build & Run dengan Docker
```sh
docker-compose up --build
```

Backend Flask API akan berjalan di `http://localhost:5000`.

### 4️⃣ Menjalankan Migrasi Database (Jika Diperlukan)
```sh
docker exec -it flask_api_backend flask db upgrade
```

## 📜 API Documentation
API ini memiliki beberapa endpoint utama:
| Endpoint | Method | Deskripsi |
|----------|--------|-----------|
| `/auth/login` | POST | Login dengan JWT |
| `/users` | GET | Mendapatkan daftar user |
| `/logs` | GET | Mendapatkan system & user activity logs |

Dokumentasi API lengkap tersedia di **Postman Collection**.


## 📌 Contoh Request API
### 🔑 Login
```sh
curl -X POST "http://localhost:5000/auth/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "password"}'
```

### 📌 Mendapatkan Daftar Pengguna (dengan JWT)
```sh
curl -X GET "http://localhost:5000/users" \
     -H "Authorization: Bearer <your_jwt_token>"
```

## 🛠️ Troubleshooting
### 1️⃣ **Database tidak dapat terhubung**
- Pastikan container database berjalan:
  ```sh
  docker ps
  ```
- Cek logs database:
  ```sh
  docker logs flask_api_db
  ```

### 2️⃣ **Docker Container Tidak Berjalan**
- Jalankan ulang dengan perintah:
  ```sh
  docker-compose down && docker-compose up --build
  ```

## 🤝 Contribution
Jika ingin berkontribusi, silakan buat **Issue** atau **Pull Request**. Terima kasih! 😊