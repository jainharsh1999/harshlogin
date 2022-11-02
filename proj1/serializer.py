from rest_framework import serializers
from .models import *

class DemoSerial(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('email','password')
        
        