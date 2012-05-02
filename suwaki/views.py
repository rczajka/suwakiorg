import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from suwaki import api
from suwaki.models import Slider


def home(request):
    return render(request, "suwaki/home.html", {
        "sliders": Slider.objects.all(),
    })


def news(request):
    values = {}
    for dim in Slider.objects.all():
        try:
            val = int(request.GET[str(dim.pk)])
        except KeyError:
            continue
        except ValueError:
            continue
        values[dim.pk] = val
    chosen = api.get_relevant_news(values, settings.SUWAKI_MAX_NEWS)
    response_data = [n.to_dict() for n in chosen]
    return HttpResponse(json.dumps(response_data), mimetype="application/json")
