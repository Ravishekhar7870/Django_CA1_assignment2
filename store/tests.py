from django.test import TestCase

class ProductPageTests(TestCase):
    def test_product_detail_page(self):
        response = self.client.get('/product/101/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Price:')
