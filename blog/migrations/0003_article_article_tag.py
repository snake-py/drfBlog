# Generated by Django 3.2.9 on 2021-12-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(null=True, to='blog.ArticleTag'),
        ),
    ]
