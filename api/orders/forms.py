from django import forms
from .models import Customer, Item, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'code','phone']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'item', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()
        self.fields['item'].queryset = Item.objects.all()

