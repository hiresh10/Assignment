from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Index,name="index"),
    path("signup",views.SignUppage, name="signup"),
    path("register/",views.Register, name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("login/",views.Login,name="login"),
    path("home/",views.Home,name="home"),
    # path("userapi/",include('app.api.urls')),
]
