from rest_framework import serializers

from website.models import Product, UserData


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'