from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    transaction_count_last_thirty_days = serializers.IntegerField(read_only=True)
    balance_change_last_thirty_days = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
