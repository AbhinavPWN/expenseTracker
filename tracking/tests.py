from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import ExpenseIncome
from rest_framework_simplejwt.tokens import RefreshToken

class ExpenseIncomeTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='testpass123')
        self.superuser = User.objects.create_superuser(username='wrongdoer', password='adminpass')
        refresh = RefreshToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_user_registration(self):
        data = {"username": "testuser2", "password": "testpass123"}
        response = self.client.post('/api/auth/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_expense(self):
        data = {"title": "Test", "amount": 100.00, "transaction_type": "debit", "tax": 10.00, "tax_type": "flat"}
        response = self.client.post('/api/expenses/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["total"], 110.00)

    def test_list_expenses(self):
        ExpenseIncome.objects.create(user=self.user1, title="Test", amount=100.00, transaction_type="credit", tax=0, tax_type="flat")
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permission_unauthenticated(self):
        self.client.credentials()
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_regular_user_access_other(self):
        user2 = User.objects.create_user(username='testuser2', password='testpass123')
        expense = ExpenseIncome.objects.create(user=self.user1, title="Test", amount=100.00, transaction_type="credit", tax=0, tax_type="flat")
        refresh = RefreshToken.for_user(user2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get(f'/api/expenses/{expense.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)