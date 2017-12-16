from rest_framework import viewsets, status, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Ciudad, Tienda, Usuario
from .serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer


class CiudadViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    """
    API endpoint que permite a las ciudades ser vistas y listados.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class TiendaViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    """
    API endpoint que permite a las tiendas ser vistas y listados.
    """
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

    @detail_route(methods=['get'], url_path='usuarios')
    def get_users(self, request, pk=None):
        """
        Retorna una lista de todos los usuarios que pertenecen
        a la tienda seleccionada.
        """
        tienda = self.get_object()
        serializer_context = {
            'request': request,
        }
        usuarios = tienda.usuarios.all()
        serializer = UsuarioSerializer(usuarios, many=True, context=serializer_context)
        return Response(serializer.data)


class UsuarioViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    """
    API endpoint que permite a los usuarios ser vistos y listados.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @detail_route(methods=['get'], url_path='tiendas')
    def get_stores(self, request, pk=None):
        """
        Retorna una lista de todas las tiendas que pertenecen
        al usuario seleccionado.
        """
        usuario = self.get_object()
        serializer_context = {
            'request': request,
        }
        tiendas = usuario.tiendas.all()
        serializer = TiendaSerializer(tiendas, many=True, context=serializer_context)
        return Response(serializer.data)
