from django.http import HttpResponse
from django.template import loader

from visualAdmin.models import Artwork


def bootstrap(request):
    latest_question_list = Artwork.objects.all()
    template = loader.get_template('bootstrap_test.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))