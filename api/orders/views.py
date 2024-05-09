from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer, Order, Item
from .forms import CustomerForm,  OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from dotenv import load_dotenv

import africastalking
import logging

logger = logging.getLogger(__name__)


load_dotenv()
username = "sandbox"
api_key = "527308bf8c52f133fc68bca976a3d34e2186bece67aa39290d7dc790cbd15b46"

africastalking.initialize(username, api_key)
sms = africastalking.SMS



def send_sms(pk):
    recipients = ['+254726258462']
    sender = "informatics" #alphanumeric sender ID
    order = Order.objects.get(id=pk)
    message = f"Your order #{order.pk} for {order.quantity} {order.item.name} has been placed successfully!"
    try:
        response = sms.send(message, recipients, sender)
        logger.debug(response)


    except Exception as e:
        logger.error(f"An error occurred: {e}")

    

    






@login_required
def home1(request):
    return redirect('create_order')

def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'orders/order_detail.html', {'order': order})






def CreateCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_order")  # Redirect to the create_order view
    else:
        form = CustomerForm()
    
    return render(request, "orders/home1.html", {"form": form})




def CreateOrder(request):
    customers = Customer.objects.all()
    items = Item.objects.all()

    order_form = OrderForm()
    customer_form = CustomerForm()



    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        logger.debug(f"POST data: {request.POST}")  # Debugging statement to log POST data

        item = order_form.data.get("item")
        quantity = int(order_form.data.get("quantity"))
        item_price = Item.objects.get(id = item).price
        logger.debug(f"item_price = {item_price}")
        amount = item_price * quantity
        logger.debug(f"amount = {amount}")  

        order_form.instance.amount = amount
        logger.debug(f"order_form.instance.amount = {order_form.instance.amount}")
        

        if order_form.is_valid():
            order = order_form.save()
            logger.debug(f"order saved: {order}")  # Debugging statement to log saved customer

            send_sms(order.pk)


            return redirect('order_detail', pk=order.pk)
        else:
            logger.debug(f"Order form errors: {order_form.errors}")  # Debugging statement for order form errors
        
                
            order_form = OrderForm()
            customer_form = CustomerForm()

    return render(request, 'orders/home1.html', {'order_form': order_form, 'customer_form': customer_form, 'customers': customers, 'items': items,})






































# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from rest_framework import generics
# from .models import Customer, Order, Item
# from .serializers import CustomerSerializer, OrderSerializer
# from rest_framework.response import Response
# from django.contrib import messages
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework import serializers, status


# @login_required
# def home(request):
#     return redirect('order-list-create')

# def success(request, pk):
#     order = Order.objects.get(id=pk)
#     return render(request, 'orders/success.html', {'order': order})

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
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'orders/success.html'



#     def get_context_data(self, request, *args, **kwargs):
#         item = Item.objects.all()
#         customer = Customer.objects.all()
#         context = {
#             'items': item,
#             'customers': customer
#         }
#         return context
    
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(request, *args, **kwargs)
#         return render(request, 'orders/home.html', context)

#     def perform_create(self, serializer, *args, **kwargs):
#         items_data = self.request.data.get('items')
#         customer_data = self.request.data.get('customer')

#         if customer_data and items_data:
#             # Calculate total amount based on selected items
#             item_id = items_data.get("id")
#             item = Item.objects.filter(id=item_id).first()
#             quantity_data = self.request.data.get('quantity', 1)  # Default quantity is 1
#             validated_data = {
#                 "customer": customer_data,
#                 "item": item,
#                 "quantity": quantity_data
                
#             }
#             serializer = OrderSerializer(data=validated_data)
#             serializer.save(**validated_data)
#             context = self.get_context_data(self.request, *args, **kwargs)
        

#             return render(self.request, self.template_name, context)
#         else:
#             return Response({"message": "missing data"}, status=status.HTTP_400_BAD_REQUEST)
        



    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()  # Object creation and saving handled in the serializer's create method
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




    # def perform_create(self, serializer):
    #     data = self.request.data
    #     customer_id = data.get('customer')  # Assuming 'customer' field in data is customer_id
    #     item_id = data.get('item')
    #     quantity = data.get('quantity')

    #     # Fetch the customer and item objects from the database
    #     try:
    #         customer = Customer.objects.get(pk=customer_id)
    #         item = Item.objects.get(pk=item_id)
    #     except (Customer.DoesNotExist, Item.DoesNotExist):
    #         return Response({"error": "Customer or Item not found"}, status=status.HTTP_400_BAD_REQUEST)

    #     # Ensure that the item price is a Decimal type
    #     item_price = Decimal(item.price)

    #     # Calculate the total amount as a Decimal
    #     total_amount = item_price * Decimal(quantity)

    #     # Update the data dictionary with primary key values and Decimal amount
    #     data['customer'] = customer_id
    #     data['item'] = item_id
    #     data['amount'] = total_amount  # Set the calculated amount here

    #     # Pass the updated data to the serializer for validation and saving
    #     serializer.save(**data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




        #     if item and quantity_data:
        #         validated_data = {
        #             "customer": customer_data,
        #             "item": item,
        #             "quantity": quantity_data
        #         }
        #         serializer = OrderSerializer(data=validated_data)
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save(**validated_data)
        #         return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
        #     else:
        #         return Response({"message": "missing data"}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     raise serializers.ValidationError("Invalid data", code=status.HTTP_400_BAD_REQUEST)
        

        
            # response_data = serializer.data
            # recipients = ['+254726258462']
            # sender = "informatics"
            # message = "Hello, your order has been received successfully. Here is your order reciept".format(response_data)
            # try:
            #     response = self.sms.send(message, recipients, sender)
            #     print(response)

            # except Exception as e:
            #     print(f"An error occurred: {e}")











        #     if item and quantity_data:
        #         total_amount = item.price * quantity_data
        #         data = {
        #             "customer": customer_data,
        #             "item": item,
        #             "amount": total_amount
        #         }
        #         serializer = OrderSerializer(data=data)
        #         serializer.is_valid(raise_exception=True)    
        #         serializer.save()
        #         return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
        #         # return redirect("success", pk=order.id)
                
        #     else:
        #         return Response({"message": "missing data"}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     raise serializers.ValidationError("Invalid data", code=status.HTTP_400_BAD_REQUEST)
        
        

    

    


