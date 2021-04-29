from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from AleksSite.serializer import ShopSerializer
from firstapp.models import Shop


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['price']


def index(request):
    products = Shop.objects.all()
    return render(request, "index.html", {"products": products})
