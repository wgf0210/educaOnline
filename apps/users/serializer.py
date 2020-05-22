from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url','id','username','nick_name','birthday','gender','address','mobile','image')