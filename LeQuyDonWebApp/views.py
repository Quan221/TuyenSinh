from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response
from .models import User, Quan, Phuong, DonTuyenSinh, QuanvaPhuong, DaHocHetLop5, Truong, TruongVaQuan, DangKyHoc
from .serializers import UserSerializer, PhuongSerializers, DonTuyenSinhSerializers, QuanSerializers, TrinhDoSerializers, TruongSerializers, DangKyHocSerializers
from django.shortcuts import render
from rest_framework import viewsets, status, generics, parsers, permissions
from rest_framework.decorators import action


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
        queryset = User.objects.filter(is_active=True)
        serializer_class = UserSerializer
        parser_classes = [parsers.MultiPartParser, ]

        def get_permissions(self):
                if self.action == 'current_user':
                        return [permissions.IsAuthenticated()]

                return [permissions.AllowAny()]

        @action(methods=['get'], url_path="current-user", detail=False)
        def current_user(self, request):
                return Response(self.serializer_class(request.user, context={'request': request}).data,
                                status=status.HTTP_200_OK)


class QuanViewSet (viewsets.ViewSet, generics.ListAPIView):
        queryset = Quan.objects.all()
        serializer_class = QuanSerializers

        @action(methods=['get'], detail=True, url_path='phuong')
        def get_phuong(self, request, pk):
                phuong = Phuong.objects.filter(quanvaphuong__quan_id=pk)

                return Response(PhuongSerializers(phuong, many=True, context={"request": request}).data,
                                status=status.HTTP_200_OK)

        @action(methods=['get'], detail=True, url_path='truong')
        def get_truong(self, request, pk):
                truong = Truong.objects.filter(truongvaquan__quan_id=pk)

                return Response(TruongSerializers(truong, many=True, context={"request": request}).data,
                                status=status.HTTP_200_OK)

class DonTuyenSinhViewSet (viewsets.ViewSet, generics.CreateAPIView):
        serializer_class = DonTuyenSinhSerializers

class TrinhDoViewSet (viewsets.ViewSet, generics.ListAPIView):
        queryset = DaHocHetLop5.objects.all()
        serializer_class =  TrinhDoSerializers
class DangKyHocViewSet (viewsets.ViewSet, generics.ListAPIView):
        queryset = DangKyHoc.objects.all()
        serializer_class =  DangKyHocSerializers
