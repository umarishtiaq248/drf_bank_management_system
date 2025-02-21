from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import BankSerializer
from .models import Bank

@api_view(['GET'])
def bank_view(request):
    if request.method=='GET':
        bank = Bank.objects.all()
        serializer = BankSerializer(bank,many=True)
        return Response(serializer.data)

