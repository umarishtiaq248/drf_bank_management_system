from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from .serializers import BankSerializer
from .models import Bank

@api_view(['GET','POST'])
def bank_view(request):
    if request.method=='GET':
        bank = Bank.object.all()
        serializer = BankSerializer(bank,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

