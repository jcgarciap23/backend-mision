# Generated by Django 3.0.8 on 2021-10-18 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idpedido', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('total', models.FloatField(default=0)),
                ('totalHours', models.FloatField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('1', 'Por hacer'), ('2', 'En proceso'), ('3', 'Terminado')], default='1', max_length=1)),
                ('invoiceNumber', models.IntegerField(null=True)),
            ],
        ),
    ]