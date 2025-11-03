from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/non_existent_page/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        # Membuat instance Product
        product = Product.objects.create(
            name="Laptop Gaming",
            price=15000000,
            description="Laptop dengan spesifikasi tinggi untuk gaming.",
            category="electronics",
            is_featured=True,
            stock=10,
        )
        # Memastikan atribut sesuai dengan yang dibuat
        self.assertEqual(product.name, "Laptop Gaming")
        self.assertEqual(product.price, 15000000)
        self.assertTrue(product.is_featured)
        self.assertEqual(product.stock, 10)
        
    def test_product_stock_management(self):
        product = Product.objects.create(
            name="Keyboard Mekanik",
            price=1000000,
            description="Keyboard mekanik dengan switch brown.",
            category="peripherals",
            is_featured=False,
            stock=5
        )
        # Tes menambah stok
        initial_stock = product.stock
        product.add_stock(5)
        self.assertEqual(product.stock, initial_stock + 5)
        
        # Tes mengurangi stok
        initial_stock = product.stock
        product.reduce_stock(3)
        self.assertEqual(product.stock, initial_stock - 3)

    def test_product_default_stock(self):
        # Membuat instance Product tanpa mengisi stok
        product = Product.objects.create(
            name="Mouse Wireless",
            price=500000,
            description="Mouse wireless ringan.",
            category="peripherals",
            is_featured=False,
        )
        # Memastikan nilai default stock adalah 0
        self.assertEqual(product.stock, 0)