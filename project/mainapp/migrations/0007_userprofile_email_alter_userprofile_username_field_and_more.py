# Generated by Django 5.2.1 on 2025-06-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='-', max_length=150),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='USERNAME_FIELD',
            field=models.CharField(default='nuill', max_length=150),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
