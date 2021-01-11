from django.contrib import admin

# Register your models here.
from .models import Post, Comment
class CommentAdmin(admin.ModelAdmin):
   list_display = ('name', 'post', 'created', 'active')
   list_filter = ('active', 'created')
   search_fields = ('name','body')
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
