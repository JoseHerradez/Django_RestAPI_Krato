from rest_framework import viewsets
from .models import Ciudad, Tienda, Usuario
from .serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer


class CiudadViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las ciudades ser vistas o editadas.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class TiendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las tiendas ser vistas o editadas.
    """
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los usuarios ser vistos o editados.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
