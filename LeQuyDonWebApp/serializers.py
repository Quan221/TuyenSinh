from  rest_framework import  serializers

from .models import  User, DonTuyenSinh, Quan, QuanvaPhuong, Phuong, DaHocHetLop5, TruongVaQuan, Truong, DangKyHoc




class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = validated_data.copy()

        u = User(**data)
        u.set_password(u.password)
        u.save()

        return u

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True}
        }



class QuanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quan
        fields = '__all__'

class QuanvaPhuongSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuanvaPhuong
        fields = '__all__'

class PhuongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phuong
        fields = '__all__'

class DonTuyenSinhSerializers(serializers.ModelSerializer):
    class Meta:
        model = DonTuyenSinh
        fields = '__all__'
        read_only_fields = ('id',)
class TrinhDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DaHocHetLop5
        fields = '__all__'
class DangKyHocSerializers(serializers.ModelSerializer):
    class Meta:
        model = DangKyHoc
        fields = '__all__'
class TruongVaQuanSerializers(serializers.ModelSerializer):
    class Meta:
        model = TruongVaQuan
        fields = '__all__'
class TruongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Truong
        fields = '__all__'


