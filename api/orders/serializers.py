from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
   # amount = serializers.IntegerField(read_only=True)

    quantity = serializers.IntegerField()
    
    amount = serializers.SerializerMethodField(method_name='get_amount')


    class Meta:
        model = Order
        fields = ("customer", "item", "amount", "quantity")

    def get_amount(self, instance):
        item = instance.get('item')
        quantity = instance.get('quantity')
        return item.price * quantity


    def create(self, validated_data):
        quantity = validated_data.pop('quantity', 1)
        return Order.objects.create(amount=self.get_amount(validated_data), **validated_data)

    # def create(self, validated_data):
    #     customer = validated_data.get('customer')
    #     item = validated_data.get('item')
    #     quantity = validated_data.get('quantity')
    #     total_amount = item.price * quantity
    #     order = Order.objects.create(customer=customer, item=item, amount=total_amount)
    #     return order