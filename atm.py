import sys
import os
import hashlib
import django

# system setup
sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from atm.models import Account, Card
from atm.serialers import CardSerializer, AccountSerializer, AccountDetailSerializer


def hash_code(pin_number):
    return hashlib.sha256(str(pin_number).encode('utf-8')).hexdigest()


def is_valid_card(card_number):
    queryset = len(Card.objects.filter(card_number=card_number))
    if queryset == 0:
        return False
    return True


def is_valid_card_pin_number(card_number, pin_number):
    if is_valid_card(card_number):
        card_object = CardSerializer(Card.objects.get(card_number=card_number)).data
        if card_object['pin_number'] != hash_code(pin_number):
            print('핀번호가 일치하지 않습니다. 다시 입력해 주십시오')
            return False
        account_object = AccountSerializer(Account.objects.get(account_number=card_object['account_number'])).data
        if len(account_object) == 0:
            print('계좌번호가 유효하지 않습니다. 해당 카드가 하나 이상의 계좌랑 연결되어있는지 확인하세요.')
            return False
        return True


def return_account_number(card_number, pin_number):
    if is_valid_card_pin_number(card_number, pin_number):
        account_number = CardSerializer(Card.objects.get(card_number=card_number)).data['account_number']
        return account_number
    print('유효한 카드번호와 핀번호를 입력하세요')
    return


def current_balance(card_number, pin_number):
    if is_valid_card_pin_number(card_number, pin_number):
        account_number = CardSerializer(Card.objects.get(card_number=card_number)).data['account_number']
        balance = AccountDetailSerializer(Account.objects.get(account_number=account_number)).data['balance']
        print(f'현재 잔액은 {balance}입니다.')
        return balance
    return


def deposit(card_number, pin_number, price):
    try:
        int(price)
    except ValueError:
        print('양의 정수만 입력하세요.')
        return
    if price <= 0:
        print('양의 정수만 입력하세요.')
        return
    if type(price) != type(1):
        print('양의 정수만 입력하세요.')
        return

    if is_valid_card_pin_number(card_number, pin_number):
        account_number = return_account_number(card_number, pin_number)
        account_object = Account.objects.get(account_number=account_number)
        account_object.balance += int(price)
        account_object.save()
        print(f'금액: {price}이 입금되었습니다. 현재 잔액은 {account_object.balance}입니다.')
        return account_object.balance
    print('유효한 카드번호와 핀번호를 입력하세요')
    return


def withdraw(card_number, pin_number, price):
    try:
        int(price)
    except ValueError:
        print('뽑으려는 금액을 양의 정수로 입력하세요.')
        return
    if price <= 0:
        print('뽑으려는 금액을 양의 정수로 입력하세요.')
        return
    if type(price) != type(1):
        print('뽑으려는 금액을 양의 정수로 입력하세요.')
        return
    if is_valid_card_pin_number(card_number, pin_number):
        account_number = return_account_number(card_number, pin_number)
        account_object = Account.objects.get(account_number=account_number)
        if price > account_object.balance:
            print(f'잔액이 부족합니다. {account_object.balance} 안으로 인출이 가능합니다.')
            return
        account_object.balance -= int(price)
        account_object.save()
        print(f'금액: {price}이 인출 되었습니다. 현재 잔액은 {account_object.balance}입니다.')
        return account_object.balance
    print('유효한 카드번호와 핀번호를 입력하세요')
    return


# is_valid_card(3285901382865019)
# is_valid_card_pin_number(3285901382865019, 1111)
# current_balance(3285901382865019, 1111)
# deposit(3285901382865019, 1111, 1)
# withdraw(3285901382865019, 1111, 10001)