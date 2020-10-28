# Generated by Django 2.2.12 on 2020-09-12 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0026_auto_20200905_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectToc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(verbose_name='文集文档层级目录')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doc.Project')),
            ],
            options={
                'verbose_name': '文集目录',
                'verbose_name_plural': '文集目录',
            },
        ),
    ]