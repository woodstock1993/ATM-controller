from rest_framework import serializers
from atm.models import Card, Account


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'pin_number',
            'account_number',
            'card_number',
        )


class CardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


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