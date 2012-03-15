from django.template import Library

register = Library()

@register.simple_tag
def stop_pos(counter, items):
    print counter
    length = len(items)
    width = 100.0 / (length - 1)
    left = (counter - 1.5) * width
    return "left: %.2f%%; width: %.2f%%" % (left, width)
