from django.test import TestCase
from django.urls import reverse
from orders.models import Customer, Order, Item
from orders.views import home1, order_detail, CreateCustomer, CreateOrder
from orders.forms import CustomerForm, OrderForm
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(name='Test Customer', code='12345')
        self.item = Item.objects.create(name='Test Item', price=100)

    def test_home1_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home1'))
        self.assertEqual(response.status_code, 302)  # Check if the view redirects (e.g., to create_order)

    def test_order_detail_view(self):
        order = Order.objects.create(customer=self.customer, item=self.item, quantity=1, amount=100)
        response = self.client.get(reverse('order_detail', kwargs={'pk': order.pk}))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a success status code

    def test_CreateCustomer_view(self):
        self.client.force_login(self.user)
        form_data = {'name': 'New Customer', 'code': '54321'}
        response = self.client.post(reverse('create_customer'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Check if the view redirects after form submission

    def test_CreateOrder_view(self):
        self.client.force_login(self.user)
        form_data = {'customer': self.customer.pk, 'item': self.item.pk, 'quantity': 2}  # Sample form data
        response = self.client.post(reverse('create_order'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Check if the view redirects after form submission

        # You can add more assertions to check the specific behavior of the view

