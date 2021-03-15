from django.http import HttpResponse
from django.template import loader


def index(request):    
    template = loader.get_template('platform_/index.html')
    context = { }
    return HttpResponse(template.render(context, request))