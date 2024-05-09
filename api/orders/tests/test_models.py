from django.test import TestCase
from orders.models import Customer, Item, Order

class CustomerModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Test Customer',
            code='TC001',
            email='test@example.com',
            phone='1234567890'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'Test Customer')
        self.assertEqual(self.customer.code, 'TC001')
        self.assertEqual(self.customer.email, 'test@example.com')
        self.assertEqual(self.customer.phone, '1234567890')

    def test_customer_str_method(self):
        self.assertEqual(str(self.customer), 'Test Customer')

class ItemModelTestCase(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name='Test Item', price=100)

    def test_item_creation(self):
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.price, 100)

    def test_item_str_method(self):
        self.assertEqual(str(self.item), 'Test Item')

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer', code='TC001')
        self.item = Item.objects.create(name='Test Item', price=100)
        self.order = Order.objects.create(customer=self.customer, item=self.item, quantity=2)

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.item, self.item)
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.amount, 200)  # Assuming quantity * price = 2 * 100 = 200

    def test_order_str_method(self):
        self.assertEqual(str(self.order), 'Test Customer')
