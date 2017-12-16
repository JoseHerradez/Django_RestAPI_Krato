from rest_framework import serializers
from .models import Ciudad, Tienda, Usuario


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('nombre')


class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('nombre', 'ubicacion', 'ciudad')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre', 'cedula', 'residencia', 'tiendas')
