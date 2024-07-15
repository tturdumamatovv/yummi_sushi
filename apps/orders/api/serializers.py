# serializers.py
from rest_framework import serializers
from apps.orders.models import Order, OrderItem, Delivery
from apps.product.models import ProductSize, Set
from apps.authentication.models import UserAddress


class ProductOrderItemSerializer(serializers.ModelSerializer):
    product_size_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['product_size_id', 'quantity']

    def validate(self, data):
        if data.get('product_size_id') == 0:
            raise serializers.ValidationError("Invalid product_size_id.")
        return data


class SetOrderItemSerializer(serializers.ModelSerializer):
    set_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['set_id', 'quantity']

    def validate(self, data):
        if data.get('set_id') == 0:
            raise serializers.ValidationError("Invalid set_id.")
        return data


class DeliverySerializer(serializers.ModelSerializer):
    user_address_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Delivery
        fields = ['user_address_id', 'delivery_time']


class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderItemSerializer(many=True, required=False)
    sets = SetOrderItemSerializer(many=True, required=False)
    delivery = DeliverySerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery', 'order_time', 'total_amount', 'is_pickup', 'order_status', 'products',
                  'sets']
        read_only_fields = ['total_amount', 'order_time', 'order_status']

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        sets_data = validated_data.pop('sets', [])
        delivery_data = validated_data.pop('delivery')
        user = validated_data.pop('user')

        user_address = UserAddress.objects.get(id=delivery_data['user_address_id'])
        nearest_restaurant = self.context['nearest_restaurant']
        delivery_fee = self.context['delivery_fee']

        delivery = Delivery.objects.create(
            restaurant=nearest_restaurant,
            user_address=user_address,
            delivery_time=delivery_data['delivery_time'],
            delivery_fee=delivery_fee
        )

        order = Order.objects.create(
            delivery=delivery,
            user=user,
            restaurant=nearest_restaurant,
            **validated_data
        )

        for product_data in products_data:
            if product_data.get('product_size_id'):
                OrderItem.objects.create(order=order, product_size_id=product_data['product_size_id'],
                                         quantity=product_data['quantity'])

        for set_data in sets_data:
            if set_data.get('set_id'):
                OrderItem.objects.create(order=order, set_id=set_data['set_id'], quantity=set_data['quantity'])

        return order
