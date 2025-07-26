# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan perguruan yang telah beroperasi sejak tahun 2000, dengan reputasi yang sangat baik dalam mencetak lulusan berkualitas. Namun, di balik kesuksesan tersebut, institusi ini menghadapi tantangan signifikan berupa tingginya angka siswa yang tidak menyelesaikan pendidikan (dropout). Hal ini tidak hanya berpengaruh pada citra institusi tetapi juga berdampak pada efektivitas program pendidikan dan keberlanjutan institusi dalam jangka panjang.

Pihak manajemen Jaya Jaya Institut menyadari pentingnya mengidentifikasi sedini mungkin siswa yang berisiko dropout untuk memberikan intervensi yang tepat sasaran. Dalam era digital dan analitik data saat ini, institusi pendidikan perlu memanfaatkan teknologi berbasis data untuk mengoptimalkan proses pembelajaran dan meningkatkan tingkat keberhasilan siswa. Melalui implementasi solusi analitik data dan kecerdasan buatan, Jaya Jaya Institut berharap dapat secara proaktif memitigasi risiko dropout dan meningkatkan angka kelulusan.

### Permasalahan Bisnis

**1. Tingginya Tingkat Dropout Siswa**  
Jaya Jaya Institut menghadapi masalah serius dengan jumlah siswa yang meninggalkan studi sebelum menyelesaikan program pendidikan. Hal ini merugikan tidak hanya bagi siswa tetapi juga bagi reputasi dan keberlanjutan operasional jangka panjang institusi.

**2. Minimnya Pemahaman Faktor Penyebab Dropout**  
Belum adanya analisis komprehensif untuk memahami pola dan faktor penentu yang mempengaruhi keputusan siswa untuk meninggalkan studi, sehingga program intervensi yang ada tidak tepat sasaran.

**3. Keterbatasan Sistem Deteksi Dini**  
Institusi belum memiliki mekanisme efektif untuk mengidentifikasi siswa yang berisiko dropout pada tahap awal. Akibatnya, intervensi akademik dan dukungan yang diperlukan tidak dapat diberikan tepat waktu, sehingga peluang untuk mempertahankan siswa menjadi sangat rendah.

**4. Ketiadaan Sistem Monitoring yang Efektif**  
Tidak ada sistem yang memadai untuk memonitor dan menganalisis status akademik siswa secara real-time, yang menghambat pengambilan keputusan berbasis data untuk mencegah dropout.

**5. Kurangnya Instrumen Prediktif dalam Pengambilan Keputusan**  
Pengambilan keputusan terkait program retensi siswa masih mengandalkan pendekatan reaktif dan kurang didukung oleh analisis data prediktif yang dapat mengantisipasi risiko dropout.

### Cakupan Proyek

**1. Eksplorasi dan Analisis Dataset Performa Siswa**  
   Melakukan analisis mendalam terhadap dataset "students' performance" yang disediakan oleh Jaya Jaya Institut untuk mengidentifikasi pola dan indikator utama yang berkorelasi dengan perilaku dropout.

**2. Pengembangan Model Prediktif Dropout**  
   Merancang dan melatih model machine learning yang dapat memprediksi siswa dengan risiko dropout tinggi berdasarkan berbagai parameter dari dataset, seperti performa akademik, kehadiran, demografi, dan faktor perilaku lainnya.

**3. Pengembangan Dashboard Interaktif untuk Monitoring**  
   Mengembangkan dashboard interaktif yang memungkinkan pihak Jaya Jaya Institut untuk memantau status akademik siswa secara visual. Dashboard ini membantu dalam mengidentifikasi siswa dengan risiko tinggi untuk dropout, serta melihat tren terkait performa akademik.

**4. Pengembangan Prediksi Web-Based Application**  
   Membangun aplikasi berbasis Streamlit yang memungkinkan pihak manajemen dan pegajar untuk memasukkan data siswa secara langsung dan mendapatkan prediksi status siswa serta informasi performa secara keseluruhan. Aplikasi ini mempermudah pengguna untuk mengakses model dan insight yang telah dikembangkan.

**5. Penyusunan Rekomendasi Strategis**  
   Berdasarkan analisis data dan hasil prediksi, menyusun rekomendasi langkah-langkah yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan tingkat kelulusan siswa.

### Persiapan

#### **Sumber Data**  
Data yang digunakan dalam proyek ini dapat diakses melalui link berikut: [Dataset Siswa Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

#### **Setup environment**
Proyek ini dikembangkan menggunakan bahasa pemrograman Python dan beberapa library populer untuk keperluan analisis data, pemrosesan fitur, penanganan data imbalance, serta pengembangan dan evaluasi model machine learning. Selain itu, Tableau digunakan untuk membangun dashboard visualisasi interaktif yang mendukung analisis secara real-time.

**1. Tools & Teknologi yang Digunakan**  
   - **Python** – Bahasa pemrograman untuk analisis data dan pengembangan model prediktif.
   - **Jupyter Notebook** atau **Google Colab** – Digunakan untuk menjalankan dan mengembangkan analisis data.
   - **Streamlit** – Untuk membangun prototype dashboard prediktif yang bisa dijalankan secara lokal maupun di cloud.
   - **Tableau** – Untuk membuat dashboard visualisasi interaktif dari data yang dianalisis.

**2. Library Python yang Digunakan**  
Proyek ini menggunakan beberapa library Python populer untuk analisis data, machine learning, dan visualisasi, antara lain:  
   - **`numpy`, `pandas`** – Untuk manipulasi dan analisis data.
   - **`matplotlib`, `seaborn`** – Untuk visualisasi eksploratif.
   - **`scikit-learn`** – Untuk preprocessing data, modeling, dan evaluasi model.
   - **`imbalanced-learn`** – Untuk menangani dataset yang imbalance dengan teknik seperti SMOTEENN.
   - **`joblib`** – Untuk menyimpan dan memuat model.
   - **`streamlit`** – Untuk membangun aplikasi berbasis web.
   - **`warnings`, `time`** – Modul built-in untuk logging dan kontrol eksekusi.

**3. Membuat Virtual Environment**  
Sebelum menginstal dependensi, sangat disarankan untuk membuat *virtual environment* untuk memisahkan dependensi proyek ini. Berikut cara membuat dan mengaktifkan *virtual environment* menggunakan Python:

   - **Membuat Virtual Environment**  
      Jalankan perintah berikut di terminal atau command prompt untuk membuat *virtual environment*:
      ```bash
      python -m venv .venv
      ```

   - **Mengaktifkan Virtual Environment**
      - **Windows:**
         ```bash
         .venv\Scripts\activate
         ```
      - **macOS/Linux:**
         ```bash
         source .venv/bin/activate
         ```

**4. Instalasi Library**  
Setelah virtual environment diaktifkan, install semua dependensi yang diperlukan untuk proyek ini.
   - **Menggunakan `requirements.txt`**      
      Jika sudah ada file requirements.txt yang disediakan, jalankan perintah berikut untuk menginstal semua dependensi:
      ```bash
      pip install -r requirements.txt 
      ```
   - **Tanpa file `requirements.txt`**  
      Jika tidak ada file requirements.txt, Anda bisa menginstal library satu per satu:  
      ```bash
      pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn joblib streamlit
      ```
**6. Mengakses Tableau**  
   Berikut merupakan langkah untuk mengakses dashboard di Tableau Public:
   - Klik tautan berikut untuk membuka dashboard interaktif: [Link Dashboard Tableau Public](https://public.tableau.com/app/profile/karinda.amelia/viz/dashboard_students_performance/Dashboard2)  
   - Setelah itu, Anda akan diarahkan ke halaman Tableau Public untuk melihat visualisasi data secara interaktif.

**7. Mengakses Streamlit**  
   Aplikasi berbasis web yang dibangun menggunakan Streamlit dapat diakses melalui tautan berikut:
   [Link Streamlit](https://student-status.streamlit.app/)  

## Business Dashboard
Business dashboard ini dikembangkan menggunakan Tableau Public dan dirancang untuk membantu pihak institusi dalam menganalisis performa akademik siswa secara visual dan interaktif.

**1. Tujuan Pembuatan Dashboard**  
   Dashboard ini dirancang untuk:
   - Memberikan gambaran menyeluruh mengenai status akademik siswa (Dropout, Enrolled, Graduate).
   - Mengidentifikasi hubungan antara nilai akademik dengan status siswa.
   - Mengidentifikasi pola hubungan antara jumlah unit yang diambil dan tingkat penyelesaian studi.

**2. Komponen Dashboard**  
   Berikut merupakan komponen utama dari dashboard:
   - **Total of Students**:  
      Menampilkan jumlah total siswa yang dianalisis (4.424 siswa).
   - **Distribution Grade by Status**:  
      Visualisasi ini menggunakan bar chart horizontal untuk memperlihatkan perbandingan rata-rata nilai siswa berdasarkan status:
      - Avg. grade (1st – 2nd sem): menunjukkan performa nilai keseluruhan dari semester 1 sampai 2.
      - Avg. Curricular units 1st sem grade dan 2nd sem grade: memperlihatkan kualitas nilai pada masing-masing semester.
      - Dapat membantu mengidentifikasi apakah siswa dengan status dropout memiliki performa akademik yang lebih rendah dibandingkan yang lulus.
   - **Completion Ratio vs Enrolled Heatmap**:
      - Heatmap ini menggambarkan hubungan antara:
         - Jumlah unit kurikulum yang diambil (Enrolled) pada sumbu Y.
         - Rasio penyelesaian studi (Completion Ratio) pada sumbu X.
      -  Intensitas warna menggambarkan densitas/rasio keberhasilan.
   - **Filter**:
      - Pengguna dapat menyaring tampilan visualisasi berdasarkan status siswa:
         - Dropout
         - Enrolled
         - Graduate
      - Filter ini memudahkan analisis mendalam per kelompok.

**3. Link Dashboard**  
   Dashboard ini dapat diakses secara publik melalui platform Tableau Public.
   [Link Dashboard Tableau Public](https://public.tableau.com/app/profile/karinda.amelia/viz/dashboard_students_performance/Dashboard2)  

## Menjalankan Sistem Machine Learning

Berikut adalah penjelasan mengenai cara menjalankan prototype sistem machine learning berbasis Streamlit yang digunakan untuk prediksi performa siswa di Jaya Jaya Institut:

**1. Buka Streamlit Dashboard**  
   - Akses dashboard melalui link berikut: [Example Streamlit](https://student-status.streamlit.app/). 
   - Tunggu beberapa saat hingga halaman sepenuhnya ter-load.

**2. Upload Data untuk Prediksi**
   - Klik tombol "Browse files" atau drag-and-drop file berformat .CSV ke area unggahan.
   - Pastikan file CSV memiliki format kolom yang lengkap sesuai dengan yang dibutuhkan sistem.
   - Setelah data berhasil diunggah, sistem akan menampilkan:
      - Notifikasi: "File successfully uploaded!"
      - Data preview: menampilkan DataFrame dari data yang diunggah, sehingga pengguna dapat langsung melihat isi file.
   - Jika format data valid, sistem akan menampilkan tambahan notifikasi: "Prediction completed successfully!", dan disertai tabel hasil prediksi dalam bentuk DataFrame.
   - Jika file yang diunggah tidak memiliki kolom yang lengkap atau salah format, maka:
      - Akan muncul peringatan berwarna kuning dengan daftar nama kolom yang hilang.
      - Sistem akan menampilkan pesan seperti: "The following columns are missing in your uploaded file..."
      - Pengguna diminta untuk memperbaiki format file dan mengunggah ulang.

**3. Download Dataset Hasil Prediksi**
   - Setelah proses prediksi selesai, akan muncul tombol “Download Prediction Results”.
   - Klik tombol tersebut untuk mengunduh dataset hasil prediksi dalam format .CSV.

## Conclusion
Proyek ini secara komprehensif mengatasi lima permasalahan utama yang dihadapi Jaya Jaya Institut terkait dropout siswa:

**1. Mengatasi Tingginya Tingkat Dropout**
   - Dikembangkan model prediktif machine learning yang mampu mengidentifikasi siswa berisiko dropout dengan akurasi tinggi.
   - Memberikan solusi konkret untuk menurunkan angka siswa yang tidak menyelesaikan pendidikan.

**2. Memahami Faktor Penyebab Dropout**
   - Dilakukan analisis mendalam terhadap dataset performa siswa untuk mengidentifikasi pola dan indikator utama penyebab dropout.
   - Menghasilkan wawasan komprehensif tentang faktor-faktor yang mempengaruhi keputusan siswa meninggalkan studi.

**3. Mengatasi Keterbatasan Sistem Deteksi Dini**
   - Dibangun aplikasi Streamlit yang memungkinkan prediksi status siswa secara langsung.
   - Menyediakan alat analitik berbasis data untuk pengambilan keputusan yang lebih akurat.

**4. Menyelesaikan Ketiadaan Sistem Monitoring Efektif**
   - Dikembangkan dashboard interaktif Tableau untuk monitoring status akademik siswa secara visual.
   - Memungkinkan identifikasi dini siswa berisiko dropout melalui sistem monitoring real-time.

**5. Mengembangkan Instrumen Prediktif dalam Pengambilan Keputusan**
   - Beralih dari pendekatan reaktif menjadi proaktif dalam menangani risiko dropout.
   - Menggunakan analisis data prediktif untuk mengantisipasi dan mencegah dropout.

### Rekomendasi Action Items
Berdasarkan hasil analisis, berikut adalah action items yang direkomendasikan untuk Jaya Jaya Institut:

**1. Sistem Peringatan Dini untuk Mitigasi Dropout**
   - Integrasikan model prediksi dropout ke dalam sistem informasi akademik institusi.
   - Bentuk tim intervensi khusus untuk memberikan dukungan cepat kepada siswa berisiko.
   - Kembangkan protokol pendampingan personal yang terstruktur.

**2. Program Dukungan Akademik Berbasis Data**
   - Rancang program remedial yang disesuaikan berdasarkan analisis pola dropout.
   - Sediakan mentor akademik untuk siswa dengan performa akademik rendah.
   - Kembangkan modul pelatihan soft skills untuk meningkatkan motivasi dan adaptasi.

**3. Pengembangan Berkelanjutan Model Prediksi**
   - Lakukan update berkala model machine learning dengan data terbaru.
   - Bangun mekanisme umpan balik untuk kontinuitas peningkatan akurasi prediksi.
   - Selenggarakan pelatihan berkelanjutan bagi staf akademik tentang interpretasi model.

**4. Optimalisasi Sistem Pelaporan**
   - Integrasikan dashboard Tableau ke dalam sistem manajemen informasi.
   - Kembangkan laporan berkala untuk manajemen puncak.
   - Berikan akses terbatas dashboard kepada pengajar untuk monitoring siswa.

**5. Strategi Retensi Siswa Komprehensif**
   - Lakukan analisis mendalam faktor-faktor utama penyebab dropout.
   - Kembangkan program spesifik untuk mengatasi tantangan teridentifikasi.
   - Bangun sistem komunikasi responsif dengan siswa berisiko.