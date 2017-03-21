from cms.models import Pages
from django.http import HttpResponse

# Create your views here.


def show(request):
    content = Pages.objects.all()
    response = ""
    for entry in content:
        response = entry.name + " => " + entry.page + "<br>" + response
    return HttpResponse(response)


def entry(request, identifier):
    entry = Pages.objects.get(id=identifier)
    response = "La página solicitada es:" + "<br>" + entry.name + \
               " => " + entry.page
    return HttpResponse(response)


def error(request):
    response = "La página solicitada no se encuentra en la base de datos"
    return HttpResponse(response)
