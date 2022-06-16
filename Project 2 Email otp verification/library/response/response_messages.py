from django.utils.translation import gettext_lazy as _

class ApiResponseMessages:
    def __init__(self):

        self.send_email_failure = u"Application failed to send to email."
        self.signin_success = u"OTP has been sent successfully!."
        self.otp_verify = u"Your OTP has been verified successfully."
        self.otp_send = u"Please check your otp again."
        self.otp_expried = u"Your OTP has been expired."
        self.phone_verify = u"Please check your phone number again."
        self.need_phone_verify = u"You need to verify your phone number."

        self.field_missing = _(u'Invalid request! or fields are missing!'),
        self.success = u"Your account logout successfully."
        self.not_found = u"User details not found."