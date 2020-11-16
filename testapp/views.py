from django.http import HttpResponse

from .models import TestModel

def index(request):
    list(TestModel.objects.all())
    return HttpResponse('ok')
