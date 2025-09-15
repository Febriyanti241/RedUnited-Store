TUGAS 1
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





TUGAS 2
<!-- 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? -->
Data delivery adalah proses pengiriman data dari sumber ke tujuan secara cepat, efisien, dan aman, baik melalui batch maupun real-time. Data delivery berperan penting dalam pengimplementasian sebuah platform karena memungkinankan pengiriman data dari server ke client secara cepat dan efisien. Mekanisme ini memungkinkan developer untuk mengirim data besar dalam bebergai format seperti JSON, XML, atau HTML yang menjadikan aplikasi web lebih responsif, interaktif, dan fleksibel untuk diakses di mana saja. Dengan dukungan protokol seperti HTTP/HTTPS atau pipeline integrasi, data delivery juga membantu mengatasi tantangan terkait keamanan, akurasi, dan skalabilitas melalui enkripsi, validasi, serta pemanfaatan infrastruktur cloud yang fleksibel.
Sumber: https://www.fanruan.com/en/glossary/big-data/data-delivery

<!-- 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? -->
Menurut saya, saya lebih memilih untuk menggunakan JSON. Hal ini dikarenakan JSON menggunakan key value structure lebih mudah dibaca manusia dibandingan dengan XML yang menggunakan key value structure. Selain itu, JSON sangat cocok untuk pertukaran data dari aplikasi web modern karena terintegrasi secara alami dengan JavaScript. Parsing JSON lebih cepat dan langsung bisa digunakan sebagai objek dalam bahasa pemrograman modern sehingga lebih memudahkan developer. Maka dari itu JSON lebih populer dibandingkan dengan XML
sumber: https://www.geeksforgeeks.org/html/difference-between-json-and-xml/

<!-- 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? -->
Method is_valid() berfungsi untuk memvalidasi input user apakah sudah sesuai dengan aturan sebelum diproses lebih lanjut. Method ini juga mengantisipasi agar kita terhindar dari error saat menyimpan data ke database. Dengan demikian, aplikasi akan lebih aman dan andal karena input yang tidak valid langsung ditolak.

<!-- 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? -->
Karena csrf_token adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya dan untuk memastikan bahwa form benar benar dari halaman aplikasi sendiri, bukan dari situs lain. Jika kita tidak menambahkan csrf_token, Django tidak punya cara untuk memverifikasi asal request yang mengakibatkan form rentan terhadap Cross-Site Request Forgery dan siapapun dapat memalsukan request seolah menjadi user yang sah. Hal ini dapat dimanfaatkan oleh penyerang untuk menyamar sebagai user asli yang dapat mengakses segala data di dalam akun pengguna.

<!-- 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -->
I. Pertama, buat empat fungsi baru di views.py. Fungsinya biar data yang udah ada di database bisa ditampilkan dalam format XML atau JSON. Ada dua versi, yang nampilin semua data, dan yang nampilin data berdasarkan ID tertentu. Jadi kalau aku buka /xml/, semua data keluar dalam bentuk XML, kalau /json/1/, cuma data dengan ID 1 yang keluar dalam bentuk JSON. Untuk keempat fungsi ini diambil dari tutorial 2, namun kata "news" diubah menjadi "product"

II. Setelah view-nya jadi, sambungkan ke URL di urls.py yang ada di direktori main. Jadi aku daftarin link kayak /xml/, /json/, /xml/<id>/, dan /json/<id>/ dengan format 
path('product/<str:id>/', show_product, name='show_product'),
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'). 
Dengan begitu, fungsi yang tadi aku bikin bisa dipanggil lewat browser atau Postman dengan alamat yang jelas.

III. Kemudian, buat halaman yang isinya daftar semua data. Halaman ini dibuat pada folder main.html yang berada pada direktori main. Di halaman ini aku kasih tombol “Add Product” buat nambah data baru, dan tombol “Details” di setiap item. Jadi user bisa lihat daftar data yang ada, terus kalau mau nambah tinggal klik Add Product, kalau mau lihat detail tinggal klik Details.

IV. Buat forms.py di direktori main yang mendefinisikan atribut apa saja yang ingin ditambahkan. Waktu tombol “Add Product” diklik, user diarahkan ke halaman form. Di form ini user bisa isi data sesuai kolom yang ada di model (misalnya judul, konten, kategori, dll). Begitu disubmit, data langsung masuk ke database, lalu biasanya balik ke halaman list biar hasilnya langsung kelihatan. Setelah membuat model juga jangan lupa untuk makemigration dan migrate. 

V. Buat di view.py show_product(request, id) yang menggunakan get_object_or_404(Product, pk=id) untuk ambil objek, panggil product.increment_views() jika ada fungsi untuk menambah view count, lalu render template product_detail.html dengan konteks {'product': product}. Di template tampilkan nama produk, harga, kategori, tanggal, thumbnail dan deskripsi produk, serta tombol “Back to Product List”.

<!-- 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan? -->
Tidak ada. Tutorial sudah mempunyai intruksi yang sangat jelas dan arahan dari tim asdos juga sudah sangat membantu.

<!-- 7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md. -->
![alt text](<Screenshot 2025-09-14 231826.png>)
![alt text](<Screenshot 2025-09-14 231941.png>)
![alt text](<Screenshot 2025-09-14 232035.png>)
![alt text](<Screenshot 2025-09-14 232051.png>)