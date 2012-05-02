from django.db import models
from django.utils.translation import ugettext_lazy as _


class Slider(models.Model):
    name = models.CharField(_('name'), max_length=255)
    ordering = models.IntegerField(_('ordering'))

    class Meta:
        verbose_name = _('slider')
        verbose_name_plural = _('sliders')
        ordering = ['ordering']

    def __unicode__(self):
        return self.name


class Value(models.Model):
    slider = models.ForeignKey(Slider, verbose_name=_('slider'))
    name = models.CharField(_('name'), max_length=255)
    ordering = models.IntegerField(_('ordering'))

    class Meta:
        ordering = ['ordering']
        verbose_name = _('value')
        verbose_name_plural = _('values')

    def __unicode__(self):
        return "%s: %s" % (self.slider.name, self.name)


# Create your models here.
class News(models.Model):
    #flickr_img = models.CharField(_)
    value = models.ForeignKey(Value, verbose_name=_('value'))
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('text'))
    active = models.BooleanField(_('active'), default=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __unicode__(self):
        return self.title

    def to_dict(self):
        return {'title': self.title,
                'text': self.text,
                }
