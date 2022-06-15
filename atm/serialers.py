from rest_framework import serializers
from atm.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'card_number',
            'pin_number',
            'account',
        )
