# Generated by Django 5.0.6 on 2024-05-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='mensajito',
            field=models.CharField(default='Vuelve cuando puedas :)', max_length=300),
        ),
    ]