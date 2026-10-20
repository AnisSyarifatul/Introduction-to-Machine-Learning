# Klasifikasi Pesan Spam Menggunakan Machine Learning

## Studi Kasus

Pesan spam merupakan pesan yang tidak diinginkan dan sering kali berisi promosi berlebihan, tawaran hadiah, atau tautan yang mencurigakan. Proyek ini mengembangkan program klasifikasi pesan berbasis Machine Learning menggunakan algoritma Logistic Regression untuk membedakan pesan spam dan bukan spam berdasarkan pola teks. Data pesan diolah menggunakan metode TF-IDF untuk mengubah teks menjadi representasi numerik, kemudian dibagi menjadi data latih dan data uji untuk melatih serta mengevaluasi model. Proyek ini menerapkan tahapan dasar Machine Learning sebagaimana dibahas dalam webinar *Introduction to Machine Learning*, dengan dataset contoh yang digunakan untuk keperluan pembelajaran.

## Tujuan
- Memahami alur kerja dasar Machine Learning.
- Melakukan preprocessing teks menggunakan TF-IDF.
- Melatih model klasifikasi menggunakan Logistic Regression.
- Mengevaluasi model menggunakan accuracy, precision, recall, dan F1-score.

## Teknologi
- Python
- Pandas
- Scikit-learn
- Git dan GitHub

## Fitur
- Membaca dataset pesan.
- Mengolah teks menjadi fitur numerik.
- Melatih model klasifikasi pesan.
- Mengevaluasi hasil prediksi.
- Menguji prediksi pada pesan baru.

## Struktur File
- `main.py`: program utama Machine Learning.
- `dataset.csv`: dataset pesan dan label.
- `requirements.txt`: daftar library yang dibutuhkan.
- `README.md`: dokumentasi proyek.

## Cara Menjalankan
1. Instal library menggunakan `pip install -r requirements.txt`.
2. Jalankan program menggunakan `python main.py`.

## Batasan
Dataset yang digunakan masih berupa data contoh berukuran kecil sehingga hasil evaluasi belum menggambarkan kinerja model pada pesan spam di dunia nyata. Pengembangan selanjutnya dapat menggunakan dataset yang lebih besar dan beragam.

## Pengembangan Selanjutnya
Proyek dapat dikembangkan dengan membandingkan beberapa algoritma klasifikasi, memperluas dataset, serta membuat antarmuka web untuk menguji pesan secara langsung.