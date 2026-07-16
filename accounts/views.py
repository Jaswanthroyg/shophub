from rest_framework.views import APIView    
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({"message":"user registered successfully",
                             "username":user.username,
                             "email":user.email}, status=201)
        return Response(serializer.errors, status=400)
class LoginAPIView(APIView):
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username, password=password)

            if user is None:
                return Response({"Message":"Invalid credentials please try again"}, status=400)
                
            refresh = RefreshToken.for_user(user)
            access=refresh.access_token
            return Response({
                "message":"login successful",
                "refresh": str(refresh),
                "access": str(access)},status=200
            )
        return Response(serializer.errors, status=400)