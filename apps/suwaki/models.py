from django.db import models
from django.utils.translation import ugettext_lazy as _
from suwaki.constants import dimensions



# Create your models here.
class News(models.Model):
    #flickr_img = models.CharField(_)
    title = models.CharField(_('title'), max_length=255)
    text = models.TextField(_('title'))
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

# add dimension fields
for dim in dimensions:
    models.IntegerField(dim.name).contribute_to_class(News, dim.field_name())

