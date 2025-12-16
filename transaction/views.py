from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwner
from .filters import TransactionFilter
from .models import Transaction, Category
from .serializers import CategorySerializer, TransactionSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsOwner]
    filterset_class = TransactionFilter
    ordering_fields = ['amount', 'created_at']

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)