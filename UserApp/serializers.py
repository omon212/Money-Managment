from rest_framework.serializers import ModelSerializer
from .models import User,PayMoney
from rest_framework import serializers





class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", )
# class UserSerializer(serializers.Serializer)
#     username = serializers.CharField(max_length=30)
#     password = serializers.CharField(max_length=30)
#     email = serializers.CharField(max_length=30)
#     recover_password = serializers.IntegerField(null=True)
class ALLUSERSERIALIZER(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class PayMoneySerializer(ModelSerializer):
    class Meta:
        model = PayMoney
        fields = '__all__'
class UserSerializerFilter(ModelSerializer):
    class Meta:
        model = PayMoney
        fields = ("who",)

class AllUserPaySerializer(ModelSerializer):
    class Meta:
        model = PayMoney
        fields = '__all__'


