from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reader, User, Author

admin.site.register(User, UserAdmin)
admin.site.register(Author)
admin.site.register(Reader)