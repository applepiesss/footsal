# Footsal. 

Tautan menuju Footsal. -> [https://nadia-aisyah-footsal.pbp.cs.ui.ac.id]

## Tugas 2
1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.**
    - Membuat sebuah proyek Django baru.
        Saya membuat direktori baru dengan nama `footsal` dan membuat virtual environment di dalamnya. 
        Kemudian saya membuat file requirements.txt yang berisi beberapa dependencies lalu melakukan instalasi dependencies tersebut dengan perintah `pip intall -r requirements.txt`. 
        Selanjutnya, saya membuat proyek Django `footsal` dengan perintah `django-admin startproject footsal .`. 
        Lalu saya membuat file `.env` dan `.env.prod` di direktori root proyek, dan memodifikasi `settings.py`. 
        kemudian, saya menambahkan dan mengubah konfigurasi `ALLOWED_HOSTS`, `PRODUCTION`, dan `DATABASES`.

    - Membuat aplikasi dengan nama main pada proyek tersebut.
        Saya menjalankan perintah `python manage.py startapp main` di terminal direktori root proyek.
        Kemudian saya mendaftarkan aplikasi main ke dalam proyek dengan menambahkan `main` ke dalam `INSTALLED_APPS` pada `settings.py` yang berada di direktori proyek `footsal`.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        Saya mengubah konfigurasi `urls.py` yang di dalam direktori `footsal` dengan mengimport `from django.urls import path, include` dan menambahkan `path('', include('main.urls')),` pada `urlpatterns` supaya request URL proyek akan diarahkan ke aplikasi main.

    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description, thumbnail, category, is_featured
        Saya membuat model pada aplikasi main dengan mengisi file `models.py` pada direktori aplikasi main dengan attributes dan tipe yaitu
        ```
            name = models.CharField(max_length=50)
            price = models.IntegerField()
            description = models.TextField()
            thumbnail = models.URLField()
            categoty = models.CharField(max_length=20)
            is_featured = models.BooleanField()
            brand = models.CharField(max_length=20)
        ``` 
        Kemudian, saya melakukan migrasi model dengan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate`.

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        Saya menambahkan fungsi `show_main(request)` pada `views.py` dengan context 
        - title : Footsal.
        - name : Nadia Aisyah Fazila
        - class : PBP C
        Fungsi tersebut memiliki `return render(request, "main.html", context)` untuk render tampilan dari main.html sesuai dengan context.

    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        Saya membuat berkas `urls.py` di dalam direktori main dan mengisinya dengan:
        ```
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
        ```
        untuk mengatur pola URL pada aplikasi main.


    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        Dengan menambahkan URL `nadia-aisyah-footsal.pbp.cs.ui.ac.id` pada `ALLOWED_HOSTS` di `settings.py` pada direktori root proyek dan melakukan push ke PWS. 

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
    [https://drive.google.com/file/d/1UQ18nhBw_0oZUQK0yE4ySzssOUmez2H8/view?usp=sharing]

3. **Jelaskan peran settings.py dalam proyek Django!**
    - untuk mengontrol konfigurasi keseluruhan proyek Django yang sesuai dengan kebutuhan, contoh:
    `DATABASE` = untuk konfigurasi database dari proyek Django
    `ALLOWED_HOST` = daftar host yang diizinkan untuk mengakses proyek Django
    `INSTALLED_APPS` = daftar aplikasi yang dapat diakses pada proyek Django  

4. **Bagaimana cara kerja migrasi database di Django?**
    - `makemigrations` melakukan perisapan untuk melakukan migrasi skema model ke dalam database Django lokal
    - `migrasi` melakukan migrasi file dan menerapkan skema yang telah dibuat ke dalam database Django lokal
    - setiap melakukan perubahan pada `models.py` harus melakukan migrasi untuk merefleksikan perubahan tersebut.  

5. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
    - karena framework Django menggunakan bahasa python yang sintaksnya lebih simple dan mudah dipahami
    - karena framework Django adalah fullstack yang lengkap, sehingga memudahkan untuk fokus building the app tanpa harus melakukan banyak konfigurasi tambahan, karena fitur-fitur penting sudah tersedia secara built in.
    - karena Django bisa dijadikan backend yang dapat dihubungkan ke aplikasi mobile. Jadi pembuatan aplikasi yang sama pada platform yang berbeda akan menjadi lebih cepat dan sederhana. 

6. **Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
    - tidak ada feedback karena para asdos membantu dengan baik pada sesi tutorial.