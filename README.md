# DNA Sequence Classification for Diabetes Mellitus

Aplikasi ini adalah proyek machine learning berbasis **Streamlit** yang bertujuan untuk mengklasifikasikan sekuens DNA ke dalam tiga jenis utama diabetes mellitus:

- **DMG**: Gestational Diabetes Mellitus  
- **DMT1**: Type 1 Diabetes Mellitus  
- **DMT2**: Type 2 Diabetes Mellitus  

## 🌐 Demo Online

👉 **[Streamlit App](https://diabetes-mellitus-dna-sequences-mka.streamlit.app/)**

> Gantilah URL di atas dengan link Streamlit Cloud Anda.

## 🚀 Fitur Utama

- Antarmuka pengguna interaktif berbasis web (Streamlit)
- Input sekuens DNA dengan validasi huruf A, C, G, T
- Pra-pemrosesan otomatis menggunakan **K-mer** (ukuran k = 3)
- Vektorisasi menggunakan model TF-IDF
- Normalisasi fitur menggunakan `scaler`
- Prediksi jenis diabetes menggunakan model klasifikasi terlatih (`model.pkl`)
- Interpretasi hasil klasifikasi ke label aslinya menggunakan `encoder`



