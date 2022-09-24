from django.http import Http404
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from TestApp.models import UserProfile
from TestApp.serializer import UserProfileSerializer


class UserView(APIView):

    permission_classes = (IsAuthenticated,)



    def get_objects(self, pk):
        try:
            return UserProfile.objects.get(pk = pk)
        except:
            if UserProfile.DoesNotExist:
                raise Http404


    def get(self, request, pk , format= None):

        User = self.get_objects(pk)
        serializer = UserProfileSerializer(User)
        return Response(serializer.data)

class UserRegister(APIView):

    '''User will get registered with this view'''

    def post(self, request, format = None):
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data = data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
        return Response(serializer.data)




