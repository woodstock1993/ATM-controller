from rest_framework.response import Response
from rest_framework import status
from atm.models import Account
import hashlib


def _request_param(request):
    try:
        result = {
            'pin_number': request.data.get('pin_number', None),
            'account_number': request.data.get('account_number', None),
        }
    except ValueError:
        return Response({'error_message': "{pin_number: , account: } 형태로 입력하세요"}, status=status.HTTP_400_BAD_REQUEST)
    return result


def exception_handling(request):
    requests = _request_param(request)
    return requests
