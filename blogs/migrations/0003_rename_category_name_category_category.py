# Generated by Django 5.0 on 2023-12-20 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_category_alter_blog_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
    ]