# Generated by Django 2.2.6 on 2019-10-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='linha2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]