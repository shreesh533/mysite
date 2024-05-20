from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import bad_request
from rest_framework.status import HTTP_400_BAD_REQUEST
from consumer.serializers import UserSerilizer
from consumer.models import User


class ListUsers(GenericAPIView):
    def get(self, request):
        """
        Return a list of all users.
        """
        params = request.GET.dict().copy()
        phone = params.get("phone")
        if not phone:
            return JsonResponse({"status": "success", "data": f"Phone Required"}, status=HTTP_400_BAD_REQUEST)
        users = User.objects.filter(phone=phone)
        user_serializer = UserSerilizer(users, many=True)
        return JsonResponse({"status": "success", "data": user_serializer.data})


    def post(self, request):
        """
        Return a list of all users.
        """
        payload = request.data
        phone = payload.get("phone")
        first_name = payload.get("first_name")
        last_name = payload.get("last_name")
        
        if not phone or not first_name or not last_name:
            return JsonResponse({"status": "success", "data": f"Phone Required"}, status=HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(phone=phone, first_name=first_name, last_name=last_name)
        return JsonResponse({"status": "success", "data": f"User {user.id} created"})