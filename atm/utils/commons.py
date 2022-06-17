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
    if requests['pin_number'] is None or requests['account_number'] is None:
        return Response({'error_message': "유효한 핀넘버와 계좌번호를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        pin_number = requests.get('pin_number')
        len(pin_number) != 6 and map(int, list(pin_number))
    except ValueError:
        return Response({'error_message': "핀넘버 6자리를 숫자로 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)

    requests['pin_number'] = hashlib.sha256(requests['pin_number'].encode('utf-8')).hexdigest()
    return requests
