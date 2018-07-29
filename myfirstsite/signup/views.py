from rest_framework import generics
from rest_framework import response
from .signupserializer import SignUpSerializer
from rest_framework.exceptions import APIException


# Create your views here.
class SignUp(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def perform_create(self, serializer):
        data = self.request.data

        if self.checkusername(data['username']):
            if self.checkemail(data['useremail']):
                if self.checkpassword(data['userpassword']):
                    serializer.save()
                else:
                    raise APIException("Invalid password.")
            else:
                raise APIException("Invalid email id.")
        else:
            raise APIException("Invalid username.")

        return

    @staticmethod
    def checkusername(username):
        if len(username) > 10:
            return False
        return True

    @staticmethod
    def checkemail(useremail):
        return len(useremail) > 5

    @staticmethod
    def checkpassword(userpassword):

        if len(userpassword) > 8:
            return True
        return False

    def handle_exception(self, exc):

        response_message = {
            "message": str(exc),
            "status": "error"
        }

        return response.Response(data=response_message, status=401)
