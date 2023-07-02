from django.contrib import admin

# Register your models here.
from myapp.models import Classification, Book, Tag, User, Comment

admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Comment)
