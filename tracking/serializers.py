from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ExpenseIncome

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    
class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField(source='get_total')

    class Meta:
        model = ExpenseIncome
        fields = ['id', 'user', 'title', 'description', 'amount', 'transaction_type', 'tax', 'tax_type', 'total', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
        
    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount cannot be negative.")
        return value

    def validate_tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Tax cannot be negative.")
        return value