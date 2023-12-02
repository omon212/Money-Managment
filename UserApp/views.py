from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from .serializers import UserSerializer,ALLUSERSERIALIZER,PayMoneySerializer,UserSerializerFilter,AllUserPaySerializer
from .models import User,PayMoney
from drf_yasg.utils import swagger_auto_schema


class UserRegisterView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        # saver = User.objects.create(username=username,password=password,email=email)
        # saver.save()


        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"})
        else:
            return Response(serializer.errors)

class LoginView(APIView):
    queryset = User.objects.all()
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.all().filter(username=username, password=password)

        if user is None:
            return Response({"message": "Not Found user"})
        else:
            return Response({"message":"Login Sucsessfuy"})


class AllUser(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = ALLUSERSERIALIZER(users,many=True)

        return Response(serializer.data)

class AllPays(APIView):
    def get(self, request):
        pullar = PayMoney.objects.all()
        # return Response(pullar)

        serializer = PayMoneySerializer(pullar, many=True)



        return Response(serializer.data)

class PayMoneyView(APIView):
    @swagger_auto_schema(request_body=PayMoneySerializer)
    def post(self,request):
        serializer = PayMoneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FilterUserMoney(APIView):

    @swagger_auto_schema(request_body=UserSerializerFilter)
    def post(self,request):
        who =request.data.get('who')
        pullar_filter = PayMoney.objects.all().filter(who=who)
        serializer = PayMoneySerializer(pullar_filter, many=True)
        return Response(serializer.data)


class AllUserPayView(APIView):

    def get(self,request):
        userlar = User.objects.all()
        odamlar_royxati = []

        for i in userlar:
            odamlar_royxati.append(i.id)
        fake_database_kirim  = {}
        print(odamlar_royxati)
        for d in odamlar_royxati:
            print(d)
            filter_kirim = PayMoney.objects.all().filter(id=int(d),status_money='chiqim')
        serializer = AllUserPaySerializer(filter_kirim,many=True)
        return Response(serializer.data)
        

import random
class AddUserFake(APIView):
    def get(self,request):

        for i in range(1,11):
            for d in range(3):
                methodplace = ["Oziq-ovqat","Transport","Kiyim-kechak","Komunal","Axborot-vositalari","Kafe-restoran","Taksi","Xizmatlar"]
                method = random.choice(methodplace)
                comment = ["chingiz togo","dostim uchun keta oldik","chingiz uchun padarka oldik"]
                com = random.choice(comment)
                pul = random.randint(1000,10000000)
                fake_money = PayMoney.objects.create(total = pul,who_id = i,status_money = 'chiqim',method_plase = method,comment  = com)
                fake_money.save()
        return Response({"msg": "okey"})