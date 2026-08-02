# 🚀 Panduan Deployment Dual-Hosting PT INCAP

Dokumen ini berisi panduan langkah demi langkah untuk mempublikasikan:
1. **Website Utama** di **GitHub Pages** (`github.io` / `www.incap.id`)
2. **Portal Demo Interaktif** di **Streamlit Community Cloud** (`streamlit.app`)

---

## 🌐 BAGIAN 1: Deployment Website Utama ke GitHub Pages

### Opsi A: Menggunakan Repositori Terpisah (Direkomendasikan untuk Custom Domain)

1. **Buat Repositori Baru di GitHub**:
   - Buka [github.com/new](https://github.com/new).
   - Beri nama repositori: `ptincap.github.io` (atau `incap-landing`).
   - Atur visibilitas ke **Public**.

2. **Upload/Push Konten `github_pages_site`**:
   Buka terminal di komputer Anda dan jalankan perintah berikut:
   ```bash
   cd d:\Documents\#ptincap\ptincap\github_pages_site
   git init
   git add .
   git commit -m "Initial release PT INCAP main site"
   git branch -M main
   git remote add origin https://github.com/USERNAME/ptincap.github.io.git
   git push -u origin main
   ```
   *(Ganti `USERNAME` dengan nama akun GitHub Anda)*.

3. **Aktifkan GitHub Pages**:
   - Buka halaman repositori Anda di GitHub.
   - Klik **Settings** ➔ **Pages**.
   - Pada bagian **Build and deployment**:
     - Source: Pilih **Deploy from a branch**.
     - Branch: Pilih **main** / **(root)**.
   - Klik **Save**.
   - Tunggu 1–2 menit, website Anda akan aktif di `https://USERNAME.github.io`.

4. **Konfigurasi Custom Domain (`www.incap.id`)**:
   - File `CNAME` yang berisi `www.incap.id` sudah tersedia secara otomatis di folder proyek.
   - Buka penyedia domain Anda (misal: Niagahoster, Domainesia, Cloudflare).
   - Tambahkan **CNAME Record**:
     - Name/Host: `www`
     - Target/Value: `USERNAME.github.io`
   - Pada Settings GitHub Pages, centang **Enforce HTTPS**.

---

## 🐍 BAGIAN 2: Deployment Portal Demo ke Streamlit Community Cloud

1. **Buat Repositori GitHub untuk Streamlit Lab**:
   - Buka [github.com/new](https://github.com/new).
   - Beri nama repositori: `incap-demo-lab`.
   - Visibilitas: **Public** (Syarat gratis Streamlit Cloud).

2. **Upload/Push Konten `streamlit_lab_app`**:
   ```bash
   cd d:\Documents\#ptincap\ptincap\streamlit_lab_app
   git init
   git add .
   git commit -m "Initial release INCAP Streamlit Lab"
   git branch -M main
   git remote add origin https://github.com/USERNAME/incap-demo-lab.git
   git push -u origin main
   ```

3. **Daftar & Hubungkan ke Streamlit Cloud**:
   - Buka [share.streamlit.io](https://share.streamlit.io).
   - Login menggunakan akun GitHub Anda.

4. **Deploy App Baru**:
   - Klik tombol **"Create app"** / **"New app"**.
   - Isi formulir deployment:
     - **Repository**: `USERNAME/incap-demo-lab`
     - **Branch**: `main`
     - **Main file path**: `app.py`
     - **App URL (Custom Subdomain)**: `incap-demo-lab` (menghasilkan URL `https://incap-demo-lab.streamlit.app`).
   - Klik **Deploy!**.
   - Streamlit akan menginstall dependensi `requirements.txt` dan meluncurkan aplikasi dalam 1–2 menit.

---

## 🔗 BAGIAN 3: Menghubungkan Kedua Website (Koneksi Hybrid)

1. Di **GitHub Pages (`index.html`)**:
   - Tombol badge **`⚡ Streamlit Lab Demo`** mengarah ke URL Streamlit Anda (`https://incap-demo-lab.streamlit.app`).
2. Di **Streamlit Lab (`app.py`)**:
   - Sidebar badge **`🏠 Kembali ke Website Utama`** mengarah ke website utama Anda (`https://www.incap.id`).
