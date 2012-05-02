from django.contrib import admin
from suwaki.models import News, Slider, Value


class ValueInline(admin.TabularInline):
    model = Value

class SliderAdmin(admin.ModelAdmin):
    inlines = [ValueInline]


admin.site.register(News)
admin.site.register(Slider, SliderAdmin)
