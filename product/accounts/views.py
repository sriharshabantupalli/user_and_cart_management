from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, UserProfileModel, UserCartModel, ProductMainModel, ProductImageModel, UserCartProductModel
from .serializers import UserModelSerializer, UserProfileModelSerializer, UserCartModelSerializer, ProductMainModelSerializer, ProductImageModelSerializer, UserCartProductModelSerializer, SendOTPSerializer, UserLoginSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # create user cart
            user_cart = UserCartModel.objects.create(owner=user, price=0)

            # create user profile
            user_profile = UserProfileModel.objects.create(owner=user)

            return Response({
                'user': UserModelSerializer(user).data,
                'user_cart': UserCartModelSerializer(user_cart).data,
                'user_profile': UserProfileModelSerializer(user_profile).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductMainModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()

            return Response(ProductMainModelSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(generics.ListAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = ProductMainModelSerializer


class ProductWithImagesCreateView(generics.CreateAPIView):
    serializer_class = ProductMainModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()

            images = request.FILES.getlist('images')
            for image in images:
                ProductImageModel.objects.create(product=product, image=image)

            return Response(ProductMainModelSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendOTPView(generics.CreateAPIView):
    serializer_class = SendOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Send OTP to the user's email
            # ... implementation ...

            return Response({'detail': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Validate the OTP and login the user
            # ... implementation ...

            return Response({'detail': 'User logged in successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCartProductCreateView(generics.CreateAPIView):
    serializer_class = UserCartProductModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']

            # Check if the user already has the product in their cart
            user_cart_product = UserCartProductModel.objects.filter(cart__owner=user, product=product).first()
            if user_cart_product:
                user_cart_product.quantity += quantity
                user_cart_product.save()
            else:
                # Add the product to the user's cart
                user_cart = UserCartModel.objects.get(owner=user)
                user_cart_product = UserCartProductModel.objects.create(cart=user_cart, product=product,
                                                                        quantity=quantity)

            return Response(UserCartProductModelSerializer(user_cart_product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
