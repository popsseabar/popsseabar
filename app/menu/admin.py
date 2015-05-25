from django.contrib import admin

from grappelli.forms import GrappelliSortableHiddenMixin

from menu.models import Section, Item


class ItemInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Item
    extra = 0

class SectionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [ItemInline]
    # list_display = ('question', 'pub_date', 'was_published_recently')
    # list_filter = ['name']
    # search_fields = ['question']

admin.site.register(Section, SectionAdmin)
