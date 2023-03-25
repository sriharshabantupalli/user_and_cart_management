from rest_framework import serializers
from .models import User, UserProfileModel, UserCartModel, ProductMainModel, ProductImageModel, UserCartProductModel

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'

class UserCartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartModel
        fields = '__all__'

class ProductMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMainModel
        fields = '__all__'

class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = '__all__'

class UserCartProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartProductModel
        fields = '__all__'

class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)