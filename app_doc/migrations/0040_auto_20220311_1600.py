# Generated by Django 2.2.24 on 2022-03-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0039_auto_20211013_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='name',
            field=models.CharField(max_length=255, verbose_name='文档标题'),
        ),
    ]