from django.http import Http404
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from TestApp.models import UserProfile
from TestApp.serializer import UserProfileSerializer
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from Test import settings
from django.utils.decorators import method_decorator


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



@cache_page(900)
def homepage(request):
    return HttpResponse("Hello world")

# @method_decorator(cache_page(60 * 5), name = 'UserView')
class UserView(APIView):

    # permission_classes = (IsAuthenticated,)

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




