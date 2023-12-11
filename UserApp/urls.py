from django.urls import path
from .views import UserRegisterView, LoginView, AllUser, PayMoneyView, FilterUserMoney, AllPays, AllUserPayView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('all/',AllUser.as_view()),
    path('paymoney/',PayMoneyView.as_view()),
    path('usermoney',FilterUserMoney.as_view()),
    path('pays/',AllPays.as_view()),
    path('kirimchiqim/',AllUserPayView.as_view()),
    # path('addfake/',AddUserFake.as_view())
]