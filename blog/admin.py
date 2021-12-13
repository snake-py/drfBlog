from django.contrib import admin


from .models import ArticleTag, Article, Comment


class ArticleTagInlineAdmin(admin.StackedInline):
    model = Article.tags.through

class ArticleTagAdmin(admin.ModelAdmin):
    model = ArticleTag

class ArticleCommentAdmin(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInlineAdmin, ArticleCommentAdmin]
    exclude = ('tags',)

admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(Article, ArticleAdmin)