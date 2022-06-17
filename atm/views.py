from atm.models import Card, Account

from rest_framework.views import APIView
from atm.serialers import CardSerializer, CardDetailSerializer, AccountSerializer, AccountDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from random import random
import math, hashlib
from atm.utils.commons import exception_handling


def account_number_generator():
    account_number = random()
    while account_number == 0.0:
        account_number = random()
    while True:
        try:
            Account.objects.get(account_number=account_number)
        except:
            return str(math.trunc(account_number * 100000000000000))


def card_number_generator():
    card_number = random()
    while card_number == 0.0:
        card_number = random()
    while True:
        try:
            Card.objects.get(card_number=card_number)
        except:
            return str(math.trunc(card_number*10**16))


def is_account_number_in_account(account_number):
    try:
        Account.objects.get(account_number=account_number)
    except:
        return False
    return True


class CardList(APIView):
    """
    List all cards, or create a new card.
    """
    def get(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        request = exception_handling(request)
        if not is_account_number_in_account(request['account_number']):
            return Response({'error_message': "유효한 계좌번호를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            card_number = card_number_generator()
            request.update({'card_number': card_number})
            serializer = CardSerializer(data=request)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error_message': "카드 생성1에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error_message': "카드 생성2에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)


class CardDetail(APIView):
    """
        get Card
    """
    def get_object(self, pk):
        pk = str(pk)
        return get_object_or_404(Card, card_number=pk)

    def get(self, request, pk, format=None):
        try:
            queryset = self.get_object(pk)
            serializer = CardDetailSerializer(queryset)
            return Response(serializer.data)
        except ValueError:
            return Response({'error_message': "요청하신 카드번호는 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if pk is None:
            return Response({'error_message': "invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            card_number = str(pk)
            card_object = Card.objects.get(card_number=card_number)
            card_object.delete()
            return Response({'success_message': "DELETE SUCCESS"}, status=status.HTTP_200_OK)


class AccountList(APIView):
    def get(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            account_number = account_number_generator()
            serializer = AccountSerializer(data={'account_number': account_number})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error_message': "계좌 개설이 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error_message': "계좌 개설이 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):

    def get_object(self, pk):
        pk = str(pk)
        return get_object_or_404(Account, account_number=pk)

    def get(self, request, pk, format=None):
        try:
            queryset = self.get_object(pk)
            serializer = AccountDetailSerializer(queryset)
            return Response(serializer.data)
        except ValueError:
            return Response({'error_message': "요청하신 계좌번호는 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(sel, request, pk):
        if pk is None:
            return Response({'error_message': "invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            account_number = str(pk)
            account_object = Account.objects.get(account_number=account_number)
            account_object.delete()
            return Response({'success_message': "DELETE SUCCESS"}, status=status.HTTP_200_OK)


class AccountBalanceDetail(APIView):
    pass