from django.conf import settings
from django.db.models import Q
from suwaki.constants import Dimension
from suwaki.models import News


TOLERANCE = settings.SUWAKI_TOLERANCE

def get_relevant_news(values):
    news = News.objects.filter(active=True).order_by('?')
    for slug, value in values.items():
        news = news.filter(**{
            "%s__range" % Dimension.build_field_name(slug): (value - TOLERANCE, value + TOLERANCE),
        })
    return news
