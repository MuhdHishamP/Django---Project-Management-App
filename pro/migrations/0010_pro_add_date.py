# Generated by Django 4.2.3 on 2023-09-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0009_remove_pro_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro_add',
            name='date',
            field=models.DateField(default=None, null=True),
        ),
    ]
