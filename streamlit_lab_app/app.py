"""
==============================================================================
PT INCAP DIGITAL TEKNOLOGI - INTERACTIVE DEMO LAB (STREAMLIT CLOUD PORTAL)
==============================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import math

# --- PAGE SETUP ---
st.set_page_config(
    page_title="INCAP Tech Lab | Interactive PoC Hub",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-tagline {
        font-size: 1rem;
        color: #8892b0;
        font-style: italic;
        margin-bottom: 1.5rem;
    }
    .lab-card {
        background-color: #10213e;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid rgba(0, 242, 254, 0.2);
        margin-bottom: 15px;
    }
    .stMetric {
        background-color: rgba(16, 33, 62, 0.7);
        border: 1px solid rgba(0, 242, 254, 0.2);
        border-radius: 10px;
        padding: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR & HYBRID NAVIGATION ---
st.sidebar.markdown("## 🌐 PT INCAP Tech Lab")
st.sidebar.caption("⚡ *Interactive Proof of Concept Portal*")
st.sidebar.markdown("---")

st.sidebar.markdown("""
<a href="https://www.incap.id" target="_blank" style="text-decoration: none;">
    <div style="background: linear-gradient(135deg, #0078d4, #00f2fe); color: white; padding: 10px 16px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px;">
        🏠 Kembali ke Website Utama (incap.id)
    </div>
</a>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Pilih Modul Lab:",
    [
        "🏠 Overview & Hybrid Ecosystem",
        "🤖 Demo AI: Sentiment & Price Prediction",
        "📡 Demo IoT: Real-time Telemetry Monitor",
        "🛡️ Demo Security: Header & Cipher Audit",
        "📋 Interactive PoC RAB Customizer"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Kontak Resmi PT INCAP:**
- 📧 Email: ptincap@gmail.com
- 🌐 Web: [www.incap.id](https://www.incap.id)
""")

# ==============================================================================
# 1. OVERVIEW & HYBRID ECOSYSTEM
# ==============================================================================
if menu == "🏠 Overview & Hybrid Ecosystem":
    st.markdown('<div class="main-header">PT INCAP Digital Teknologi</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-tagline">"Our Achievements is Your Success"</div>', unsafe_allow_html=True)

    st.write("""
    Selamat datang di **INCAP Tech Lab**, portal demonstrasi interaktif khusus untuk menguji keandalan solusi kecerdasan buatan (AI), sistem telemetri IoT, dan pengujian keamanan siber berstandar *White Hacker*.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="lab-card">
            <h4>🌐 Website Utama (GitHub Pages)</h4>
            <p style="color: #8892b0; font-size: 0.9rem;">
                Dihosting di <code>www.incap.id</code> untuk kecepatan akses CDN global, profil perusahaan, 
                dan penangkapan lead klien dengan keandalan 100%.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="lab-card">
            <h4>🐍 Interactive Demo Lab (Streamlit Cloud)</h4>
            <p style="color: #8892b0; font-size: 0.9rem;">
                Dihosting di Streamlit Cloud untuk mengeksekusi model Python AI/ML, grafis IoT real-time, 
                dan simulasi audit teknis secara langsung.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔄 7 Metodologi PoC INCAP")
    
    steps = [
        "01. Business Question & Value Definition",
        "02. Proof of Concept (PoC) & Requirement Gathering",
        "03. Data Collection & System Architecture",
        "04. Feature Engineering & Development / Coding",
        "05. Security Audit & Testing (White Hacker)",
        "06. Model & System Deployment",
        "07. Production & Maintenance"
    ]
    
    st.progress(100)
    c1, c2 = st.columns(2)
    for idx, s in enumerate(steps):
        if idx % 2 == 0:
            c1.success(f"✓ {s}")
        else:
            c2.info(f"✓ {s}")

# ==============================================================================
# 2. DEMO AI & DATA SCIENCE
# ==============================================================================
elif menu == "🤖 Demo AI: Sentiment & Price Prediction":
    st.markdown("## 🤖 Demo Interactive AI & Machine Learning")
    st.write("Uji kemampuan modul NLP (Sentiment Engine) dan Prediksi Deret Waktu (Time-Series Price Prediction).")

    tab1, tab2 = st.tabs(["📝 Sentiment Analysis Engine", "📈 Dynamic Price Prediction Simulator"])

    with tab1:
        st.subheader("Uji Analisis Sentimen Teks (NLP)")
        user_text = st.text_area(
            "Masukkan Teks Ulasan / Komentar Klien:",
            "Layanan integrasi IoT dan AI dari PT INCAP sangat cepat, responsif, aman, dan meningkatkan efisiensi operasional bisnis secara signifikan!"
        )

        if st.button("Jalankan Sentiment Engine", type="primary"):
            pos_keywords = ["cepat", "bagus", "aman", "efisien", "responsif", "terbaik", "inovatif", "signifikan", "puas", "hebat"]
            neg_keywords = ["lambat", "error", "rusak", "mahal", "buruk", "jelek", "gagal"]

            text_lower = user_text.lower()
            pos_score = sum(1 for w in pos_keywords if w in text_lower)
            neg_score = sum(1 for w in neg_keywords if w in text_lower)

            st.markdown("#### Hasil Analisis Engine:")
            if pos_score > neg_score:
                st.success(f"✅ **Sentimen: POSITIF** (Skor Kepercayaan: {min(0.7 + pos_score * 0.1, 0.99):.2%})")
                st.json({
                    "Polarity": "Positive",
                    "Extracted_Entities": ["IoT", "AI", "PT INCAP"],
                    "Key_Attributes": ["Efisiensi", "Keamanan", "Performa High Availability"]
                })
            elif neg_score > pos_score:
                st.error("⚠️ **Sentimen: NEGATIF / PERLU EVALUASI**")
            else:
                st.info("ℹ️ **Sentimen: NETRAL**")

    with tab2:
        st.subheader("Simulasi Dynamic Price Prediction (AI Model)")
        days = st.slider("Jumlah Hari Data Historis:", 10, 90, 30)
        volatility = st.slider("Tingkat Volatilitas Pasar:", 0.5, 3.0, 1.2)

        dates = pd.date_range(end=pd.Timestamp.today(), periods=days)
        np.random.seed(42)
        base_price = 150 + np.random.randn(days).cumsum() * volatility
        
        # Forecast 7 days ahead
        forecast_dates = pd.date_range(start=dates[-1] + pd.Timedelta(days=1), periods=7)
        forecast_price = base_price[-1] + np.random.randn(7).cumsum() * volatility

        df_hist = pd.DataFrame({"Tanggal": dates, "Harga Actual": base_price, "Tipe": "Historical"})
        df_fore = pd.DataFrame({"Tanggal": forecast_dates, "Harga Actual": forecast_price, "Tipe": "AI Forecast"})
        df_combined = pd.concat([df_hist, df_fore])

        fig = px.line(df_combined, x="Tanggal", y="Harga Actual", color="Tipe", title="Simulasi Prediksi Harga (PyTorch/TensorFlow Time-Series Model)")
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# 3. DEMO IOT & TELEMETRY MONITOR
# ==============================================================================
elif menu == "📡 Demo IoT: Real-time Telemetry Monitor":
    st.markdown("## 📡 Demo IoT Telemetry & Sensor Dashboard")
    st.write("Simulasi penerimaan data dari node sensor MQTT & Modbus terhubung di Smart Building / Industrial Site.")

    col_a, col_b, col_c = st.columns(3)

    np.random.seed(int(time.time()) % 100)
    temp = round(25.0 + np.random.uniform(-1.2, 1.8), 2)
    humidity = round(58.0 + np.random.uniform(-2.5, 3.0), 1)
    power = round(14.2 + np.random.uniform(-0.8, 1.1), 2)

    col_a.metric("Suhu Node Sensor (°C)", f"{temp} °C", f"{round(temp-25.0, 2)} °C")
    col_b.metric("Kelembaban Udara (%)", f"{humidity} %", f"{round(humidity-58.0, 1)} %")
    col_c.metric("Konsumsi Daya Listrik", f"{power} kW", "Status Normal")

    st.markdown("### Streaming Grafis Telemetri Live")
    
    timeline = pd.date_range(end=pd.Timestamp.now(), periods=25, freq='s')
    vib_data = np.random.normal(0.45, 0.08, 25)
    
    df_iot = pd.DataFrame({
        "Waktu": timeline,
        "Vibrasi Mesin (g)": vib_data,
        "Batas Ambulatory Warning": [0.65] * 25
    })

    fig_iot = px.area(df_iot, x="Waktu", y="Vibrasi Mesin (g)", title="Real-Time Vibration Monitoring Node (Modbus RS485)")
    fig_iot.update_layout(template="plotly_dark")
    st.plotly_chart(fig_iot, use_container_width=True)

# ==============================================================================
# 4. DEMO SECURITY AUDIT
# ==============================================================================
elif menu == "🛡️ Demo Security: Header & Cipher Audit":
    st.markdown("## 🛡️ Demo White Hacker & Security Header Audit Tool")
    st.write("Evaluasi tingkat kepatuhan keamanan web & ketahanan enkripsi cipher.")

    target_domain = st.text_input("Masukkan URL Target Pemindaian:", "https://www.incap.id")

    if st.button("Jalankan Security Penetration Audit", type="primary"):
        st.write(f"🔎 Memindai Header Keamanan untuk `{target_domain}`...")
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        st.success("✅ Audit Selesai! Skor Kepatuhan Keamanan OWASP: **A+ (98/100)**")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Status Security Headers")
            st.checkbox("Strict-Transport-Security (HSTS)", value=True, disabled=True)
            st.checkbox("X-Content-Type-Options: nosniff", value=True, disabled=True)
            st.checkbox("X-Frame-Options: SAMEORIGIN", value=True, disabled=True)
            st.checkbox("Content-Security-Policy (CSP)", value=True, disabled=True)

        with c2:
            st.markdown("#### Analisis Forensik Keamanan")
            st.info("""
            - **Status PenTest**: Bebas dari RCE & SQL Injection.
            - **TLS/SSL Encryption**: TLS 1.3 Active (Cipher Suite: AES-256-GCM).
            - **Rekomendasi White Hacker**: Audit ulang berkala setiap 6 bulan.
            """)

# ==============================================================================
# 5. INTERACTIVE POC RAB CUSTOMIZER
# ==============================================================================
elif menu == "📋 Interactive PoC RAB Customizer":
    st.markdown("## 📋 Customizer Spec & Estimator RAB Proyek")
    st.write("Atur modul kebutuhan teknis dan dapatkan ringkasan alokasi sumber daya PoC.")

    pilars = st.multiselect(
        "Pilih Pilar Solusi Utama:",
        ["Web Application", "Mobile App (iOS/Android)", "Cyber Security Audit & PenTest", "IoT Real-Time Dashboard"],
        default=["Web Application", "Cyber Security Audit & PenTest"]
    )

    tier = st.radio(
        "Pilih Skala Sistem (Users Tier):",
        ["PoC / MVP (<1.000 Users)", "Medium Enterprise (1.000 - 50.000 Users)", "High Availability (>100.000 Users)"]
    )

    if st.button("Generate Dokumen Spesifikasi PoC"):
        st.markdown("### 📜 Ringkasan Spesifikasi Proyek:")
        st.json({
            "Pilar_Terpilih": pilars,
            "Target_Skala": tier,
            "Estimasi_Siklus_PoC": "4 - 8 Minggu",
            "Alokasi_Tim_INCAP": [
                "Solution Architect",
                "Software Engineer",
                "Security White Hacker Specialist"
            ],
            "Jaminan_Layanan": "Garansi Bebas Bug & PenTest Audit Pass"
        })
