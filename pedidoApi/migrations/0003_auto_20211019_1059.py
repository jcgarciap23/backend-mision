# Generated by Django 3.0.8 on 2021-10-19 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedidoApi', '0002_auto_20211018_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='idpcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idproveedor',
            field=models.IntegerField(),
        ),
    ]
