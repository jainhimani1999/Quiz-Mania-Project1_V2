# Generated by Django 2.2.5 on 2019-09-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizMania_V2', '0002_auto_20190920_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_phone',
            field=models.IntegerField(),
        ),
    ]