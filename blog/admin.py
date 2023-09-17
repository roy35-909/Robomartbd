from django.contrib import admin
from .models import Blog,Comment,Pages,BlogTag,BlogCategory
from froala_editor.widgets import FroalaEditor
class PageInline(admin.TabularInline):
    #content = admin.CharField(widget=FroalaEditor)
    model = Pages
    extra = 1
    class Media:
        js = ['code_insert.js']
        css={'all':['code.css']}
        

class BlogAdmin(admin.ModelAdmin):
    inlines=[PageInline]
    class Meta:
        model = Blog


admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Pages)