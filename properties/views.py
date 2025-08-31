from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_all_properties

# Create your views here.
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({ "data": list(properties)}, safe=False)


# return JsonResponse({
# data: list(properties)
# }, safe=False)