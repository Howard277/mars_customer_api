from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.views.decorators.http import require_POST, require_GET
from django.core import serializers
import json


# Create your views here.
@require_GET
def health(request):
    return HttpResponse(json.dumps({'status': 'UP'}), content_type="application/json")


@require_GET
def get_customer_info(request):
    id = request.GET['id']
    return HttpResponse(serializers.serialize("json", Customer.objects.get(id=id)),
                        content_type="application/json")
