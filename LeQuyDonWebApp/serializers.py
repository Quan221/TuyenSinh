from  rest_framework import  serializers

from .models import  User, Products, Quan, QuanvaPhuong, Phuong




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

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ('id',)
