from atm.models import Card

from rest_framework.views import APIView
from atm.serialers import CardSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class CardList(APIView):
    """
    List all cards, or create a new card.
    """
    def get(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDetail(APIView):
    """
        get Card
    """
    def get_card(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except ValueError:
            return Response({'error_message': "요청하신 카드번호는 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

