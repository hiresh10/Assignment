from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api import views

router = DefaultRouter()
router.register("api",views.Signup,basename="userapi")

urlpatterns = [
    path("api/",include(router.urls))
]
