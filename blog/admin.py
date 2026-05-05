from django.contrib import admin
from blog.models import Tag, Post, Comment
from blog.models import Tag, Post, Comment, AuthorProfile

admin.site.register(AuthorProfile)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)