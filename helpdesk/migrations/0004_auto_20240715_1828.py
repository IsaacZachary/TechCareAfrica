# Generated by Django 3.1.6 on 2024-07-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_auto_20240711_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='mensajito',
            field=models.CharField(default='¡Vacaciones! Bien merecidas', max_length=300),
        ),
    ]