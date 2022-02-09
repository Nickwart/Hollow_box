from .models import ShopUser
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ListViewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=155, required=False)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = ShopUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=155, required=False)
    first_name = serializers.CharField(max_length=265)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = ShopUser
        fields = '__all__'


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    queryset = ShopUser.objects.all()


class ListUsers(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ListViewSerializer
    queryset = ShopUser.objects.all()
    pagination_class = None


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
