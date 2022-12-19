import pickle
import numpy as np
import streamlit as st
from PIL import Image

model = pickle.load(open('fetal-health.sav', 'rb'))

st.title('Prediksi Memeriksa Kesehatan Janin')

img=Image.open('fotooo.jpg')
st.image(img,  width=650)


baseline_value = st.number_input('Nilai dasar')

accelerations = st.number_input('Akselerasi')

fetal_movement = st.number_input('Gerakan janin')

uterine_contractions = st.number_input('Kontraksi Rahim')

light_decelerations = st.number_input('Deselerasi Ringan')

severe_decelerations = st.number_input('Deselerasi Parah')

prolongued_decelerations = st.number_input('Deselerasi Berkepanjangan')

abnormal_short_term_variability = st.number_input('Variabilitas jangka Pendek Yang Abnormal')

mean_value_of_short_term_variability =  st.number_input('Nilai Rata-Rata Variabilitas Jangka Pendek')

percentage_of_time_with_abnormal_long_term_variability =  st.number_input('Persentase Waktu Dengan Variabilitas Jangka Panjang Abnormal')

mean_value_of_long_term_variability = st.number_input('Nilai Rata-Rata Variabilitas Jangka Panjang')

histogram_width = st.number_input('Lebar Histogram')

histogram_min = st.number_input('Minimum Histogram')

histogram_max = st.number_input('Maksimum Histogram')

histogram_number_of_peaks = st.number_input('Jumlah Histogram Puncak')

histogram_number_of_zeroes = st.number_input('Jumlah Histogram Nol')

histogram_mode = st.number_input('Mode Histogram')

histogram_mean = st.number_input('Rata-Rata Histogram')

histogram_median = st.number_input('Median Histogram')

histogram_variance = st.number_input('Varian Histogram')

histogram_tendency = st.number_input('Kecenderungan Histogram')

fetal_diagnosis = ''

if st.button('Prediksi Kesehatan Janin'):
    fetal_prediction = model.predict([[baseline_value, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations, prolongued_decelerations, abnormal_short_term_variability, mean_value_of_short_term_variability, percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,histogram_width, histogram_min, histogram_max, histogram_number_of_peaks, histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median, histogram_variance, histogram_tendency]])

    if(fetal_prediction[0]==0):
        fetal_diagnosis = 'low risk level'
    elif(fetal_prediction[0]==1):
        fetal_diagnosis = 'medium risk level'
    else:
        fetal_diagnosis = 'high risk level'

st.success(fetal_diagnosis)
