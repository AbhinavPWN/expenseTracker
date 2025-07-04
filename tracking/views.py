from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import Serializer

from .models import ExpenseIncome
from .permissions import IsOwnerOrSuperuser
from .serializers import ExpenseIncomeSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "message": "User created successfully"
        }, status=status.HTTP_201_CREATED)

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseIncome.objects.all()  
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)