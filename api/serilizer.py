from rest_framework import serializers
from api.models import *



class SerUserReferalRecord(serializers.ModelSerializer):
    userRefer=serializers.ReadOnlyField(source="userReferenceId.fname")
    userClick=serializers.ReadOnlyField(source="userClickId.fname")
    userClickEmail=serializers.ReadOnlyField(source="userClickId.email")
    class Meta:
        model = UserReferalRecord
        
        fields = ['userRefer','userClick','userClickEmail','status','discountlink']
