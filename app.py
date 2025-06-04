import streamlit as st
import pandas as pd
import re
import joblib

# Fungsi untuk membuat K-mers
def get_kmers(sequence, size=3):
    return [sequence[i:i+size] for i in range(len(sequence) - size + 1)]

# Load model dan preprocessing tools
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

# UI Streamlit
st.title("DNA Sequence Classification for Diabetes Mellitus")
st.markdown("""
This application is designed to classify DNA sequences into three main categories:

- **DMG**: Gestational Diabetes Mellitus  
- **DMT1**: Type 1 Diabetes Mellitus  
- **DMT2**: Type 2 Diabetes Mellitus  

Please enter a DNA sequence (only letters **A**, **C**, **G**, and **T**) below, then click the **Predict** button to see the classification result.
""")


sequence = st.text_area("Input DNA Sequence", height=150)

# Tombol untuk memicu prediksi
if st.button("Prediction"):
    if not sequence:
        st.warning("Please enter a DNA sequence first.")
    else:
        sequence = sequence.strip().upper()

        if not re.match("^[ACGT]+$", sequence):
            st.error("Invalid sequence. Only the letters A, C, G, and T are allowed.")
        else:
            try:
                # Proses sequence
                kmer_size = 3  # Sesuaikan dengan model training
                kmers = get_kmers(sequence, size=kmer_size)
                joined_kmers = ' '.join(kmers)

                # Transformasi ke vektor
                x_kmers = vectorizer.transform([joined_kmers])
                x_df = pd.DataFrame(x_kmers.toarray(), columns=vectorizer.get_feature_names_out())

                # Normalisasi
                x_scaled = scaler.transform(x_df)

                # Prediksi
                pred_encoded = model.predict(x_scaled)
                pred_class = encoder.inverse_transform(pred_encoded)

                st.success(f"Predicted DNA class: **{pred_class[0]}**")

            except Exception as e:
                st.error(f"An error occurred during processing: {e}")
