
# Klasifikasi Pesan Spam Menggunakan Machine Learning

## Studi Kasus

Pesan spam merupakan pesan yang tidak diinginkan dan sering kali berisi promosi berlebihan, tawaran hadiah, atau ajakan mengakses tautan yang mencurigakan. Proyek ini mengembangkan program klasifikasi pesan berbasis Machine Learning menggunakan algoritma Logistic Regression untuk membedakan pesan spam dan bukan spam berdasarkan pola teks.

Program menggunakan metode TF-IDF (Term Frequency-Inverse Document Frequency) untuk mengubah teks menjadi representasi numerik yang dapat diproses oleh model Machine Learning. Selanjutnya, dataset dibagi menjadi data latih dan data uji untuk melatih serta mengevaluasi model.

Proyek ini merupakan penerapan dasar Machine Learning dalam pengolahan teks atau Natural Language Processing (NLP), dengan dataset contoh yang digunakan untuk keperluan pembelajaran.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Pandas** — membaca dan mengolah dataset.
- **Scikit-learn** — membangun, melatih, dan mengevaluasi model Machine Learning.
- **TF-IDF Vectorizer** — mengubah teks menjadi representasi numerik.
- **Logistic Regression** — algoritma klasifikasi pesan.
- **Visual Studio Code** — lingkungan pengembangan program.
- **Git dan GitHub** — pengelolaan kode dan dokumentasi proyek.

## Algoritma dan Metode

### 1. TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF merupakan metode yang digunakan untuk mengubah teks menjadi nilai numerik berdasarkan tingkat kepentingan kata dalam suatu dokumen dibandingkan dengan keseluruhan dokumen pada dataset.

Dalam proyek ini, TF-IDF membantu model mengenali pola kata yang terdapat dalam pesan spam maupun bukan spam.

### 2. Logistic Regression

Logistic Regression merupakan algoritma Machine Learning yang dapat digunakan untuk klasifikasi. Pada proyek ini, algoritma tersebut mempelajari hubungan antara fitur teks dan label pesan untuk memprediksi apakah suatu pesan termasuk spam atau bukan spam.

### 3. Evaluasi Model

Model dievaluasi menggunakan beberapa metrik:

- **Accuracy:** persentase seluruh prediksi yang benar.
- **Precision:** ketepatan prediksi pada suatu kelas.
- **Recall:** kemampuan model mengenali data yang benar-benar termasuk dalam suatu kelas.
- **F1-score:** rata-rata harmonis antara precision dan recall.

Metrik tersebut digunakan untuk memberikan gambaran mengenai hasil klasifikasi model pada data uji.

## Dataset

Dataset disimpan dalam file `dataset.csv` dan berisi 12 contoh pesan dengan dua kategori, yaitu `spam` dan `bukan_spam`.

### Struktur Dataset

| Atribut | Keterangan |
|---|---|
| `pesan` | Isi teks pesan yang akan diklasifikasikan. |
| `label` | Kategori pesan, yaitu spam atau bukan_spam. |

### Contoh Dataset

```csv id="2z0m3f"
pesan,label
"Selamat! Anda memenangkan hadiah gratis",spam
"Klik link ini untuk mendapatkan uang",spam
"Promo spesial, klaim hadiah sekarang",spam
"Anda mendapatkan bonus besar hari ini",spam
"Menangkan hadiah dengan mengisi formulir",spam
"Halo, apakah tugas kuliah sudah selesai",bukan_spam
"Besok kita ada jadwal praktikum",bukan_spam
"Jangan lupa mengumpulkan laporan hari ini",bukan_spam
"Terima kasih atas bantuanmu kemarin",bukan_spam
"Nanti kita bertemu di kampus",bukan_spam
"Transfer uang sekarang untuk hadiah",spam
"Ayo belajar bersama di perpustakaan",bukan_spam
```

**Catatan:** Dataset tersebut merupakan data contoh untuk pembelajaran. Pola pesan di dalamnya belum mewakili seluruh variasi pesan spam dan pesan normal di dunia nyata.

## Fitur Program

### 1. Membaca Dataset

Program membaca data pesan dan label dari file `dataset.csv` menggunakan Pandas.

### 2. Menampilkan Distribusi Label

Program menampilkan jumlah data pada setiap kategori untuk mengetahui distribusi pesan spam dan bukan spam dalam dataset.

### 3. Preprocessing Teks Menggunakan TF-IDF

Teks diubah menjadi fitur numerik menggunakan `TfidfVectorizer` agar dapat dipelajari oleh algoritma klasifikasi.

### 4. Melatih Model

Model Logistic Regression dilatih menggunakan data latih yang berasal dari pembagian dataset.

### 5. Mengevaluasi Model

Program membandingkan hasil prediksi pada data uji dengan label sebenarnya, kemudian menampilkan accuracy dan classification report.

### 6. Memprediksi Pesan Baru

Program menguji model menggunakan contoh pesan baru dan menampilkan prediksi kategori untuk setiap pesan.

## Alur Kerja Program

1. Membaca dataset pesan dari `dataset.csv`.
2. Menampilkan jumlah data dan distribusi label.
3. Memisahkan teks sebagai fitur input (`X`) dan label sebagai target (`y`).
4. Membagi dataset menjadi data latih sebesar 75% dan data uji sebesar 25%.
5. Mengubah teks menjadi fitur numerik menggunakan TF-IDF.
6. Melatih model Logistic Regression menggunakan data latih.
7. Melakukan prediksi terhadap data uji.
8. Mengevaluasi model menggunakan accuracy dan classification report.
9. Menguji model pada pesan baru.
10. Menampilkan hasil klasifikasi pesan.

## Struktur Folder

```text id="7jv1qn"
klasifikasi-pesan-spam/
├── main.py
├── dataset.csv
├── requirements.txt
└── README.md
```

Keterangan:

- `main.py`: kode utama untuk melatih dan menjalankan model klasifikasi.
- `dataset.csv`: dataset teks pesan beserta labelnya.
- `requirements.txt`: daftar library Python yang diperlukan.
- `README.md`: dokumentasi proyek.

## Contoh Penggunaan

Program akan menampilkan informasi dataset, hasil evaluasi model, dan prediksi untuk pesan baru.

Contoh pesan yang diuji:

```text id="n4z2vk"
PREDIKSI PESAN BARU

Pesan: Selamat, Anda memenangkan hadiah gratis
Prediksi: spam

Pesan: Besok kita belajar bersama di kampus
Prediksi: bukan_spam
```

**Catatan:** Contoh di atas merupakan ilustrasi format output. Hasil aktual ditentukan oleh model setelah dilatih menggunakan dataset.

## Batasan Proyek

- Dataset hanya terdiri dari 12 pesan sehingga belum cukup mewakili variasi pesan spam dan bukan spam.
- Model hanya mempelajari pola teks yang tersedia pada data pelatihan.
- Pesan dengan kata-kata baru atau pola berbeda dapat menghasilkan prediksi yang kurang tepat.
- Nilai evaluasi pada data uji yang sangat sedikit dapat berubah secara signifikan.
- Klasifikasi pesan tidak menjamin bahwa seluruh pesan berbahaya dapat terdeteksi.

Oleh karena itu, model ini ditujukan sebagai proyek pembelajaran, bukan sebagai sistem penyaring spam yang siap digunakan dalam skala produksi.

## Kesimpulan

Proyek ini menerapkan Machine Learning untuk mengklasifikasikan pesan spam dan bukan spam menggunakan algoritma Logistic Regression dengan ekstraksi fitur TF-IDF. Program mencakup proses pembacaan dataset, pengolahan teks, pelatihan model, evaluasi performa, dan prediksi terhadap pesan baru.

Melalui proyek ini, pengguna dapat memahami dasar penerapan Natural Language Processing dan Machine Learning untuk klasifikasi teks. Pengembangan lebih lanjut dengan dataset yang lebih besar dan beragam diperlukan agar model dapat dievaluasi secara lebih andal.