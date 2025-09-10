1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
I. Saya membuat direktori RedUnited-Store, lalu membuat dan mengaktifkan virtual environment dengan python -m venv env dan env\Scripts\activate. Setelah menyiapkan requirements.txt berisi dependencies (Django, gunicorn, whitenoise, psycopg2-binary, dll.), saya instal dengan pip install -r requirements.txt. Kemudian membuat proyek Django bernama redunited_store dengan django-admin startproject redunited_store ., menambahkan file .env dan .env.prod yang dihubungkan ke settings.py, lalu menjalankan migrasi database dan runserver. Halaman roket Django muncul di http://localhost:8000 sebagai tanda proyek berhasil.

II. Saya membuat aplikasi main dengan python manage.py startapp main, lalu menambahkannya ke INSTALLED_APPS di settings.py.

III & VI. Untuk routing, saya membuat urls.py di folder main dengan route ke fungsi show_main. Di urls.py proyek utama, saya menambahkan path('', include('main.urls')), sehingga halaman main dapat diakses di http://localhost:8000/.

IV & V. Di models.py, saya membuat model Product dengan atribut name, price, description, thumbnail, category, dan is_featured, lalu melakukan migrasi database. Di views.py, saya membuat fungsi show_main yang mengirim context berisi nama aplikasi, nama saya, dan kelas ke template HTML untuk ditampilkan secara dinamis.

VII. Deployment ke PWS dilakukan dengan login SSO, membuat proyek baru, menambahkan environment variables dari .env.prod, lalu menambahkan URL PWS ke ALLOWED_HOSTS. Setelah git add, commit, dan push, saya jalankan git push pws master. Jika status Running, aplikasi bisa diakses melalui URL PWS.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](<Option 1.jpg>)
urls.py: menerima request dari client lalu mencocokkan URL yang diminta. Jika cocok, diarahkan ke fungsi yang sesuai di views.py.
views.py: berisi logika utama. Di sini request diproses, data bisa diminta dari models.py, lalu dikirimkan ke template HTML untuk ditampilkan.
models.py: berhubungan langsung dengan database. Views.py akan melakukan query (baca/tulis) lewat models.py, dan hasilnya dikirim kembali ke views.
main.html (Template HTML): menerima data dari views.py melalui context, lalu menghasilkan halaman web dinamis.
Client: akhirnya menerima HTTP response berupa halaman HTML yang sudah jadi.
sumber: https://user-images.githubusercontent.com/105644250/267360412-9cb5536b-83d7-45ea-ae2b-a8abde7cde9e.png

3. Jelaskan peran settings.py dalam proyek Django!
settings.py adalah modul python yang berfungsi sebagai pusat konfigurasi untuk projek Django. Semua hal penting mulai dari database yang dipakai, aplikasi apa saja yang aktif, aturan keamanan, dan lokasi file statis diatur di sini. File ini juga bisa membaca environment variables, jadi pengembang bisa dengan mudah membedakan pengaturan untuk development dan production tanpa harus ubah-ubah kode. Karena ditulis dengan Python biasa, file ini juga fleksibel banget dan gampang disesuaikan sesuai kebutuhan proyek.
sumber: https://www.colabcodes.com/post/a-complete-guide-to-settings-py-in-django-configuration-for-your-python-web-project

4. Bagaimana cara kerja migrasi database di Django?
Migrasi di Django adalah mekanisme untuk menjaga agar struktur database selalu sesuai dengan model Python yang kita definisikan. Saat kita mengubah model (misalnya menambah field baru), kita jalankan python manage.py makemigrations untuk membuat file migrasi yang berisi instruksi perubahan. Lalu, python manage.py migrate akan mengeksekusi instruksi tersebut ke database, sehingga tabel dan kolom ikut diperbarui. Setelah migrasi selesai, Django akan membuat tabel-tabel dasar yang dibutuhkan serta menyesuaikan database sesuai model aplikasi. Django juga mencatat migrasi mana yang sudah diterapkan di tabel internal, jadi perubahan tidak dijalankan dua kali. Dengan begitu, migrasi bekerja layaknya “version control” untuk skema database, memastikan kode dan database tetap sinkron di setiap environment.
sumber: https://docs.djangoproject.com/en/5.2/topics/migrations/

5. Kenapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut artikel di Dev.to "Why Django is the Perfect Framework for Beginners and Pros Alike", ada beberapa alasan utama:
a. Fitur lengkap bawaan (batteries-included). Django sudah menyediakan banyak fitur dasar seperti autentikasi, manajemen database, dan antarmuka admin. Hal ini membuat pengembang bisa langsung fokus ke logika aplikasi tanpa repot menyiapkan hal-hal dasar terlebih dahulu.

b. Keamanan terpadu. Django dilengkapi proteksi penting terhadap SQL injection, XSS, dan clickjacking, sehingga aplikasi lebih aman secara default.

c. Skalabilitas tinggi. Django dapat digunakan untuk proyek kecil maupun besar, bahkan dipakai oleh platform populer seperti Instagram, Pinterest, dan Mozilla.

d. Mudah dipelajari. Dokumentasi yang jelas serta struktur kode yang rapi dan intuitif membuat Django ramah untuk pemula, namun tetap efisien untuk pengembang berpengalaman.

sumber: https://dev.to/codefusionlab/-why-django-is-the-perfect-framework-for-beginners-and-pros-alike-99j

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Menurut saya dokumen pada tutorial 1 sudah sangat jelas. Selain itu, asisten dosen juga telah stand by untuk mahasiswa sehingga memudahkan mahasiswa untuk bertanya jika terdapat kendala. 