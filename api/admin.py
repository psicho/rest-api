from django.contrib import admin
from .models import *


class TopModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'children',)


class OneInnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'children',)


class TwoInnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'children',)


class ThreeInnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ModelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'children')


admin.site.register(TopModel)
admin.site.register(ThreeInner)
admin.site.register(TwoInner)
admin.site.register(OneInner)
admin.site.register(Models)
