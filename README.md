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
    Klik tombol → sistem cek apakah user pemilik produk
    Kalau iya → produk dihapus dari database
    User dibalikin ke daftar produk + pesan sukses
   >Step 2: Edit Produk
    Tambahin tombol Edit di card produk
    Klik tombol → user diarahkan ke form yang sudah auto-terisi data produk lama
    User ubah data → submit → sistem validasi
    Data tersimpan → user balik ke detail/daftar produk + pesan sukses
  >Step 3: Navbar Responsive
    Navbar ditaruh di semua halaman biar konsisten
    Versi desktop: menu horizontal + logo + tombol login/logout
    Versi mobile: menu jadi hamburger, bisa di-toggle buka/tutup
    Pastikan link ke halaman utama, tambah produk, login/logout selalu ada
  >Step 4: Daftar Produk (List)
    Kalau belum ada produk: tampilkan ilustrasi/gambar + teks “Belum ada produk” + tombol buat produk
    Kalau sudah ada produk: tampilkan produk dalam bentuk card grid
    Mobile → 1 kolom
    Desktop → beberapa kolom
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
