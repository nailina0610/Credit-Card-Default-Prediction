# Import Library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# membuat title page
st. set_page_config(
    page_title= 'DEFAULT PAYMENT PREDICTION'
)

def run():
    # membuat judul
    st.title('**Default Payment Next Month Prediction**')

    # membuat subheader
    st.subheader('EDA Dataset Credit Card Default')

    # tambahkan gambar
    image = Image.open('gambar.jpg')
    st.image(image, caption = 'Abundance in every coin')

    # membuat deskripsi
    st.write('*Selamat datang di page buatan Farah. Silahkan melihat visualisasi data default payment pada halaman "EDA" dan prediksi pada halaman "Prediction"*')

    # membuat garis pemisah
    st.markdown('---')

    # membuat deskripsi dataset
    st.write('Berikut adalah Dataset Credit Card Default')
    # show dataframe
    df = pd.read_csv('P1G5_Set_1_nailina_farah.csv')
    st.dataframe(df)

    # Penjelasan Dataframe
    st.write('Dataset ini merupakan hasil query yang diambil dari bigquery public data dan terdiri dari 2965 baris data, 24 kolom dimana 20 kolom bertipe float dan 4 kolom bertipe integer')

    # VISUALISASI 1
    # Membuat dictionary untuk memetakan nama kolom asli ke nama yang ingin ditampilkan
    column_names = {
        'education_level': 'Tingkat Pendidikan',
        'pay_0': 'Repayment Status in September',
        'pay_2': 'Repayment Status in August',
        'pay_3': 'Repayment Status in July',
        'pay_4': 'Repayment Status in June',
        'pay_5': 'Repayment Status in May',
        'pay_6': 'Repayment Status in April'
    }
    # Menambahkan penjelasan untuk visualisasi
    st.write('### Visualisasi Tingkat Pendidikan dan Status Pembayaran')
    st.write('Visualisasi ini menampilkan frekuensi kategori pada kolom yang Anda pilih.')
    st.write('Anda dapat memilih kolom untuk divisualisasikan dari dropdown di bawah.')
    # Memilih kolom untuk divisualisasikan
    option = st.selectbox('Pilih kolom: ', list(column_names.values()))
    # Mengambil nama kolom asli berdasarkan nama yang ditampilkan
    selected_column = [key for key, value in column_names.items() if value == option][0]
    # Hitung frekuensi masing-masing kategori
    value_counts = df[selected_column].value_counts()
    # Buat bar plot
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(x=value_counts.index, y=value_counts.values)
    plt.xlabel(option)
    plt.ylabel('Frequency')
    plt.title('Bar Plot of ' + option)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # VISUALISASI 2
    # Menambahkan penjelasan untuk visualisasi
    st.write('### Plotly plot - Batas Limit Kredit Berdasarkan Usia')
    st.write('Visualisasi ini menampilkan hubungan antara usia dan batas limit kredit, dengan informasi tambahan saat mengarahkan kursor ke titik plot.')
    # Mengganti nilai kolom sex
    df['sex'] = df['sex'].map({1: 'male', 2: 'female'})
    # Mengganti nilai kolom education_level
    education_mapping = {
        1: 'graduate school',
        2: 'university',
        3: 'high school',
        4: 'others',
        5: 'unknown',
        6: 'unknown'
    }
    df['education_level'] = df['education_level'].map(education_mapping)
    # Membuat plotly plot
    fig = px.scatter(df, x='age', y='limit_balance', hover_data=['age', 'sex', 'education_level', 'limit_balance'])
    st.plotly_chart(fig)
    st.write('Dari scatterplot tersebut, terlihat bahwa credit limit tertinggi berada pada rentang umur sekitar 50-60 tahun.')

    # VISUALISASI 3
    # Membuat histogram usia
    st.write('## Histogram Usia')
    st.write('Visualisasi ini menunjukkan distribusi usia dari nasabah dalam dataset.')
    # Membuat histogram interaktif dengan Plotly
    fig = px.histogram(df, x='age', nbins=20, title='Distribusi Umur', barmode='overlay')
    # Menampilkan histogram interaktif
    st.plotly_chart(fig)
    st.write('Dari grafik terlihat bahwa sebagian pelanggan cukup banyak di rentang umur 20 -40 tahun. Kemudian dari 40 tahun keatas semakin bertambah usia, maka semakin berkurang frekuensinya.')

    # VISUALISASI 4
    # visualisasi limit balance berdasarkan pendidikan
    st.write('## Distribusi Limit Balance berdasarkan Pendidikan')
    st.write('Visualisasi ini menunjukkan distribusi limit balance berdasarkan tingkat pendidikan.')

    # Buat scatter plot interaktif dengan Plotly
    fig = px.scatter(df, x='education_level', y='limit_balance', title='Distribusi Limit Balance berdasarkan Pendidikan',
                    labels={'education_level': 'Tingkat Pendidikan', 'limit_balance': 'Limit Balance'})
    # Menampilkan scatter plot interaktif
    st.plotly_chart(fig)
    st.write('Terlihat bahwa limit balance paling tinggi pada kelompok university, namun nilai tersebut seperti outlier apabila dibandingkan dengan limit balance lainnya di kelompok yang sama')

    # VISUALISASI 5
    # Visualisasi jumlah peminjam berdasar status perkawinan
    st.write('## Jumlah Peminjam berdasarkan Status Perkawinan')
    st.write('Visualisasi ini menunjukkan jumlah peminjam berdasarkan status perkawinan.')
    # Ganti nilai kolom marital_status
    df['marital_status'].replace({1: 'single', 2: 'married', 3: 'other'}, inplace=True)
    # Hitung jumlah peminjam per status perkawinan
    count_by_marriage = df['marital_status'].value_counts().reset_index()
    count_by_marriage.columns = ['Status Perkawinan', 'Jumlah Peminjam']
    # Buat bar plot interaktif dengan Plotly
    fig = px.bar(count_by_marriage, x='Status Perkawinan', y='Jumlah Peminjam', title='Jumlah Peminjam berdasarkan Status Perkawinan')
    # Menampilkan bar plot interaktif
    st.plotly_chart(fig)
    st.write('Terlihat bahwa jumlah peminjam paling tinggi pada kategori married daripada single dan others, selain itu terdapat missing value karena ada nilai 0')

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