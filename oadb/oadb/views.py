from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from . import serializers
from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.schemas import SchemaGenerator
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework_swagger import renderers
from .models import Adaptor, Kit, Database, Run
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import permission_classes


User = get_user_model()


class HomeView(TemplateView):
    template_name = 'oadb/index.html'


@permission_classes((IsAdminUser, ))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = serializers.UserSerializer

@permission_classes((IsAuthenticatedOrReadOnly, ))
class AdaptorViewSet(viewsets.ModelViewSet):
    queryset = Adaptor.objects.all()
    serializer_class = serializers.AdaptorSerializer

@permission_classes((IsAuthenticatedOrReadOnly, ))
class KitViewSet(viewsets.ModelViewSet):
    queryset = Kit.objects.all()
    serializer_class = serializers.KitSerializer

@permission_classes((IsAuthenticatedOrReadOnly, ))
class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = serializers.DatabaseSerializer

@permission_classes((IsAuthenticatedOrReadOnly, ))
class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = serializers.RunSerializer
