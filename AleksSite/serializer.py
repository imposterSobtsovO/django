from rest_framework.serializers import ModelSerializer

from firstapp.models import Shop


# Serializer can work not only to output (serialization), but also to input(validation).
class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'