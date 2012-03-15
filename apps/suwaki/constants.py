from collections import namedtuple
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

MAX_NEWS = settings.SUWAKI_MAX_NEWS

class Dimension(namedtuple('Dimension', 'slug name stops')):
    __slots__ = ()

    @staticmethod
    def build_field_name(slug):
        return "dimension_%s" % (slug,)

    def field_name(self):
        return self.build_field_name(self.slug)


dimensions = [
    Dimension('length', _("Copyright length"), [
        _('none'),
        _('a month'),
        _('a year'),
        _('10 years'),
        _('50 years'),
        _('200 years'),
        _('forever'),
    ]),
    Dimension('control', _("Level of control"), [
        _('attribution is enough'),
        _('have to pay sometimes'),
        _('commercial reuse needs permission'),
        _('uncommercial sharing is OK'),
        _('personal use is OK'),
        _('permission needed for everything'),
    ]),
    Dimension('enforcement', _("Level of enforcement"), [
        _('the law is ignored'),
        _('applies only to big players'),
        _('companies must be wary'),
        _('site owners, bloggers get busted'),
        _('people get sued over lolcats'),
        _('not one illegal copy gets through'),
    ]),
    Dimension('severity', _("Severity of punishment for infringement"), [
        _('apology'),
        _('symbolic compensation'),
        _('cutting off the net'),
        _('huge fines'),
        _('prison'),
    ]),
]
