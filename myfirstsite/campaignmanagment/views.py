from rest_framework import generics
from .campaignserializer import CampaignSerializer
from usermanagement.models import User
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from abc import  abstractmethod
from .models import Campaign
from django.utils import timezone
from datetime import datetime


# Create your views here.
class CampaignManager(generics.GenericAPIView):

    request = None
    request_data = None
    userid = None
    campaign_name = None
    campaign_id = None
    start_at = None
    end_at = None
    logintoken = None

    def check_userid_valid(self):

        query_set = User.objects.filter(user_id=self.userid, logintoken=self.logintoken)
        if bool(query_set):
            return True
        return False

    def set_request_and_data(self, request):
        self.request = request
        self.request_data = self.request.data

    def set_campaign_parameters(self):
        self.set_userid()
        self.set_campaign_name()
        self.set_startat()
        self.set_endat()
        self.set_logintoken()
        self.set_campaign_id()

    @abstractmethod
    def set_campaign_id(self):
        pass

    def set_userid(self):
        try:
            self.userid = self.request_data["created_by"]
        except KeyError:
            self.userid = None
            raise APIException("User id is must for campaign management API's")

    def set_campaign_name(self):
        try:
            self.campaign_name = self.request_data["campaign_name"]
        except KeyError:
            self.campaign_name = None

    def set_startat(self):
        try:
            self.start_at = self.request_data["start_at"]
        except KeyError:
            self.start_at = None

    def set_endat(self):
        try:
            self.end_at = self.request_data["end_at"]
        except KeyError:
            self.end_at = None

    def set_logintoken(self):
        try:
            self.logintoken = self.request_data["logintoken"]
        except KeyError:
            self.logintoken = None

    def get_userid(self):
        return self.userid

    def get_campaign_name(self):
        return self.campaign_name

    def get_start_at(self):
        return self.start_at

    def get_end_at(self):
        return self.end_at

    def get_logintoken(self):
        return self.logintoken

    def get_campaign_id(self):
        return self.campaign_id

    def handle_exception(self, exc):
        response_message = {
            "message": "Some parameter is missing.",
            "response_code": 444,
            "exact_message": str(exc)
        }

        return Response(data=response_message, status=201)


class CreateCampaign(CampaignManager, generics.CreateAPIView):

    serializer_class = CampaignSerializer

    def create(self, request, *args, **kwargs):

        self.set_request_and_data(request)
        serializer = self.get_serializer(data=self.request_data)
        self.set_campaign_parameters()

        if self.check_userid_valid():
            if serializer.is_valid():
                serializer.save()
                return Response(data={"message": "Campaign created successfully.", "response_code": 222}, status=201)

        return Response(data={"message": "Campaign not created, user not authenticated.", "response_code": 444},
                        status=201)

    def set_campaign_id(self):
        try:
            self.campaign_id = self.request_data["campaign_id"]
        except KeyError:
            self.campaign_id = None


class UpdateCampaign(CampaignManager, generics.RetrieveUpdateAPIView):

    serializer_class = CampaignManager

    def update(self, request, *args, **kwargs):

        self.set_request_and_data(request)
        self.set_campaign_parameters()

        query_set = self.get_queryset()

        if self.check_userid_valid():
            print(self.get_update_dict())
            print(query_set.query)
            query_set.update(**self.get_update_dict())
            return Response(data={"message": "Campaign updated successfully.", "response_code": 222}, status=201)
        else:
            return Response(
                data={"message": "User not found or logintoken doesn't match or campaign doesn't exists..", "response_code": 444},
                status=201)

    def get_queryset(self):
        return Campaign.objects.filter(created_by=self.get_userid(),campaign_id=self.get_campaign_id())

    def set_campaign_id(self):
        try:
            self.campaign_id = self.request_data["campaign_id"]
        except KeyError:
            self.campaign_id = None
            raise APIException("Camapign id is required in updating campaign.")

    def get_update_dict(self):

        update_dict = {}

        if self.get_campaign_name() is not None:
            update_dict["campaign_name"] = self.get_campaign_name()

        if self.get_start_at() is not None:
            update_dict["start_at"] = self.get_start_at()

        if self.get_end_at() is not None:
            update_dict["end_at"] = self.get_end_at()

        update_dict["updated_at"] = datetime.now()

        return update_dict

    def handle_exception(self, exc):
        response_message = {
            "message": "Some parameter is missing.",
            "response_code": 444,
            "exact_message": str(exc)
        }

        return Response(data=response_message, status=201)