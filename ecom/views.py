from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": f"{user.role} registered successfully!"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Both fields are required."}, status=400)

    user = authenticate(username=email, password=password)
    if not user:
        return Response({"error": "Invalid credentials."}, status=400)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "role": user.role}, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_view(request):
    if request.user.role == "CUSTOMER":
        return Response({"message": "Welcome Customer!"}, status=200)
    return Response({"error": "Unauthorized"}, status=403)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def seller_view(request):
    if request.user.role == "SELLER_OWNER":
        return Response({"message": "Welcome Seller!"}, status=200)
    return Response({"error": "Unauthorized"}, status=403)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_view(request):
    if request.user.role == "ADMIN":
        return Response({"message": "Welcome Admin!"}, status=200)
    return Response({"error": "Unauthorized"}, status=403)
