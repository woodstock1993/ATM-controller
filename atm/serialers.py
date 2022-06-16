from rest_framework import serializers
from atm.models import Card, Account


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'card_number',
            'pin_number',
            'account',
        )


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'account_number',
        )


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'