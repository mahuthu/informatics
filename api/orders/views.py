from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Customer, Order, Item
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import serializers, status


@login_required
def home(request):
    return redirect('order-list-create')

def success(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'orders/success.html', {'order': order})

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        
        return redirect('order-list-create')



class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #renderer_classes = [TemplateHTMLRenderer]


    def get_context_data(self, request, *args, **kwargs):
        item = Item.objects.all()
        customer = Customer.objects.all()
        context = {
            'items': item,
            'customers': customer
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request, 'orders/home.html', context)

    def perform_create(self, serializer, *args, **kwargs):
        items_data = self.request.data.get('items')
        customer_data = self.request.data.get('customer')





        if customer_data and items_data:
            # Calculate total amount based on selected items
            item_id = items_data.get("id")
            item = Item.objects.filter(id=item_id).first()
            quantity_data = self.request.data.get('quantity', 1)  # Default quantity is 1
            validated_data = {
                "customer": customer_data,
                "item": item,
                "quantity": quantity_data
                
            }
            serializer = OrderSerializer(data=validated_data)
            serializer.save(**validated_data)
            return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "missing data"}, status=status.HTTP_400_BAD_REQUEST)
        





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
        
        

    

    


