from django.contrib import admin

from grappelli.forms import GrappelliSortableHiddenMixin

from .models import Section, Item


class ItemInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Item
    extra = 0

class SectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [ItemInline]
    list_display = ('name', 'position')
    list_editable = ['position']

    class Media:
        js = (
            'js/admin_list_reorder.js',
        )

admin.site.register(Section, SectionAdmin)
