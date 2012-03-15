import json
from django.http import HttpResponse
from django.shortcuts import render
from suwaki.constants import dimensions, MAX_NEWS
from suwaki import api


def home(request):
    return render(request, "suwaki/home.html", {
        "dimensions": dimensions,
    })




def news(request):
    values = {}
    for dim in dimensions:
        try:
            val = int(request.GET[dim.slug])
        except KeyError:
            continue
        except ValueError:
            continue
        values[dim.slug] = val
    chosen = api.get_relevant_news(values)[:MAX_NEWS]
    response_data = [n.to_dict() for n in chosen]
    return HttpResponse(json.dumps(response_data), mimetype="application/json")
