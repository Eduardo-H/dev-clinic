# Generated by Django 3.0.7 on 2020-09-24 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('marca', models.CharField(blank=True, max_length=60)),
                ('quantidade', models.BigIntegerField()),
            ],
        ),
    ]
