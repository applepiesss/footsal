# Footsal. 

Tautan menuju Footsal. -> [https://nadia-aisyah-footsal.pbp.cs.ui.ac.id]

## Tugas 2
1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.**
    - **Membuat sebuah proyek Django baru.**
        Saya membuat direktori baru dengan nama `footsal` dan membuat virtual environment di dalamnya. 
        Kemudian saya membuat file requirements.txt yang berisi beberapa dependencies lalu melakukan instalasi dependencies tersebut dengan perintah `pip install -r requirements.txt`. 
        Selanjutnya, saya membuat proyek Django `footsal` dengan perintah `django-admin startproject footsal .`. 
        Lalu saya membuat file `.env` dan `.env.prod` di direktori root proyek, dan memodifikasi `settings.py`. 
        kemudian, saya menambahkan dan mengubah konfigurasi `ALLOWED_HOSTS`, `PRODUCTION`, dan `DATABASES`.

    - **Membuat aplikasi dengan nama main pada proyek tersebut.**
        Saya menjalankan perintah `python manage.py startapp main` di terminal direktori root proyek.
        Kemudian saya mendaftarkan aplikasi main ke dalam proyek dengan menambahkan `main` ke dalam `INSTALLED_APPS` pada `settings.py` yang berada di direktori proyek `footsal`.

    - **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
        Saya mengubah konfigurasi `urls.py` yang di dalam direktori `footsal` dengan mengimport `from django.urls import path, include` dan menambahkan `path('', include('main.urls')),` pada `urlpatterns` supaya request URL proyek akan diarahkan ke aplikasi main.

    - **Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name, price, description, thumbnail, category, is_featured**
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

    - **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
        Saya menambahkan fungsi `show_main(request)` pada `views.py` dengan context 
        - title : Footsal.
        - name : Nadia Aisyah Fazila
        - class : PBP C
        Fungsi tersebut memiliki `return render(request, "main.html", context)` untuk render tampilan dari main.html sesuai dengan context.

    -** Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
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


    - **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
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

## Tugas 3
1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
    Kita memerlukan data delivery dalam pengimplementasian sebuah platform supaya dapat mengirimkan data dari suatu stack ke stack lainnya dengan aman dan cepat, selain itu data delivery juga dapat membantu supaya tidak terjadi bottleneck ketika traffic sedang tinggi, dan untuk membantu menjaga konsistesi pada data.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
    - Menurut saya, yang lebih baik adalah JSON karena lebih mudah dimengerti karena setiap elemennya mendeskripsikan dirinya sendiri.
    - JSON lebih populer karena mudah dibaca dan banyak bahasa pemrograman yang mendukung untuk membaca dan membuat JSON, karena walaupun syntaxnya berasal dari objek javascript, namun JSON adalah format text.

3. **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
    - Fungsi dari method `is_valid()` adalah untuk melakukan validasi apakah data yang dikirim memenuhi semua aturan validasi yang sudah ditentukan.
    - Kita butuh method `is_valid()` supaya memiliki data yang lengkap dengan format yang benar agar tidak menyebabkan inkonsistensi data dan error.

4. **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
    - Kita butuh `csrf_token` sebagai security untuk mencegah serangan berbahaya yang tidak diinginkan. 
    - Dengan tidak menambahkan `csrf_token` pada form Django, kita tidak dapat memastikan apakah request yang masuk dari pengguna atau dari penyerang.
    - Dengan tidak mengunakan `csrf_token`, penyerang dapat memaksa program untuk melakukan sesuatu atas nama pengguna.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    - **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
    Dengan menambahkan function berikut pada `views.py` 
    ```
    def show_xml(request):
        product_list = Product.objects.all()
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")

    def show_json(request):
        product_list = Product.objects.all()
        json_data = serializers.serialize("json", product_list)
        return HttpResponse(json_data, content_type="application/json")

    def show_xml_by_id(request, product_id):
        try:
            product_item = Product.objects.filter(pk=product_id)
            xml_data = serializers.serialize("xml", product_item)
            return HttpResponse(xml_data, content_type="application/xml")
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        
    def show_json_by_id(request, product_id):
        try:
            product_item = Product.objects.get(pk=product_id)
            json_data = serializers.serialize("json", [product_item])
            return HttpResponse(json_data, content_type="application/json")
        except Product.DoesNotExist:
            return HttpResponse(status=404)
    ```

    - **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.**
    Dengan melakukan import keempat function tersebut: `from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id` di `urls.py`, dan menambahkan routing sebagai berikut di urls.py juga pada `urlpatterns`:
    ```
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    ```

    - **Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.**
        - Untuk membuat tombol "Add" saya membuat file `create_product.html` dan menambahkan kode sebagai berikut di `main.html` pada direktori main/templates:
            ```
            ...
            <a href="{% url 'main:create_product' %}">
                <button>Add</button>
            </a>
            ...
            ```
        - Untuk membuat tombol "Detail" saya membuat file `product_detail.html` dan kode sebagai berikut di `main.html` pada direktori main/templates: `<a href="{% url 'main:show_product' product.id %}"><button>Detail</button></a>` 

    - **Membuat halaman form untuk menambahkan objek model pada app sebelumnya.**
    Menuliskan kode berikut pada `forms.py` untuk membuat struktur form yang dapat menerima data product baru:
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "brand"]
    ```
    Kemudian, button `Add` pada main.html tersebut akan mengarahkan ke create_product.html yang saya buat di direktori main/templates juga dengan kode:
    ```
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product" />
            </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    pada kode diatas, `{{ form.as_table }}` adalah template tag yang digunakan untuk menampilkan fields form yang sudah di buat di `forms.py` sebagai table. Setelah itu saya melakukan routing untuk URLnya dengan menambahkan `path('create-product/', create_product, name='create_product'),` di `urlpatterns` pada `urls.py` 
    Kemudian saya menambahkan kode `CSRF_TRUSTED_ORIGINS = [
    "<https://nadia-aisyah-footsal.pbp.cs.ui.ac.id>"]` di `settings.py` 

    - **Membuat halaman yang menampilkan detail dari setiap data objek model.**
    Button `Detail` pada `main.html` akan mengarahkan ke `show_product.html` yang saya buat pada direktori main/templates juga dengan isi sebagai berikut:
        ```
        {% extends 'base.html' %}
        {% block content %}
        <p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>

        {% if product.thumbnail %}
        <img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
        <br/><br />
        {% endif %}

        <h1>{{ product.name }}</h1>
        <h3>{{ product.brand }}</h3>
        <p>{{ product.description }}</p>
        <p><b>Rp{{product.price}}</b></p> 

        {% endblock content %}
        ```
        pada kode diatas, saya membuat tampilannya menjadi menampilkan detail tentang product dengan urutan thumbnail-name-brand-description-price (saya tidak menampilkan `category` dan `is_featured` karena saya ingin `category` dan `is_featured` hanya terlihat di main saja). Setelah itu saya melakukan routing untuk URLnya dengan menambahkan `path('product/<str:id>/', show_product, name='show_product'),` di `urlpatterns` pada `urls.py` 

6. **Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
    - tidak ada feedback karena para asdos membantu dengan baik pada sesi tutorial 2.

## Tugas 4
1.  **Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**
- Django AuthenticationForm adalah
- Kelebihan: mudah untuk dipahami
- Kekurangan: 


2. **Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**


3. **Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**


4. **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**


5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    -  **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.**
    - **Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.**
    - **Menghubungkan model Product dengan User.**
    - **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.**