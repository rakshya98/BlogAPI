# Generated by Django 5.0 on 2023-12-20 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_category_category_name_alter_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]