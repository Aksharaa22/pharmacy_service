# Generated by Django 3.2 on 2021-06-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PharmSupply', '0004_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
