import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns



st.header('COVID 19')

st.header('DASHBOARD PERSEBARAN DATA COVID-19')
data_covid = pd.read_csv("covid_19_indonesia_time_series_all.csv")
st.write(data_covid)
jumlah = data_covid.iloc[:, 7:10]
# total_kasus = jumlah.sum[:, 7, 8, 9, 10]
# total_kasus

st.header('TOTAL KASUS COVID 19')
jumlah_kasus = data_covid.iloc[:, 7]
total_kasus = jumlah_kasus.sum()
jumlah_kasus
st.write(total_kasus)

st.header('TOTAL KASUS POSITIF COVID 19')
jumlah_positif = data_covid.iloc[:, 10]
total_positif = jumlah_positif.sum()
jumlah_positif
st.write(total_positif)

st.header('TOTAL KASUS YANG MENINGGAL')
jumlah_mati = data_covid.iloc[:, 8]
total_mati = jumlah_mati.sum()
jumlah_mati
st.write(total_mati)

st.header('TOTAL KASUS YANG SELAMAT')
jumlah_selamat = data_covid.iloc[:, 9]
total_selamat = jumlah_selamat.sum()
jumlah_selamat
st.write(total_selamat)
