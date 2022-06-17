import sys
import os
import django

# system setup
sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from atm.models import Account, Card

def is_valid_card(card_number):
    queryset = len(Card.objects.filter(card_number=card_number))
    if queryset == 0:
        return False
    return True


def is_valid_pin_number(card_number, pin_number):
    if is_valid_card(card_number):
        Card.objects.get(card_number=card_number)
