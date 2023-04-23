from rest_framework import serializers
from .models import *

class JobScheduledata(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = ['name','message','date','description']