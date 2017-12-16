from rest_framework import serializers
from .models import Ciudad, Tienda, Usuario


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'


class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    usuarios = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='usuario-detail',
        read_only=True
    )

    class Meta:
        model = Tienda
        fields = '__all__'


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
