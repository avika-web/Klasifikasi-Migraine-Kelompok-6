import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB

st.set_page_config(page_title="Klasifikasi Migrain", layout="wide")
st.title("Aplikasi Klasifikasi Jenis Migrain")

st.markdown("""
Aplikasi ini memungkinkan Anda mengisi data pasien secara manual untuk mengetahui jenis migrain menggunakan algoritma **Naive Bayes**.
""")

data = pd.read_csv("data_migraine.csv")  # Gantilah path jika jalankan di server Streamlit
data['Type'] = data['Type'].str.title()

X = data.drop("Type", axis=1)
y = data["Type"]

model = GaussianNB()
model.fit(X, y)

with st.form("migraine_form"):
    st.subheader("Masukkan Data Pasien")

    st.markdown("**Umur**")
    st.caption("Menunjukkan usia pasien yang mengalami migrain.")
    age = st.number_input("", min_value=0, max_value=120, value=25)

    st.markdown("**Durasi Migrain**")
    st.caption("1 = Pendek <4 jam, 2 = Sedang 4–24 jam, 3 = Panjang >24 jam")
    duration = st.selectbox("", options=[1, 2, 3], format_func=lambda x: {1: "<4 jam", 2: "4-24 jam", 3: ">24 jam"}[x])

    st.markdown("**Frekuensi**")
    st.caption("1 = Jarang, 2=Terjadi sesekali dalam sebulan, 3=Terjadi beberapa kali dalam sebulan, 4=Sekitar dalam sekitar sekali dalam seminggu, 5=Terjadi beberapa kali dalam seminggu, 6=Terjadi hampir setiap hari, 7=Terjadi setip hari, 8=Lebih dari sekali sehari")
    frequency = st.selectbox("", options=list(range(1, 8)))

    st.markdown("**Lokasi Nyeri Kepala**")
    st.caption("0 = Unilateral, 1 = Bilateral, 2 = Belakang/leher")
    location = st.selectbox("", options=[0, 1, 2])

    st.markdown("**Karakter Nyeri**")
    st.caption("0 = Berdenyut, 1 = Menusuk, 2 = Tumpul")
    character = st.selectbox("", options=[0, 1, 2])

    st.markdown("**Intensitas Nyeri**")
    st.caption("0 = Ringan, 1 = Sedang, 2 = Berat, 3 = Sangat Berat")
    intensity = st.selectbox("", options=[0, 1, 2, 3])

    st.markdown("**Mual**")
    st.caption("0 = Tidak, 1 = Ya")
    nausea = st.radio("", [0, 1])

    st.markdown("**Muntah**")
    st.caption("0 = Tidak, 1 = Ya")
    vomit = st.radio("", [0, 1])

    st.markdown("**Sensitif Suara (Phonophobia)**")
    st.caption("0 = Tidak, 1 = Ya")
    phonophobia = st.radio("", [0, 1])

    st.markdown("**Sensitif Cahaya (Photophobia)**")
    st.caption("0 = Tidak, 1 = Ya")
    photophobia = st.radio("", [0, 1])

    st.markdown("**Gangguan Visual**")
    st.caption("0 = Normal, 1 = Kilatan cahaya, 2 = Blind spot, 3 = Penglihatan bergelombang, 4 = Kehilangan penglihatan")
    visual = st.selectbox("", options=[0, 1, 2, 3, 4])

    st.markdown("**Gangguan Sensorik**")
    st.caption("0 = Tidak ada, 1 = Gangguan ringan, 2 = Gangguan berat")
    sensory = st.selectbox("", options=[0, 1, 2])

    st.markdown("**Kesulitan Berbicara (Dysphasia)**")
    st.caption("0 = Tidak, 1 = Ya, kesulitan bicara saat migrain")
    dysphasia = st.radio("", [0, 1])

    st.markdown("**Gangguan Bicara Otot (Dysarthria)**")
    st.caption("0 = Tidak, 1 = Ya, akibat kelemahan otot bicara")
    dysarthria = st.radio("", [0, 1])

    st.markdown("**Vertigo**")
    st.caption("0 = Tidak, 1 = Ya")
    vertigo = st.radio("", [0, 1])

    st.markdown("**Tinnitus**")
    st.caption("0 = Tidak, 1 = Ya (telinga berdenging)")
    tinnitus = st.radio("", [0, 1])

    st.markdown("**Gangguan Pendengaran (Hypoacusis)**")
    st.caption("0 = Tidak, 1 = Ya")
    hypoacusis = st.radio("", [0, 1])

    st.markdown("**Diplopia (Penglihatan Ganda)**")
    st.caption("0 = Tidak, 1 = Ya, melihat objek menjadi dua")
    diplopia = st.radio("", [0, 1])

    st.markdown("**Cacat Neurologis (Defect)**")
    st.caption("0 = Tidak, 1 = Ya")
    defect = st.radio("", [0, 1])

    st.markdown("**Gangguan Keseimbangan (Ataxia)**")
    st.caption("0 = Tidak, 1 = Ya")
    ataxia = st.radio("", [0, 1])

    st.markdown("**Gangguan Kesadaran (Conscience)**")
    st.caption("0 = Tidak, 1 = Ya, misal pingsan/semi sadar")
    conscience = st.radio("", [0, 1])

    st.markdown("**Parestesia**")
    st.caption("0 = Tidak, 1 = Ya, kesemutan atau mati rasa")
    paresthesia = st.radio("", [0, 1])

    st.markdown("**DPF (penyempitan kelopak mata)**")
    st.caption("0 = Tidak, 1 = Ya, penyempitan kelopak mata kontrateral")
    dpf = st.radio("", [0, 1])

    submitted = st.form_submit_button("Klasifikasi Migrain")

if submitted:
    user_data = [[age, duration, frequency, location, character, intensity, nausea, vomit,
                  phonophobia, photophobia, visual, sensory, dysphasia, dysarthria, vertigo,
                  tinnitus, hypoacusis, diplopia, defect, ataxia, conscience, paresthesia, dpf]]
    prediction = model.predict(user_data)
    st.success(f"✅ Jenis migrain yang diprediksi: **{prediction[0]}**")
