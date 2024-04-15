# import library
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Files
with open('model_SVC.pkl', 'rb') as  file_1: 
  model_svc = pickle.load(file_1)

def run():
    # buat form imputan
    with st.form('form_default_payment'):
        limit_balance = st.number_input('Credit Limit', min_value=0.0, max_value=800000.0)
        education_level = st.selectbox('Tingkat Pendidikan', (1, 2, 3, 4), help = '1=graduate school, 2=university, 3=high school, 4=others')
        pay_0 = st.selectbox('Status Pembayaran Bulan September 2005', (1.0, 0.0, -1.0, -2.0), help = '1=Keterlambatan pembayaran, 0=Penggunaan kredit revolusioner, -1=Pembayaran tepat waktu, -2=Tidak ada penggunaan kredit')
        pay_2 = st.selectbox('Status Pembayaran Bulan Agustus 2005', (1.0, 0.0, -1.0, -2.0), help = '1=Keterlambatan pembayaran, 0=Penggunaan kredit revolusioner, -1=Pembayaran tepat waktu, -2=Tidak ada penggunaan kredit')
        pay_3 = st.selectbox('Status Pembayaran Bulan Juli 2005', (1.0, 0.0, -1.0, -2.0), help = '1=Keterlambatan pembayaran, 0=Penggunaan kredit revolusioner, -1=Pembayaran tepat waktu, -2=Tidak ada penggunaan kredit')
        pay_4 = st.selectbox('Status Pembayaran Bulan Juni 2005', (1.0, 0.0, -1.0, -2.0), help = '1=Keterlambatan pembayaran, 0=Penggunaan kredit revolusioner, -1=Pembayaran tepat waktu, -2=Tidak ada penggunaan kredit')
        pay_5 = st.selectbox('Status Pembayaran Bulan Mei 2005', (1.0, 0.0, -1.0, -2.0), help = '1=Keterlambatan pembayaran, 0=Penggunaan kredit revolusioner, -1=Pembayaran tepat waktu, -2=Tidak ada penggunaan kredit')
        pay_6 = st.selectbox('Status Pembayaran Bulan April 2005', (1.0, 0.0, -1.0, -2.0), help = '1=Keterlambatan pembayaran, 0=Penggunaan kredit revolusioner, -1=Pembayaran tepat waktu, -2=Tidak ada penggunaan kredit')
        pay_amt_1 = st.number_input('Jumlah Pembayaran Bulan September 2005', min_value = 0.0, max_value = 10000000.0)
        pay_amt_2 = st.number_input('Jumlah Pembayaran Bulan Agustus 2005', min_value = 0.0, max_value = 10000000.0)
        pay_amt_3 = st.number_input('Jumlah Pembayaran Bulan Juli 2005', min_value = 0.0, max_value = 10000000.0)
        pay_amt_4 = st.number_input('Jumlah Pembayaran Bulan Juni 2005', min_value = 0.0, max_value = 10000000.0)
        pay_amt_5 = st.number_input('Jumlah Pembayaran Bulan Mei 2005', min_value = 0.0, max_value = 10000000.0)
        pay_amt_6 = st.number_input('Jumlah Pembayaran Bulan April 2005', min_value = 0.0, max_value = 10000000.0)

        # submit button
        submitted = st.form_submit_button('Predict')

    data_inf = {
        'limit_balance':20000, 
        'education_level':2, 
        'pay_0':1.0, 
        'pay_2':-1.0, 
        'pay_3':0.0, 
        'pay_4':-2.0,
        'pay_5':-2.0, 
        'pay_6':-2.0, 
        'pay_amt_1':0, 
        'pay_amt_2':0.316, 
        'pay_amt_3':0.316, 
        'pay_amt_4':0,
        'pay_amt_5':0, 
        'pay_amt_6':0
    }

    data_inf = pd.DataFrame([data_inf])
    data_inf

    if submitted:
        # predict
        y_pred_inf = model_svc.predict(data_inf)
        # predict akan dishow sesuai hasil
        if y_pred_inf == 0:
            st.write('## Tidak terjadi default payment pada bulan berikutnya')
        else:
            st.write('## Terjadi default payment pada bulan berikutnya')

    # membuat garis pemisah
    st.markdown('---')
    
    # Kalimat penutup
    st.write("""
    Terima kasih telah menjelajahi analisis data kami menggunakan Streamlit! 
    Semoga visualisasi dan prediksi yang saya bagikan membantu Anda memahami dataset ini dengan lebih baik. 
    Jangan ragu untuk menjelajahi fitur-fitur lainnya dan saya harap Anda menemukan pengalaman yang bermanfaat.  
    Sampai jumpa pada kesempatan berikutnya!
    """)
    
# untuk running
if __name__ == '__main__':
   run()