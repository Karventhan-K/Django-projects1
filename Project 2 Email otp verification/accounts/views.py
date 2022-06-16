from ast import Not
import random
from traceback import print_tb
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from accounts.serializer import *
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from rest_framework import status
from django.contrib.auth import get_user_model
from library.response.response_messages import ApiResponseMessages
from library.response.api_response import CustomResponse
from library.utility.utility import Email
from rest_framework.generics import GenericAPIView
from django.utils import timezone
# from django.utils.timezone import datetime
import time
from datetime import datetime, date, time, timedelta

api_msg_obj = ApiResponseMessages()
User = get_user_model()


def user_more_then_24(time):
    return time + timedelta(hours=24) > timezone.now()


@permission_classes((AllowAny, ))
@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        create_serializer = UserCreateSerializer(data=request.data)

        if create_serializer.is_valid():
            otp = random.randint(1000, 9999)
            valid_phonenumber = User.objects.filter(
                phonenumber=create_serializer.data['phonenumber'])

            if valid_phonenumber:
                valid_phonenumber.update(
                    otp=otp, modified_by=timezone.now(), is_verified=False)
                email_template = render_to_string('otp.html',
                                                  {"otp": otp, "phonenumber": create_serializer.data['phonenumber']})
            else:
                User(
                    phonenumber=create_serializer.data['phonenumber'], otp=otp).save()
                email_template = render_to_string('otp.html',
                                                  {"otp": otp, "phonenumber": create_serializer.data['phonenumber']})
        try:
            Email.send_email(email_template, "OTP verification",
                             "karventhanalpm1999@gmail.com")
            status_code = status.HTTP_200_OK
            msg = api_msg_obj.signin_success

        except:
            msg = api_msg_obj.send_email_failure
            status_code = status.HTTP_408_REQUEST_TIMEOUT
        resp_json = CustomResponse.default_response(msg, status_code)
        return Response(resp_json, status=status_code)


@permission_classes([AllowAny, ])
class OtpVerifyView(GenericAPIView):
    serializer_class = OtpVerificationsSerializer

    def post(self, request):
        """
            This api verifies the newly created user account.
            :return: returns user account verification status message
        """
        otp_verify_serializer = OtpVerificationsSerializer(data=request.data)
        if otp_verify_serializer.is_valid():
            try:
                user = User.objects.get(
                    phonenumber=otp_verify_serializer.data['phonenumber'])
                if user.is_verified == False:
                    if user.otp == request.data['otp']:
                        user.is_verified = True
                        user.save()
                        msg = api_msg_obj.otp_verify
                        status_code = status.HTTP_200_OK
                    else:
                        msg = api_msg_obj.otp_send
                        status_code = status.HTTP_406_NOT_ACCEPTABLE
                else:
                    msg = api_msg_obj.otp_expried
                    status_code = status.HTTP_404_NOT_FOUND
            except:
                msg = api_msg_obj.phone_verify
                status_code = status.HTTP_502_BAD_GATEWAY
        else:
            msg = api_msg_obj.field_missing
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        resp_json = CustomResponse.default_response(msg, status_code)
        return Response(resp_json, status=status_code)


@permission_classes([AllowAny, ])
class LoginApiView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        login_serializer = UserCreateSerializer(data=request.data)

        if login_serializer.is_valid():
            try:
                user = User.objects.get(
                    phonenumber=login_serializer.data['phonenumber'])
                if user:
                    if user_more_then_24(user.modified_by):
                        try:
                            Token.objects.get(user=user).delete()
                        except:
                            pass
                        user_token = Token.objects.create(
                            user=user)
                        data = {
                            "Phone number": login_serializer.data["phonenumber"], "key": str(user_token)}

                        return Response(data)
                    else:
                        msg = api_msg_obj.need_phone_verify
                        status_code = status.HTTP_408_REQUEST_TIMEOUT
                else:
                    msg = api_msg_obj.phone_verify
                    status_code = status.HTTP_404_NOT_FOUND
            except:
                msg = api_msg_obj.field_missing
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        resp_json = CustomResponse.default_response(msg, status_code)
        return Response(resp_json, status=status_code)


@permission_classes([AllowAny, ])
class LogoutApiView(GenericAPIView):
    serializer_class = UserLogout

    def post(self, request):
        try:
            Token.objects.get(key=request.data['key']).delete()
            msg = api_msg_obj.success
            status_code = status.HTTP_200_OK
        except:
            msg = api_msg_obj.not_found
            status_code = status.HTTP_401_UNAUTHORIZED

        resp_json = CustomResponse.default_response(msg, status_code)
        return Response(resp_json, status=status.HTTP_200_OK)
