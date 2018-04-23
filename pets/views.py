from django.http import HttpResponse
from .models import Pet


def index(request):
    response = Pet.objects.all()
    return HttpResponse(response)
