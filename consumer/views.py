from django.http import JsonResponse
from rest_framework.generics import GenericAPIView


class ListUsers(GenericAPIView):
    def get(self, request):
        """
        Return a list of all users.
        """
        return JsonResponse({1:1})