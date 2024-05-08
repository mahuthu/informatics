from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    
    amount = serializers.SerializerMethodField(method_name='get_amount')


    class Meta:
        model = Order
        fields = ("customer", "item", "amount", "quantity")

    def get_amount(self, instance):
        item = instance.get('item')
        quantity = instance.get('quantity')
        return item.price * quantity


    def create(self, validated_data):

        order = Order.objects.create(amount=self.get_amount(validated_data), **validated_data)
        return order
       

    # def create(self, validated_data):
    #     customer_data = validated_data.get('customer')
    #     item_data = validated_data.get('item')
    #     quantity = validated_data.get('quantity')

    #     # Fetch the customer and item objects from the database
        
    #     items = Item.objects.get(pk=item_data)
        


    #     # Calculate the amount based on item price and quantity
    #     amount = self.get_amount(items, quantity)

    #     # Create the order object with the calculated amount and other fields
    #     order = Order.objects.create(customer=customer_data, item=item_data, quantity=quantity, amount=amount)

    #     return order

        #return Order.objects.create(amount=self.get_amount(validated_data), **validated_data)



    # def get_amount(self, instance):
    #     item = instance.get('item')
    #     quantity = instance.get('quantity')
    #     return item.price * quantity
    
    # def create(self, validated_data):
    #     customer = validated_data.get('customer')
    #     item_id = validated_data.get('item')
    #     quantity = validated_data.get('quantity')
    #     amount = self.get_amount(validated_data)

    #     data = {
    #         'customer':customer,
    #         "item": item_id,
    #         "quantity":quantity,
    #         "amount":amount
    #     }
       

    #     return super().create(data)
    






        # def create(self, validated_data):
        #     item_id = validated_data.get('item')
        #     quantity = validated_data.get('quantity')

        #     # Fetch the item object from the database
        #     try:
        #         item = Item.objects.get(pk=item_id)
        #     except Item.DoesNotExist:
        #         raise serializers.ValidationError("Item not found")

        #     # Ensure that the item price is a Decimal type
        #     item_price = Decimal(item.price)

        #     # Calculate the total amount as a Decimal
        #     total_amount = item_price * Decimal(quantity)

        #     # Add the calculated amount to validated data before saving
        #     validated_data['amount'] = total_amount

        #     # Create and return the order object
        #     return super().create(validated_data)


    # def get_amount(self, instance):
    #     item = instance.get('item')
    #     quantity = instance.get('quantity')
    #     return item.price * quantity


    # def create(self, validated_data):
    #     return Order.objects.create(amount=self.get_amount(validated_data), **validated_data)

    # def update(self, instance, validated_data):
    #     instance.customer = validated_data.get('customer', instance.customer)
    #     instance.item = validated_data.get('item', instance.item)
    #     instance.amount = self.get_amount(validated_data)
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     instance.save()
    #     return instance

    # def get_amount(self, instance):
    #     item = instance.get('item')
    #     quantity = instance.get('quantity')
    #     amount =  item.price * quantity
    #     return amount
    
    # def create(self, validated_data):
    #     return Order.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.customer = validated_data.get('customer', instance.customer)
    #     instance.item = validated_data.get('item', instance.item)
    #     instance.amount = validated_data.get('amount', instance.amount)
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     instance.save()
    #     return instance



    
   
    
    
# # Path: api/orders/views.py
# from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework import permissions
# from .models import Customer, Order
# from .serializers import CustomerSerializer, OrderSerializer

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages


# class CustomerListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()        
#         return redirect('order-list-create')
    
# class OrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()        
#         return redirect('success', pk=serializer.data['id'])
    
#     def get_context_data(self, request, *args, **kwargs):
#         item = Item.objects.all()
#         customer = Customer.objects.all()
#         context = {
#             'items': item,
#             'customers': customer
#         }
#         return context
    
# def success(request, pk):
#     order = Order.objects.get(id=pk)
#     return render(request, 'orders/success.html', {"order": order})

# def home(request):
#     return redirect('order-list-create')

# # Path: api/orders/urls.py

# from django.urls import path
# from. import views
# from .views import CustomerListCreateAPIView, OrderListCreateAPIView

# urlpatterns = [
#     path('home', views.home, name="home"),
#     path('customer', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
#     path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
#     path('success/<int:pk>', views.success, name='success'),
# ]
