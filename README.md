<<<<<<< HEAD
=======
link : https://salsabila-salimah-meowlfootball.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> Membuat folder baru sebagai root yaitu pbp-tugas2
> Membuat Virtual Environment
 - python -m venv env
> Mengaktifkan Virtual Environment
 - env\Scripts\activate
> Menginstall dependencies dan start django project
 - Tulis dependencies yang dibutuhkan di file requirements.txt
 - Jalankan pip install -r requirements.txt untuk menginstal semua dependencies
 - Jalankan django-admin startproject meowl_store untuk memulai Django dengan nama  meowl_store
> Konfigurasi Environment Variables
 - Buat file '.env' di direktori root
 - Tulis 'PRODUCTION=False' di dalam file .env
 - Buat file .env.prod.
 - Tulis konfigurasi database di dalam .env.prod dengan 'PRODUCTION=True' dan 'SCHEMA=tugas_individu'
> Konfigurasi settings.py
 - Modifikasi file settings.py dan tambahkan string pada 'ALLOWED_HOSTS = ["localhost", "127.0.0.1"]'
 - Tulis di atas code DEBUG, PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
 - Mengganti database konfigurasi untuk menggunakan PostgreSQL dengan kredensials dari environment variables
> Membuat main app di project
 - python manage.py startapp main
 - tambahkan 'main' to INSTALLED_APPS di settings.py
> Membuat models
 - Product model berisi nama, price, description, thumbnail, category, is_featured
> Menjalankan server
 - python manage.py migrate
 - python manage.py runserver
> Membuat views dan template 
 - import render pada views.py
 - Buat fungsi bernama show_main, siapkan data di dalam context, dan kirimkan render sebagai respons
 - Buat folder templates di dalam main, lalu buat file main.html di dalamnya
 - Tampilkan data dengan membuat variabel template untuk menampilkan nilai yang sudah dikirimkan dari context
> Konfigurasi Routing URL 
 - Buka file urls.py yang ada di dalam folder main dan sesuaikan urlpatterns
 - Buka file urls.py yang ada di dalam direktori proyek meowl_store
 - Tambahkan include pada bagian import
 - Tambahkan path('', include('main.urls')) ke urlpatterns
 > Unit Testing
 - Buat file tests.py di dalam folder main
 - Impor TestCase, Client, dan News
 - Tambahkan fungsi-fungsi pengujian 
 - Jalankan python manage.py test di terminal
 > Deploy dengan PWS
 - Buat proyek baru di PWS
 - Tambahkan URL deployment PWS ke ALLOWED_HOSTS di settings.py
 - Jalankan perintah git add, git commit, dan git push.
 - Jalankan perintah yang terdaftar di PWS Project Command
 - Jalankan git push pws master
 - Lihat situs web di URL deployment PWS

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="731" height="869" alt="image" src="https://github.com/user-attachments/assets/3350b7aa-cf9b-450a-a789-a1fd59199f43" />

Penjelasan: 
Bagan tersebut menggambarkan alur kerja permintaan (request) dan respons (response) dalam framework Django dengan menggunakan pola MVT (Model–View–Template). Ketika seorang user mengirimkan permintaan, permintaan tersebut pertama kali masuk ke urls.py yang ada di tingkat proyek. File ini bertugas meneruskan permintaan ke urls.py di dalam aplikasi (main), untuk kemudian diarahkan ke fungsi yang sesuai di views.py. Pada tahap ini, views.py berperan dalam memproses logika aplikasi. Apabila dibutuhkan data dari database, maka views.py akan meminta model melalui models.py. Selanjutnya, models.py menjadi perantara antara logika aplikasi dan database; ia menerima permintaan dari views.py, mengakses database untuk mendapatkan data yang diminta, lalu mengembalikannya kepada views.py.

Setelah data tersedia, views.py akan mengolah data tersebut dan mengirimkannya ke berkas template, dalam hal ini main.html. Template bertugas menampilkan data dalam bentuk yang dapat dipahami oleh user. Hasil akhir berupa halaman HTML tersebut kemudian dikirimkan kembali kepada user sebagai respons. Dengan demikian, alur pada bagan ini memperlihatkan bagaimana Django mengatur hubungan antara URL, logika aplikasi, model data, dan tampilan, sehingga setiap permintaan dari user dapat diproses secara terstruktur hingga menghasilkan tampilan yang sesuai.

3. Jelaskan peran settings.py dalam proyek Django!
= settings.py merupakan pusat kendali yang menyimpan semua konfigurasi. File ini digunakan untuk menentukan aplikasi yang aktif (INSTALLED_APPS), middleware (termasuk WhiteNoise untuk static files), konfigurasi template, database (development SQLite, production dapat diarahkan ke PostgreSQL melalui environment variables), pengelolaan static files (STATIC_ROOT, STATICFILES_STORAGE), serta aspek keamanan seperti SECRET_KEY, DEBUG, dan ALLOWED_HOSTS. settiings.py ini memastikan seluruh aplikasi yang digunakan pada proyek user melalui INSTALLED_APPS dankredensialnya.

4. Bagaimana cara kerja migrasi database di Django?
Django sering dijadikan sebagai permulaan dalam pembelajaran pengembangan perangkat lunak karena menggunakan bahasa Python yang sederhana, mudah dipahami, dan banyak digunakan di berbagai bidang. Framework ini juga telah menyediakan beragam fitur bawaan, sehingga pemula tidak perlu direpotkan dengan konfigurasi yang rumit sejak awal. Selain itu, Django menerapkan arsitektur MVT (Model–View–Template) yang membantu dalam memahami pemisahan tanggung jawab di dalam aplikasi. Model berfungsi untuk mengatur data serta berhubungan langsung dengan database, View berperan dalam mengelola logika aplikasi sesuai permintaan pengguna, sedangkan Template bertugas menampilkan data dalam bentuk antarmuka yang dapat dipahami pengguna. Dengan pola tersebut, pembelajar pemula dapat memperoleh gambaran menyeluruh mengenai bagaimana sebuah aplikasi web bekerja secara terstruktur, sekaligus mempraktikkan prinsip-prinsip baik dalam pengembangan perangkat lunak modern.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
= Django sering dijadikan permulaan belajar karena dia pakai Python yang mudah dipahami, strukturnya rapi, dan sudah menyediakan banyak fitur bawaan seperti autentikasi, ORM, dan admin panel. Jadi pemula bisa langsung belajar konsep inti pengembangan perangkat lunak tanpa ribet setting ini-itu. Selain itu, Django juga ngajarin praktik baik dalam membangun aplikasi, sehingga cocok jadi fondasi awal sebelum coba framework lain yang lebih kompleks.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
= tidak ada, terima kasih kaka asdos semoga sukses dan sehat selalu
>>>>>>> d9389e5efd43284a70203084ca64cc9528230b42
