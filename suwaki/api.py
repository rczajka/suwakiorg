from itertools import chain
import random
from suwaki.models import News, Slider, Value


def get_relevant_news(values, max_news):
    channels = []
    for i, v in values.items():
        try:
            channel = Slider.objects.get(pk=int(i)).value_set.get(pk=int(v)
                ).news_set.filter(active=True).order_by('?')[:max_news]
        except (News.DoesNotExist, Slider.DoesNotExist, Value.DoesNotExist):
            pass
        else:
            channels.append(channel)
    if channels:
        random.shuffle(channels)
        return list(chain.from_iterable(zip(*channels)))[:max_news]
    return []
