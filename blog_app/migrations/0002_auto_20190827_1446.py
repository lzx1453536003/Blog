# Generated by Django 2.2.3 on 2019-08-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='name'),
        ),
    ]
