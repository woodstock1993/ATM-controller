from atm.models import Card, Account

from rest_framework.views import APIView
from atm.serialers import CardSerializer, AccountSerializer, AccountDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


def get(request):
    queryset = Card.objects.all()
    serializer = CardSerializer(queryset, many=True)
    return Response(serializer.data)


def post(request):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardList(APIView):
    """
    List all cards, or create a new card.
    """


class CardDetail(APIView):
    """
        get Card
    """

    def get_object(self, pk):
        try:
            pk = str(pk)
            return Card.objects.get(pk=pk)
        except ValueError:
            return Response({'error_message': "요청하신 카드번호는 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


def post(request):
    account_number = request.data['account_number']
    if account_number is None:
        return Response({'error_message': "14자리 숫자를 문자형태로 입력하시오"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        (map(int, list(account_number)))
        if len(account_number) != 14:
            return Response({'error_message': "14자리 숫자를 문자형태로 입력하시오"}, status=status.HTTP_400_BAD_REQUEST)
        if Account.objects.get(account_number=account_number):
            return Response({'error_message': "다른 계좌번호를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ValueError:
        return Response({'error_message': "14자리 숫자를 문자형태로 입력하시오"}, status=status.HTTP_400_BAD_REQUEST)


class AccountList(APIView):
    def get(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)


def delete(request, **kwargs):
    if kwargs.get('pk') is None:
        return Response({'error_message': "invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        account_number = kwargs.get('pk')
        account_object = Account.objects.get(account_number=account_number)
        account_object.delete()
        return Response({'success_message': "DELETE SUCCESS"}, status=status.HTTP_200_OK)


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
