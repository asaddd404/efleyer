# admin.py
from django.contrib import admin
from .models import *

# Inline для SliderContent, привязанного к Fashion
class SliderContentInline(admin.TabularInline):
    model = SliderContent
    extra = 0
    max_num = 3  # Ограничение на 3 элемента

# Inline для SliderContent2, привязанного к Electronic
class SliderContentInline2(admin.TabularInline):
    model = SliderContent2
    extra = 0
    max_num = 3  # Ограничение на 3 элемента

class SliderContentInline3(admin.TabularInline):
    model = SliderContent3
    extra = 0
    max_num = 3  # Ограничение на 3 элемента

# Админ-класс для Fashion с инлайном SliderContent
class FashionAdmin(admin.ModelAdmin):
    inlines = [SliderContentInline]

# Админ-класс для Electronic с инлайном SliderContent2
class ElectronicAdmin(admin.ModelAdmin):
    inlines = [SliderContentInline2]


class AccessoriesAdmin(admin.ModelAdmin):
    inlines = [SliderContentInline3]



admin.site.register(Fashion, FashionAdmin)
admin.site.register(Electronic, ElectronicAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Start)

