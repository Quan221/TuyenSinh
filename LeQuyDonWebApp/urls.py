from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='user')
router.register('quan', views.QuanViewSet, basename='quan')
router.register('products', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),

]