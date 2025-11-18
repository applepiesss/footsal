# Footsal. ⚽️

Nama: Nadia Aisyah Fazila
NPM: 2406495584
Kelas: PBP-C

Tautan menuju Footsal. -> [https://nadia-aisyah-footsal.pbp.cs.ui.ac.id]

## Tugas 2 👩‍💻
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
        Fungsi tersebut memiliki `return render(request, "main.html", context)` untuk render tampilan dari `main.html` sesuai dengan context.

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
    - Untuk mengontrol konfigurasi keseluruhan proyek Django yang sesuai dengan kebutuhan, contoh:
    `DATABASE` = untuk konfigurasi database dari proyek Django
    `ALLOWED_HOST` = daftar host yang diizinkan untuk mengakses proyek Django
    `INSTALLED_APPS` = daftar aplikasi yang dapat diakses pada proyek Django  

4. **Bagaimana cara kerja migrasi database di Django?**
    - `makemigrations` melakukan perisapan untuk melakukan migrasi skema model ke dalam database Django lokal
    - `migrate` melakukan migrasi file dan menerapkan skema yang telah dibuat ke dalam database Django lokal
    - setiap melakukan perubahan pada `models.py` harus melakukan migrasi untuk merefleksikan perubahan tersebut.  

5. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
    - Karena framework Django menggunakan bahasa python yang sintaksnya lebih simple dan mudah dipahami
    - Karena framework Django adalah fullstack yang lengkap, sehingga memudahkan untuk fokus building the app tanpa harus melakukan banyak konfigurasi tambahan, karena fitur-fitur penting sudah tersedia secara built in.
    - Karena Django bisa dijadikan backend yang dapat dihubungkan ke aplikasi mobile. Jadi pembuatan aplikasi yang sama pada platform yang berbeda akan menjadi lebih cepat dan sederhana. 

6. **Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
    - Tidak ada feedback karena para asdos membantu dengan baik pada sesi tutorial.

## Tugas 3 👩‍💻
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
    Kemudian, button `Add` pada `main.html` tersebut akan mengarahkan ke `create_product.html` yang saya buat di direktori main/templates juga dengan kode:
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
    Pada kode diatas, `{{ form.as_table }}` adalah template tag yang digunakan untuk menampilkan fields form yang sudah di buat di `forms.py` sebagai table. Setelah itu saya melakukan routing untuk URLnya dengan menambahkan `path('create-product/', create_product, name='create_product'),` di `urlpatterns` pada `urls.py` 
    Kemudian saya menambahkan kode `CSRF_TRUSTED_ORIGINS = [
    "<https://nadia-aisyah-footsal.pbp.cs.ui.ac.id>"]` di `settings.py` 

    - **Membuat halaman yang menampilkan detail dari setiap data objek model.**
    Button `Detail` pada `main.html` akan mengarahkan ke `show_product.html` yang saya buat pada direktori `main/templates` juga dengan isi sebagai berikut:
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
        Pada kode diatas, saya membuat tampilannya menjadi menampilkan detail tentang product dengan urutan thumbnail-name-brand-description-price (saya tidak menampilkan `category` dan `is_featured` karena saya ingin `category` dan `is_featured` hanya terlihat di main saja). Setelah itu saya melakukan routing untuk URLnya dengan menambahkan `path('product/<str:id>/', show_product, name='show_product'),` di `urlpatterns` pada `urls.py` 

6. **Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
    - Tidak ada feedback karena para asdos membantu dengan baik pada sesi tutorial 2.

7.  **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
    [https://drive.google.com/drive/folders/181KisZUXfCjDLfV0Zjzih9475pZjotzt?usp=share_link]

## Tugas 4 👩‍💻
1.  **Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**
- Django AuthenticationForm adalah form bawaan dari Django yang digunakan untuk melakuakan login yaitu untuk melakukan verifikasi username dan password, dan memanggil mekanisme autentikasi Django.
- Kelebihan: 
    - merupakan bagian resmi dari Django 
    - fleksibel dan dirancang generik sehingga bisa diperluasi dan dikostumisasi 
    - sederhana sehingga mudah dipahami
- Kekurangan: 
    - karena generic maka harus dikostumisasi sendiri sesuai kebutuhan yang bisa jadi merepotkan
    - sederhana, jadi kurang cocok jika butuh sistem otentikasi yang lebih kompleks

2. **Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**
    - **autentikasi:** memastikan siapa user 
    - **otorisasi:** menentukan apa yang boleh dilakukan dan diakses oleh user

3. **Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**
    - **session:**
        - Kelebihan:
            - data disimpan di server sehingga lebih aman untuk data yang sensitif
            - bertahan selama sesi masih aktif
            - mendukung proses transaksi 
        - Kekurangan:
            - session habis ketika browser ditutup
    - **cookies**
        - Kelebihan:
            - cookie tetap bertahan meskipun browser sudah ditutup
        - Kekurangan:
            - lebih tidak aman dari session karena data di save di client
            - ada isu privasi karena tracking data user
            - menjadi celah keamanan pada website
    - Sebaiknya menggunakan session untuk data sensitif dan cookie untuk data non-sensitif 

4. **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**
    - Tidak sepenuhnya aman secara default karena ada risiko pencurian cookies.
    - Cara Django menangani:
        - Dengan menyimpan data di server, jadi ketika penyerang mencuri cookie user nama hanya mendapatkan session id bukan isi data. session id yang dihasilkan oleh Django juga acak dan susah ditebak.
        - Dengan CSRF token dari Django yang aktif secara default sebagai pencegahan terhadap situs berbahaya dan penyerang.
        - Dengan *user authentication* dimana Django selali mengganti secret key setiap user login untuk perlindungan tambahan terhadap serangan pada CSRF.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    -  **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.**
        - Fungsi registrasi:
            dengan membuat function register() pada `views.py` untuk menghasilkan form registrasi secara otomatis. Kemudian membuat registration page `register.html`, selanjutnya melakukan routing di urls.py
        - Fungsi login:
             dengan membuat function login_user() pada `views.py` untuk menghasilkan form login secara otomatis. Kemudian membuat login page `login.html`, selanjutnya melakukan routing di urls.py
        - Fungsi logout:
            dengan membuat function logout_user() pada `views.py` kemudian menambahkan hyperlink di `main.html` untuk logout, dan melakukan routing di `urls.py`
        - Memungkinkan pengguna untuk mengakses aplikasi dengan status login dan logoutnya:
            dengan menambahkan decorator `@login_required(login_url='/login')` untuk functions yang dapat diakses ketika pengguna sudah login, yaitu pada function `show_main()`, `create_product()` dan `show_product()` di `views.py`

    - **Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.**
    [https://drive.google.com/file/d/1kKpEZXBc0-ETiZNHQ-Oy_ZvD5U3lXR3g/view?usp=sharing]

    - **Menghubungkan model Product dengan User.**
        Dengan menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True` pada model Product yang sudah dibuat, kemudian melakukan migrate, dan menambahkan potongan code ini di `views.py` 
        - Pada `create_product()`
            ```
            news_entry = form.save(commit = False)
            news_entry.user = request.user
            ```
        - Pada `show_main()`
            menambahkan filtering dengan default all dan product_list untuk product per user
        Kemudian, saya menambahkan button filter all products dan my products pada `main.html` selanjutnya saya menambahkan penampilan nama dari seller di `product_detail.html`

    - **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.**
        - Dengan menambahkan kode pada function `login_user()` untuk menyimpan cookie baru yang bernama last_login yang isinya adalah timestamp terakhir user melakukan login dan mengubah `form.is_valid()` pada `login_user()` di `views.py` menajadi:
            ```
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            ```
        Kemudian juga menambahkan `'user_username': request.user.username,` dan`'last_login': request.COOKIES.get('last_login', 'Never')` pada function `show_main()` di `views.py`. tambahan kode tersebut untuk menampilkan user yang sedang aktif dan terakhir kali user melakukan login. Selanjutnya, saya menambahkan kode ` response.delete_cookie('last_login')` pada logout_user() di `views.py` untuk menghapus cookie setelah logout.

## Tugas 5 👩‍💻
1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
    - Mulai dari prioritas tertinggi:
        - Prioritas 1: inline styles. Contoh: `<p style="color:pink;">`
        - Prioritas 2: id selectors. Contoh: `#navbar`
        - Prioritas 3: classes, attribute selectors, dan pseudo-classes. Contoh: `.product`
        - Prioritas 4: elements dan pseudo-elements. Contoh: `p {color: pink;}`
        - Prioritas 5: universal selector. Contoh: `* {color:pink;}`
    - Jika ada dua selector yang sama maka ambil yang paling akhir. Contoh: `p {color:black;} p{color:pink;}` maka akan mengambil yang pink.

2. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**
    - Karena responsive web design memberikan *user experience* yang konsisten di semua perangkat dengan menyesuaikan layout website sesuai dengan berbagai ukuran layar sehingga aksesibel di berbagai perangkat.
    - Contoh:
        - Sudah menerapkan: Tokopedia
        - Belum menerapkan: Pacil Web Service 
    - Alasan penerapan responsive web design adalah supaya *user experience* optimal pada perangkat apapun.

3. **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**
    - Margin: mengosongkan area di sekitar border (transparan). Cara implementasi adalah dengan `margin: ukuran yang diinginkan`. Contoh:
    ```
    p {
        margin: 10px; 
        margin-top: 5px;
        margin-botton: 5px;
    }
    ```
    - Border: garis tepian yang membungkus konten dan paddingnya. Cara implementasi adalah dengan `border: ukuran yang diinginkan`. Contoh:
    ```
    p {
        border: 3px double black; 
    }
    ```
    - Padding: mengosongkan area sekitar konten (transparan). Cara implementasi adalah dengan `padding: ukuran yang diinginkan` Contoh:
    ```
    p {
        padding: 10px; 
    }
    ```

4. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
    - Flex box: metode satu dimensi untuk mengatur elemen row dan column.
        - Kegunaan: membantu untuk membuat design dengan flexibel tanpa float dan position serta memudahkan perataan elemen.
    - Grid layout: metode layout dua dimensi untuk mengtur rows dan columns secara bersamaan. Biasanya digunakan untuk membuat layout halaman yang lebih complex.
        - Kegunaan: membantu untuk membuat design yang complex dengan menyusun elemen dengan kontrol penuh terhadap posisi dan ukuran dari elemen.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**
    - **Implementasikan fungsi untuk menghapus dan mengedit product.**
        Dengan membuat dua fungsi berikut pada `views.py` 
        ```
        def edit_product(request, id):
            product = get_object_or_404(Product, pk=id)
            form = ProductForm(request.POST or None, instance=product)
            if form.is_valid() and request.method == 'POST':
                form.save()
                return redirect('main:show_main')

            context = {
                'form': form
            }

            return render(request, "edit_product.html", context)

        def delete_product(request, id):
            product = get_object_or_404(Product, pk=id)
            product.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
        ```
        Selanjutnya saya melakukan routing dengan melakukan import sebagai berikut `from main.views import edit_product, delete_product` dan menambahkan path sebagai berikut pada `urlpatterns` di `urls.py`
        ```
        path('product/<int:id>/edit', edit_product, name='edit_product'),
        path('product/<int:id>/delete', delete_product, name='delete_product'),
        ```

    - **Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:**
        - **Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.**
            - Dengan mengganti ukuran dan warna dengan *color palette* sebagai berikut :
                - cherry [#75070C]
                - dusty red [#A63636]
                - olive [#4F6815]
                - moss [#5F7B1F]
                - beige [#CBB4AB]
                - oat [#F0E6DA]
                - pearl [#FAF6EF]

        - **Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:**
            - **Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.**
                Dengan menambahkan `no-product.png` di direktori `static/image` potongan code berikut pada main:
                ```
                ...
                {% if not product_list %}
                <div class="bg-[#F0E6DA] rounded-lg border border-gray-200 p-12 text-center">
                    <div class="w-32 h-32 mx-auto mb-4">
                    <img src="{% static 'image/no-product.png' %}" alt="No products available" class="w-full h-full object-contain">
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">No product found</h3>
                    <p class="text-gray-500 mb-6">Be the first to sell football product with the community.</p>
                    <a href="{% url 'main:create_product' %}" class="inline-flex items-center px-4 py-2 bg-[#4F6815] text-white rounded-md hover:bg-[#5F7B1F] transition-colors">
                    Create Product
                    </a>
                </div>
                ...
                ```
            - **Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).**
                - Dengan membuat file `card_product.html` di direktori `main/templates ` kemudian melakukan styling pada card di file tersebut. Design saya: [https://drive.google.com/drive/folders/1uBxHVdLwX544zmJ806-afdc2f-tVbDeC?usp=share_link]

        - **Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!**
            - Dengan menambahkan potongan kode dibawah pada `card_product.html`
            ```
            <!-- Action Buttons -->
            {% if user.is_authenticated and product.user == user %}
            <div class="flex items-center justify-between pt-4 border-t border-[#FAF6EF]">
                <a href="{% url 'main:show_product' product.id %}" class="text-[#4F6815] hover:text-white font-medium text-sm transition-colors">
                    Details
                </a>
                <div class="flex space-x-2">
                <a href="{% url 'main:edit_product' product.id %}" class="text-black hover:text-white text-sm transition-colors">
                    Edit
                </a>
                <a href="{% url 'main:delete_product' product.id %}" class="text-[#75070C] hover:text-white text-sm transition-colors">
                    Delete
                </a>
                </div>
            </div>
            {% else %}
            <div class="pt-4 border-t border-gray-100">
                <a href="{% url 'main:show_product' product.id %}" class="text-[#75070C] hover:text-white font-medium text-sm transition-colors">
                Details
                </a>
            </div>
            {% endif %}
            ```
        
        - **Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**
            - Dengan membuat file `navbar.html` pada direktori `main/templates` kemudian menautkan navbar tersebut ke `main.html` dengan `{% include 'navbar.html' %}` di dalam `{% block content %} ... {% endblock content%}`. Untuk membuat navbar tersebut jadi responsive maka mengatur dengan 
            - untuk desktop:
                ```
                <!-- Desktop Navigation -->
                <div class="hidden md:flex items-center space-x-8">
                <a href="/" class="text-[#F0E6DA] hover:text-white font-medium transition-colors">
                    Home
                </a>
                <a href="?filter=my" class="text-[#F0E6DA] hover:text-white font-medium transition-colors">
                    My Products
                </a>
                <a href="{% url 'main:create_product' %}" class="text-[#F0E6DA] hover:text-white font-medium transition-colors">
                    Create Product
                </a>
                </div>
                
                <!-- Desktop User Section -->
                <div class="hidden md:flex items-center space-x-6">
                {% if user.is_authenticated %}
                    <div class="text-right">
                    <div class="text-sm font-medium text-[#CBB4AB]">{{ user_username|default:user.username }}</div>
                    <div class="text-xs text-[#F0E6DA]">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
                    </div>
                    <a href="{% url 'main:logout' %}" class="bg-[#F0E6DA] text-[#75070C] font-medium transition-colors px-4 py-2 rounded-md font-medium transition-colors  hover:text-white">
                    <b>Logout</b>
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="text-gray-600 hover:text-white font-medium transition-colors">
                    Login
                    </a>
                    <a href="{% url 'main:register' %}" class="bg-pink-600 hover:text-white text-white px-4 py-2 rounded font-medium transition-colors">
                    Register
                    </a>
                {% endif %}
                </div>
                ```
            - Untuk mobile:
                ```
                <!-- Mobile Menu Button -->
                <div class="md:hidden flex items-center">
                <button class="mobile-menu-button p-2 text-[#F0E6DA] hover:text-white transition-colors">
                    <span class="sr-only">Open menu</span>
                    <div class="w-6 h-6 flex flex-col justify-center items-center">
                    <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
                    <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"></span>
                    <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
                    </div>
                </button>
                </div>
                <!-- Mobile Menu -->
                <div class="mobile-menu hidden md:hidden bg-[#A63636] border-t border-gray-200">
                <div class="px-6 py-4 space-y-4">
                    <!-- Mobile Navigation Links -->
                    <div class="space-y-1">
                    <a href="/" class="block text-[#F0E6DA] hover:text-white font-medium py-3 transition-colors">
                        Home
                    </a>
                    <a href="?filter=my" class="block text-[#F0E6DA] hover:text-white font-medium py-3 transition-colors">
                        My Products
                    </a>
                    <a href="{% url 'main:create_product' %}" class="block text-[#F0E6DA] hover:text-white font-medium py-3 transition-colors">
                        Create Product
                    </a>
                    </div>
                    
                    <!-- Mobile User Section -->
                    <div class="border-t border-gray-200 pt-4">
                    {% if user.is_authenticated %}
                        <div class="mb-4">
                        <div class="font-medium text-[#CBB4AB]">{{ user_username|default:user.username }}</div>
                        <div class="text-sm text-[#F0E6DA]">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
                        </div>
                        <div class="border-t border-gray-200 pt-4">
                            <a href="{% url 'main:logout' %}" class="bg-[#75070C] text-[#F0E6DA] font-medium transition-colors px-4 py-2 rounded-md font-medium transition-colors  hover:text-white">
                            <b>Logout</b>
                            </a>
                        </div>
                    {% else %}
                        <div class="space-y-3">
                        <a href="{% url 'main:login' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
                            Login
                        </a>
                        <a href="{% url 'main:register' %}" class="block bg-pink-600 hover:bg-pink-700 text-white font-medium py-3 px-4 rounded text-center transition-colors">
                            Register
                        </a>
                        </div>
                    {% endif %}
                </div>
            ```
        - Untuk menampilkan hamburger:
            ```
            <script>
                const btn = document.querySelector("button.mobile-menu-button");
                const menu = document.querySelector(".mobile-menu");
                
                btn.addEventListener("click", () => {
                    menu.classList.toggle("hidden");
                });
            </script>
            ```
        - Perubahan yang saya lakukan pada navbar adalah menambahkan `My Products` yang menampilan product yang dibuat oleh user yang sedang login.
        - Tampilan navbar yang saya buat: [https://drive.google.com/drive/folders/1uBxHVdLwX544zmJ806-afdc2f-tVbDeC?usp=share_link]

## Tugas 6 👩‍💻
1. **Apa perbedaan antara synchronous request dan asynchronous request?**
    - **Synchronous request**: Mencegah DOM untuk mengeksekusi kode selanjutnya hingga server memberikan response. User tidak dapat membuat request yang lain hinggga request sebelumnya diterima.
    - **Asynchronous request**: Tidak mencegah DOM untuk mengeksekusi kode selanjutnya saat menunggu server memberikan response. DOM dapat mengeksekusi request secara bersamaan.

2. **Bagaimana AJAX bekerja di Django (alur request–response)?**
    - Ilustrasi alur: [https://drive.google.com/file/d/1OVLGjkAD8Km-gdCOYUuqa2qKE4ETU08l/view?usp=sharing]
    - Penjelasan: Ketika user mengirimkan request pada halaman web, sebuah `XMLHttpRequest` object akan dibuat oleh JavaScript. Kemudian object tersebut akan mengirimkan request ke Django, dimana views.py pada Django akan memproses request tersebut, kemudian memproses data dan mengembalikan response kembali dalam bentuk JSON. Selanjutnya, response tersebut akan dibaca oleh JavaScript dan aksi berikutnya akan dipicu oleh JavaScript sesuai dengan kode yang dibuat.

3. **Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?**
    - Keuntungan menggunakan AJAX dibandingkan dengan render biasa pada Django adalah menawarkan user experience yang lebih baik dan membuat web lebih responsif dan cepat. Karena dengan menggunakan AJAX maka tidak perlu reload halaman setiap kali ada request seperti render biasa di Django.

4. **Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?**
    - **Dengan menambahkan strip_tags**: Menghapus semua tag html dari input, sehingga data yang masuk ke database sudah bersih.
    - **Dengan membersihkan data dengan DOMPurify**: Data berbahaya yang sudah ada di database akan dihapus secara otomatis.

5. **Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?**
    - AJAX memungkinkan halaman web untuk memperbarui data secara asynchronous dengan mengirimkan data ke server di balik layar. Sehingga, user dapat memperbarui sebagian elemen pada halaman tanpa harus melakukan reload halaman secara keseluruhan. Dengan hal tersebut, user experience akan menjadi lebih cepat dan nyaman.
