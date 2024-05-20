from django.shortcuts import render
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_307_TEMPORARY_REDIRECT
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from urlshorter.services import generate_uuid
from urlshorter.models import Urls

# Create your views here.


class URLListView(GenericAPIView):
    def post(self, request):
        data = request.data.copy()
        long_url = data.get("long_url")
        if not long_url:
            return JsonResponse({"status": "error", "message": "Long url should be present"}, status=HTTP_400_BAD_REQUEST)
        random_uuid = generate_uuid()
        url = Urls.objects.create(short_url=random_uuid,full_url=long_url)
        return JsonResponse({"status": "success", "data": {"url": url.short_url}})



class URLRedirect(GenericAPIView):
    def get(self, request):
        data = request.GET.dict()
        short_url = data.get("short_url")
        url = Urls.objects.filter(short_url=short_url).last()
        if not url:
            return JsonResponse({"status": "error", "message": "Short url is missing! Please register first"}, status=HTTP_400_BAD_REQUEST)
        url.hit_count += 1
        url.save()
        return JsonResponse({"status": "success", "data": {"url": url.full_url}}, status=HTTP_307_TEMPORARY_REDIRECT)

   