from django.http import HttpResponse
from .models import Card


def index(request):
    lastest_card_list = Card.objects.order_by('-created_at')[:20]
    output = ', '.join([p.name for p in lastest_card_list])
    return HttpResponse(output)


def detail(request, card_id):
    return HttpResponse("You're looking at card %s." % card_id)