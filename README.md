link : https://salsabila-salimah-meowlfootball.pbp.cs.ui.ac.id/

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
= Django AuthenticationForm adalah form bawaan Django untuk menangani proses login dengan username dan password, yang sudah terhubung dengan sistem autentikasi bawaan Django sehingga validasi dan login user dapat dilakukan dengan aman. Kelebihannya adalah mudah digunakan, aman karena menggunakan mekanisme autentikasi Django, dan bisa diubah sesuai kebutuhan, sedangkan kekurangannya adalah hanya mendukung login sederhana dan perlu kustomisasi jika ingin mendukung login dengan email, 2FA, atau fitur seperti "remember me".

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
= Autentikasi adalah proses untuk memverifikasi identitas pengguna, sedangkan otorisasi adalah proses menentukan apa yang boleh dilakukan oleh pengguna tersebut. Django mengimplementasikan autentikasi melalui fungsi authenticate() dan login() yang menyimpan identitas user di session, sedangkan otorisasi dilakukan dengan sistem permission, group, dan decorator seperti @login_required atau @permission_required untuk membatasi akses ke view tertentu.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
= Cookies menyimpan data di sisi client dan cocok untuk data kecil seperti preferensi tampilan, namun rentan dicuri atau dimodifikasi jika tidak diamankan. Session menyimpan data di sisi server sehingga lebih aman untuk data sensitif, namun memerlukan penyimpanan tambahan di server dan menambah beban jika user sangat banyak.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? 
= Cookies tidak sepenuhnya aman secara default karena bisa dicuri melalui XSS, disalahgunakan melalui CSRF, atau diubah isinya jika tidak ditandatangani atau dienkripsi. Risiko ini bisa dikurangi dengan menggunakan cookie HttpOnly, Secure, SameSite, serta selalu menggunakan HTTPS.

5. Bagaimana Django menangani hal tersebut?
= Django menangani risiko tersebut dengan menyediakan session berbasis server, middleware CSRF, cookie dengan flag HttpOnly secara default, kemampuan untuk mengaktifkan Secure dan SameSite, serta memutar session ID setiap kali login agar aman dari session fixation.

6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
= Implementasi langkah demi langkah dapat dilakukan dengan merancang kebutuhan login (username atau email), membuat custom AuthenticationForm jika perlu menambah fitur seperti remember me, menggunakan login() untuk menyimpan user di session dan mengatur expiry sesuai pilihan, mengaktifkan middleware autentikasi dan CSRF di settings, serta mengamankan cookie dengan HttpOnly, Secure, dan SameSite di produksi. Setelah itu, atur permission dan group sesuai kebutuhan otorisasi, dan lakukan pengujian dengan memastikan login, logout, dan proteksi akses bekerja sesuai harapan.