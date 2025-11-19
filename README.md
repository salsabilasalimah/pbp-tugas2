1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
= CSS selector yang mengatur elemen yang sama, browser bakal menentukan prioritasnya pakai aturan yang bernama specificity. Urutannya inline style punya prioritas paling tinggi, di bawahnya ada ID selector, lalu class, attribute, dan pseudo .
class, terus terakhir baru element atau tag selector. Jika ternyata terdapat aturan yang levelnya sama, maka yang ditulis paling akhir di CSS yang dipakai. Jadi intinya, makin spesifik selektornya, makin tinggi kemungkinan dia menang untuk dipakai

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web?
= Karena kebanyakan user menggunakan web bukan hanya dari laptop atau komputer, tapi juga dari HP, tablet, bahkan smart TV. Dengan responsive design, tampilan web bisa otomatis menyesuaikan ukuran layar pengguna, jadi lebih nyaman dilihat dan dipakai. Contohnya seperti Tokopedia, di mana kita dapat buka melalui HP atau PC. Jadi. responsive design bikin pengalaman pengguna lebih baik dan juga lebih hemat tenaga karena nggak perlu bikin versi terpisah untuk tiap device

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
= Margin itu jarak antara elemen kita dengan elemen lain di luar kotaknya, border itu garis yang mengelilingi kotak elemen, sementara padding itu ruang di dalam kotak antara konten dengan border. Misalnya, kalau kita bikin card di CSS, margin bisa dipakai biar card-nya nggak mepet sama elemen lain, border bisa dipakai buat kasih garis tepi, dan padding dipakai supaya teks atau gambar di dalam card nggak mepet banget sama garis tepi. Jadi gampangnya, margin itu kayak jarak rumah dengan rumah tetangga, border itu pagar rumah, padding itu jarak antara pagar dan dinding rumah, dan konten itu isi rumahnya

4. Jelaskan konsep flexbox dan grid layout beserta kegunaannya!
= Flexbox dan grid merupakan cara untuk mengator layout halaman di CSS. Flexbox digunakan untuk mengatur elemen yang ada di satu baris atau satu kolom, jadi digunakan untuk membuat navbar, tombol yang sejajar, atau susunan card ke samping. Sementara grid biasanya dipakai untuk mengatur struktur utama halaman seerti layout majalah yang banyak kolom. Singkatnya, kalau cuma perlu ngatur satu arah aja, pakai flexbox udah cukup, tapi kalau butuh layout kompleks dengan baris dan kolom yang teratur, grid layout lebih pas.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
= >Step 1: Hapus Produk (Delete)
    Tambahin tombol Delete di setiap card produk
    Klik tombol -> sistem cek apakah user pemilik produk
    Kalau iya -> produk dihapus dari database
    User dibalikin ke daftar produk + pesan sukses
   >Step 2: Edit Produk
    Tambahin tombol Edit di card produk
    Klik tombol -> user diarahkan ke form yang sudah auto-terisi data produk lama
    User ubah data -> submit -> sistem validasi
    Data tersimpan -> user balik ke detail/daftar produk + pesan sukses
  >Step 3: Navbar Responsive
    Navbar ditaruh di semua halaman biar konsisten
    Versi desktop: menu horizontal + logo + tombol login/logout
    Versi mobile: menu jadi hamburger, bisa di-toggle buka/tutup
    Pastikan link ke halaman utama, tambah produk, login/logout selalu ada
  >Step 4: Daftar Produk (List)
    Kalau belum ada produk: tampilkan ilustrasi/gambar + teks “Belum ada produk” + tombol buat produk
    Kalau sudah ada produk: tampilkan produk dalam bentuk card grid
    Mobile -> 1 kolom
    Desktop -> beberapa kolom
    Setiap card: gambar, judul, harga, kategori, tanggal, deskripsi singkat, tombol Edit & Delete
  >Step 5: Halaman Login & Register
    Desain form simple & jelas dengan input besar, label jelas, tombol kontras
    Register punya input username + password + konfirmasi
    Login punya input username + password
    Gunakan warna konsisten (biru/indigo)
    Ada link navigasi: “Belum punya akun? Register” atau “Sudah punya akun? Login”
  >Step 6: Halaman Create & Edit Product
    Form rapi dengan label + input yang jelas
    Field yang wajib diisi ditandai
    Tombol Cancel (balik ke daftar produk) + Submit (simpan)
    Untuk edit, data lama otomatis terisi
  >Step 7: Halaman Detail Produk
    Menampilkan judul besar, gambar utama, deskripsi lengkap, kategori, dan tanggal dibuat
    Jika pemilik produk, tombol Edit dan Delete juga muncul
    Tata letak rapi dengan card/detail box
  >Step 8: Validasi & Izin
    Form dicek: nama produk wajib, harga angka, deskripsi tidak kosong
    User lain tidak bisa edit/delete produk yang bukan miliknya
    Kalau ada error input, tampilkan pesan error di bawah field
  >Step 9: Styling & Static Assets
    Warna konsisten (misal biru/indigo + putih)
    Gunakan Tailwind untuk card, tombol, form, navbar
    Tambahin ilustrasi di empty state
    Animasi hover di tombol & card


>> TUGAS 6

1. Apa perbedaan antara *synchronous request* dan *asynchronous request*?
* Synchronous Request (Sinkron): Prosesnya "memblokir" (blocking). Saat browser mengirim permintaan, pengguna tidak bisa melakukan apa pun di halaman tersebut—tidak bisa klik, tidak bisa scroll. Browser akan diam menunggu sampai server mengirimkan kembali satu halaman HTML utuh yang baru, lalu memuat ulang (reload) seluruh halaman. Ini seperti menelepon; Anda harus menunggu sampai panggilan selesai sebelum bisa melakukan hal lain.

* Asynchronous Request (Asinkron): Prosesnya "tidak memblokir" (non-blocking). Saat browser (melalui JavaScript) mengirim permintaan, itu dilakukan di latar belakang. Pengguna bisa tetap berinteraksi dengan halaman. Ketika server mengirim balasan (biasanya data kecil seperti JSON), hanya bagian tertentu dari halaman yang diperbarui oleh JavaScript tanpa perlu reload seluruh halaman. Ini seperti mengirim pesan WhatsApp; Anda bisa melanjutkan aktivitas lain setelah mengirim pesan dan akan mendapat notifikasi saat balasan tiba.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
a.  Pemicu di Frontend: Pengguna melakukan aksi di halaman web (misalnya, mengklik tombol "Create Product").
b.  JavaScript Mengirim Request: Fungsi `fetch()` di JavaScript mengirimkan permintaan ke URL spesifik di server Django (misalnya, `/add-product-ajax/`) di latar belakang.
c.  Django Menerima Request (`urls.py`): File `urls.py` menerima URL tersebut dan mencocokkannya dengan fungsi *view* yang telah ditentukan.
d.  View Memproses Request (`views.py`): Fungsi *view* yang sesuai (misalnya `add_product_ajax`) dijalankan. Fungsi ini melakukan tugasnya di backend, seperti memvalidasi data dan menyimpannya ke database.
e.  View Mengirim `JsonResponse`: Alih-alih merender template HTML, *view* ini mengembalikan `JsonResponse`—sebuah paket data ringan yang berisi informasi status (misalnya, `{'status': 'success'}`).
f.  JavaScript Menerima Data: Fungsi `fetch()` di browser menerima data JSON tersebut dari Django.
g.  JavaScript Memperbarui Halaman: Berdasarkan data yang diterima, JavaScript secara dinamis mengubah tampilan halaman—misalnya, menampilkan notifikasi *toast* dan memuat ulang daftar produk tanpa me-refresh halaman.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
* Pengalaman Pengguna (UX) Lebih Baik: Website terasa jauh lebih cepat dan responsif karena tidak ada lagi jeda atau "kedipan" layar akibat reload halaman penuh untuk setiap aksi.
* Efisiensi Bandwidth dan Server: AJAX hanya mentransfer data yang diperlukan (JSON), yang ukurannya jauh lebih kecil daripada file HTML lengkap. Ini mengurangi beban server dan menghemat penggunaan data bagi pengguna.
* Pemisahan Tugas (Separation of Concerns): Kode menjadi lebih rapi. Backend (Django) dapat fokus berfungsi sebagai penyedia data (API), sementara Frontend (JavaScript) fokus pada cara data tersebut ditampilkan kepada pengguna.
* Interaktivitas Modern: Memungkinkan pembuatan fitur-fitur interaktif seperti *live search*, *auto-saving* pada form, notifikasi *real-time*, dan *infinite scroll*.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
* Gunakan HTTPS: Ini wajib. Semua data login dan register harus dikirim melalui koneksi terenkripsi (HTTPS) untuk mencegah pencurian data.
* Proteksi CSRF (Cross-Site Request Forgery): Request `POST` melalui AJAX harus menyertakan CSRF token. Caranya adalah dengan mengambil token dari cookie yang disediakan Django dan menambahkannya ke *header* request `fetch()`.
* Validasi Sisi Server (Server-Side Validation): Jangan pernah percaya pada validasi yang dilakukan di frontend (JavaScript). Semua validasi—seperti apakah username sudah ada, apakah format email benar, atau apakah password cukup kuat—harus selalu dilakukan kembali di sisi server (`views.py`) menggunakan form Django (`AuthenticationForm`, `UserCreationForm`).
* Proteksi XSS (Cross-Site Scripting): Saat menampilkan pesan error dari server (misalnya, "Username sudah terpakai"), pastikan untuk menampilkannya di frontend menggunakan `.textContent`, bukan `.innerHTML`, untuk mencegah eksekusi skrip jahat.


5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
* Terasa Instan: Setiap tindakan pengguna (menyukai, berkomentar, menambah produk) terasa seketika karena responsnya muncul tanpa menunggu halaman dimuat ulang.
* Alur yang Tidak Terputus: Pengguna tidak kehilangan konteks atau posisi mereka di halaman. Jika sedang scroll jauh ke bawah dan melakukan aksi, mereka akan tetap di posisi yang sama, tidak dilempar kembali ke atas halaman.
* Umpan Balik Langsung: Pengguna segera mendapatkan konfirmasi visual atas tindakan mereka, misalnya melalui notifikasi *toast* ("Produk berhasil ditambahkan!") atau pesan error yang muncul di tempat.
* Mengurangi Beban Kognitif: Dengan hanya memperbarui bagian kecil dari halaman, pengguna tidak perlu memproses ulang seluruh tata letak halaman setiap saat, membuat website terasa lebih ringan dan mudah digunakan.
