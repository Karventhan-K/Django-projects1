from rest_framework.authtoken.models import Token
from rest_framework import serializers
from accounts.models import User

class UserCreateSerializer(serializers.Serializer):
    phonenumber = serializers.CharField(required=True, allow_null=False)
    class Meta:
        model = User
        fields = ('phonenumber',"otp",)

    def create(self, validated_data):
        phonenumber = validated_data['phonenumber']
        try:
            user = super(UserCreateSerializer, self).create(validated_data)
        except:
            raise phonenumber + " already exists"
        return user

class OtpVerificationsSerializer(serializers.Serializer):
    phonenumber = serializers.CharField(required=True, allow_null=False)
    otp = serializers.CharField(required=True, allow_null=False)


class UserLogout(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)    