link : https://salsabila-salimah-meowlfootball.pbp.cs.ui.ac.id/

1. Mengapa kita memerlukan data delivery dalam implementasi sebuah platform?
= Kita memerlukan data delivery untuk mengirimkan data dari satu komponen ke komponen lain dalam sebuah sistem. Ini penting karena aplikasi web modern sering kali terdiri dari berbagai bagian yang terpisah, seperti frontend (antarmuka pengguna) dan backend (server). Data delivery memungkinkan data dari backend disajikan kepada pengguna di frontend atau sebaliknya, serta memungkinkan komunikasi antar layanan yang berbeda. Contohnya, saat menambahkan berita baru di sebuah situs, data berita tersebut perlu dikirim dari browser (frontend) ke server (backend) untuk disimpan.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
= Berdasarkan langkah yang sudah saya jalani, JSON lebih unggu;l/baik daripada XML, karena JSON sintaksnya lebih ringkas dan lebih mudah dibaca oleh manusia dan diurai (parse) oleh mesin, JSON menggunakan pasangan kunci-nilai (key-value pairs) yang mirip dengan objek JavaScript, sehingga sangat mudah diintegrasikan dengan aplikasi web yang menggunakan JavaScript. Meskipun XML bersifat self-descriptive dengan tag-nya, JSON juga self-descriptive melalui nama kunci yang jelas, tetapi tanpa overhead dari closing tags yang membuat ukuran data menjadi lebih besar. Secara umum, JSON lebih efisien untuk pertukaran data.

3. Jelaskan fungsi dari metode is_valid() pada form Django dan mengapa kita membutuhkan metode tersebut?
= Metode is_valid() pada Django Form berfungsi untuk memvalidasi data yang dikirimkan melalui form. Ketika form disubmit dengan metode POST, data tersebut diterima oleh server. Metode is_valid() akan memeriksa apakah data yang diterima, yaitu meliputi kesesuaiam dengan tipe data yang ditentukan pada model, memenuhi batasan (constraints) seperti panjang maksimum, apakah field wajib diisi, atau format data (misalnya email), Aman dari serangan seperti injeksi data.

Kita membutuhkan metode ini untuk memastikan integritas dan keamanan data sebelum menyimpannya ke database. Tanpa validasi ini, kita berisiko menyimpan data yang tidak valid, tidak lengkap, atau bahkan berbahaya, yang bisa menyebabkan error pada aplikasi atau celah keamanan

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
= karena csrf_token bekerja dengan cara menambahkan token unik dan rahasia ke setiap form. Django akan memverifikasi token ini ketika form disubmit. Jika token tidak cocok, permintaan akan ditolak. Ini memastikan bahwa permintaan POST hanya bisa dilakukan melalui form yang sah dari situs kita.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= A. Pengembangan views.py
> Mulai dengan membuat 4 fungsi baru di views.py seperti yang diminta: show_xml(), show_json(), show_xml_by_id(), dan show_json_by_id()
> Setiap fungsi akan menggunakan News.objects.all() atau News.objects.filter(pk=id) untuk mengambil data dari database.
> Kemudian, saya akan menggunakan serializers.serialize() untuk mengubah data tersebut menjadi format XML atau JSON.
> Terakhir, fungsi akan mengembalikan HttpResponse dengan data yang telah diserialisasi dan content_type yang sesuai (application/xml atau application/json).
> Untuk fungsi by-id, saya akan menambahkan try-except block untuk mengantisipasi jika ID tidak ditemukan, sehingga dapat mengembalikan respons 404 yang sesuai.
B. Pengembangan urls.py
> Setelah fungsi views selesai, buka urls.py dan mengimpor keempat fungsi baru tersebut.
> Tambahkan empat path URL baru yang mengarah ke masing-masing fungsi.
> Rute untuk fungsi by-id akan menyertakan parameter dinamis seperti <str:id>/ untuk menangkap ID berita yang diminta.
C. Pengembangan Halaman HTML
> Pastikan main.html sudah diperbarui untuk menampilkan daftar berita dengan tombol + Add News dan tombol Read More yang mengarah ke halaman detail.
> Buat create_news.html yang berisi form untuk menambahkan berita baru dan memastikan {% csrf_token %} ada di dalamnya.
> Buat news_detail.html untuk menampilkan detail berita secara lengkap.
D. Pengujian Lokal
> Jalankan server Django dengan python manage.py runserver.
> Uji setiap fitur secara manual. Saya akan coba menambahkan data baru melalui form (/create-news/), lalu memastikan data tersebut muncul di halaman utama.
> Selanjutnya klik Details untuk memastikan halaman detail berita berfungsi.
> Terakhir, uji keempat URL API (/xml/, /json/, /xml/1/, /json/1/) di browser dan Postman untuk memastikan data dikembalikan dalam format yang benar.
E. Dokumentasi dan GitHub:
> Akses URL API di Postman seperti yang diminta, mengambil tangkapan layar, dan menyertakannya di README.md.
> Setelah semua langkah selesai dan teruji, saya akan melakukan git add, git commit, dan git push ke repositori GitHub untuk menyelesaikan tugas.
6. Apakah ada feedback untuk asisten dosen tutorial 2 yang telah kamu kerjakan sebelumnya?
= tidak ada