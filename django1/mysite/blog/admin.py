from django.contrib import admin
from blog.models import Blog, Core, Servant, Praise, Sermon

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Core)
admin.site.register(Servant)
admin.site.register(Praise)
admin.site.register(Sermon)