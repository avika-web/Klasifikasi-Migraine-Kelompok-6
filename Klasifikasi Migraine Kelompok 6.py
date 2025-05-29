import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB

st.set_page_config(page_title="Klasifikasi Migrain", layout="wide")
st.title("Aplikasi Klasifikasi Jenis Migrain")

st.markdown("""
Web ini memungkinkan Anda untuk mengetahui jenis migrain sesuai dengann kondisi yang ada alami.
""")

data = pd.read_csv("data_migraine.csv")
data['Type'] = data['Type'].str.title()

X = data.drop("Type", axis=1)
y = data["Type"]

model = GaussianNB()
model.fit(X, y)

with st.form("migraine_form"):
    st.subheader("Masukkan Data Sesuai Kondisi Anda")

    st.markdown("**Umur**")
    st.caption("Isilah Usia Anda!")
    age = st.number_input("input_age", min_value=0, max_value=120, value=25, label_visibility="collapsed")

    st.markdown("**Durasi Migrain**")
    st.caption("1 = Pendek <4 jam, 2 = Sedang 4–24 jam, 3 = Panjang >24 jam")
    duration = st.selectbox("input_duration", options=[1, 2, 3], 
                            format_func=lambda x: {1: "<4 jam", 2: "4–24 jam", 3: ">24 jam"}[x], 
                            label_visibility="collapsed")

    st.markdown("**Frekuensi**")
    st.caption("1 = Jarang, 2=Terjadi sesekali dalam sebulan, 3=Terjadi beberapa kali dalam sebulan, 4=Sekitar dalam sekitar sekali dalam seminggu, 5=Terjadi beberapa kali dalam seminggu, 6=Terjadi hampir setiap hari, 7=Terjadi setip hari, 8=Lebih dari sekali sehari")
    frequency = st.selectbox("input_frequency", options=list(range(1, 8)), label_visibility="collapsed")

    st.markdown("**Lokasi Nyeri Kepala**")
    st.caption("0 = Unilateral, 1 = Bilateral, 2 = Belakang/leher")
    location = st.selectbox("input_location", options=[0, 1, 2], label_visibility="collapsed")

    st.markdown("**Karakter Nyeri**")
    st.caption("0 = Berdenyut, 1 = Menusuk, 2 = Tumpul")
    character = st.selectbox("input_character", options=[0, 1, 2], label_visibility="collapsed")

    st.markdown("**Intensitas Nyeri**")
    st.caption("0 = Ringan, 1 = Sedang, 2 = Berat, 3 = Sangat Berat")
    intensity = st.selectbox("input_intensity", options=[0, 1, 2, 3], label_visibility="collapsed")

    st.markdown("**Mual**")
    st.caption("0 = Tidak, 1 = Ya")
    nausea = st.radio("input_nausea", [0, 1], label_visibility="collapsed")

    st.markdown("**Muntah**")
    st.caption("0 = Tidak, 1 = Ya")
    vomit = st.radio("input_vomit", [0, 1], label_visibility="collapsed")

    st.markdown("**Sensitif Suara (Phonophobia)**")
    st.caption("0 = Tidak, 1 = Ya")
    phonophobia = st.radio("input_phonophobia", [0, 1], label_visibility="collapsed")

    st.markdown("**Sensitif Cahaya (Photophobia)**")
    st.caption("0 = Tidak, 1 = Ya")
    photophobia = st.radio("input_photophobia", [0, 1], label_visibility="collapsed")

    st.markdown("**Gangguan Visual**")
    st.caption("0 = Normal, 1=Mengalami kilatan cahaya, 2=Blind spot, 3=Mengalami penglihatan bergelombang, 4 = Gangguan parah seperti kehilangan penglihatan")
    visual = st.selectbox("input_visual", options=[0, 1, 2, 3, 4], label_visibility="collapsed")

    st.markdown("**Gangguan Sensorik**")
    st.caption("0 = Tidak ada, 1=Gangguan Ringan, 2= Gangguan Berat")
    sensory = st.selectbox("input_sensory", options=[0, 1, 2], label_visibility="collapsed")

    st.markdown("**Kesulitan Berbicara (Dysphasia)**")
    st.caption("0 = Tidak, 1 = Ya")
    dysphasia = st.radio("input_dysphasia", [0, 1], label_visibility="collapsed")

    st.markdown("**Gangguan Bicara Otot (Dysarthria)**")
    st.caption("0 = Tidak, 1 = Ya")
    dysarthria = st.radio("input_dysarthria", [0, 1], label_visibility="collapsed")

    st.markdown("**Vertigo**")
    st.caption("0 = Tidak, 1 = Ya")
    vertigo = st.radio("input_vertigo", [0, 1], label_visibility="collapsed")

    st.markdown("**Tinnitus**")
    st.caption("0 = Tidak, 1 = Ya")
    tinnitus = st.radio("input_tinnitus", [0, 1], label_visibility="collapsed")

    st.markdown("**Gangguan Pendengaran (Hypoacusis)**")
    st.caption("0 = Tidak, 1 = Ya")
    hypoacusis = st.radio("input_hypoacusis", [0, 1], label_visibility="collapsed")

    st.markdown("**Diplopia (Penglihatan Ganda)**")
    st.caption("0 = Tidak, 1 = Ya")
    diplopia = st.radio("input_diplopia", [0, 1], label_visibility="collapsed")

    st.markdown("**Cacat Neurologis (Defect)**")
    st.caption("0 = Tidak, 1 = Ya")
    defect = st.radio("input_defect", [0, 1], label_visibility="collapsed")

    st.markdown("**Gangguan Keseimbangan (Ataxia)**")
    st.caption("0 = Tidak, 1 = Ya")
    ataxia = st.radio("input_ataxia", [0, 1], label_visibility="collapsed")

    st.markdown("**Gangguan Kesadaran (Conscience)**")
    st.caption("0 = Tidak, 1 = Ya")
    conscience = st.radio("input_conscience", [0, 1], label_visibility="collapsed")

    st.markdown("**Parestesia**")
    st.caption("0 = Tidak, 1 = Ya")
    paresthesia = st.radio("input_paresthesia", [0, 1], label_visibility="collapsed")

    st.markdown("**DPF (Penyempitan Kelopak Mata)**")
    st.caption("0 = Tidak, 1 = Ya")
    dpf = st.radio("input_dpf", [0, 1], label_visibility="collapsed")

    submitted = st.form_submit_button("Klasifikasi Migrain")

if submitted:
    user_data = [[age, duration, frequency, location, character, intensity, nausea, vomit,
                  phonophobia, photophobia, visual, sensory, dysphasia, dysarthria, vertigo,
                  tinnitus, hypoacusis, diplopia, defect, ataxia, conscience, paresthesia, dpf]]
    prediction = model.predict(user_data)
    st.success(f"✅ Jenis migrain yang diprediksi: **{prediction[0]}**")
