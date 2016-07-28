from django.shortcuts import render_to_response
from django.template import RequestContext


def custom_handler404(request):
    response = render_to_response('404.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response