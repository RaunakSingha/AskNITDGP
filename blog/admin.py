from django.contrib import admin
from . models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish',)
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body', 'author')
    date_hierarchy = 'publish'
    ordering = ['-publish']
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'publish')
    list_filter = ('publish', )
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
