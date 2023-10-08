from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper
admin.site.empty_value_display = 'Не задано'

admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(Category)


class IceCreamAdmin(admin.ModelAdmin):
    empty_value_display = 'Не задано'
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(IceCream, IceCreamAdmin)
