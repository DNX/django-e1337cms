from django.contrib import admin
from e1337cms.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', )
    search_fields = ['title', 'content', ]
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Page, PageAdmin)