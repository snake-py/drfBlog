from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reader, User, Author

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reader, User, Author


class ReaderInlineAdmin(admin.StackedInline):
    model = Reader

class AuthorCommentAdmin(admin.TabularInline):
    model = Author


class UserAdminCustom(UserAdmin):
    inlines = [AuthorCommentAdmin, ReaderInlineAdmin]
    readonly_fields = ('date_joined', 'last_login')

admin.site.register(User, UserAdminCustom)
