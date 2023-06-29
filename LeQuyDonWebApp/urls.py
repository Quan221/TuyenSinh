from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='user')
router.register('quan', views.QuanViewSet, basename='quan')
router.register('dontuyensinh', views.DonTuyenSinhViewSet, basename='dontuyensinh')
router.register('trinhdo', views.TrinhDoViewSet, basename='trinhdo')
router.register('dangkyhoc', views.DangKyHocViewSet, basename='dangkyhoc')


urlpatterns = [
    path('', include(router.urls)),

]