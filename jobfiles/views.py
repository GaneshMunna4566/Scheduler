from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from . serializers import *

@api_view(['GET'])
def getData(request):
    items = JobDetails.objects.all()
    serializer = JobScheduledata(items, many=True)
    return  Response(serializer.data)
# Create your views here.

@api_view(['POST'])
def JobPost(request):
    serializer = JobScheduledata(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
