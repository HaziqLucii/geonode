# Generated by Django 3.2.16 on 2022-10-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0007_alter_executionrequest_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='executionrequest',
            name='source',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]