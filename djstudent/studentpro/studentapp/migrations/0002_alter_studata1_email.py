# Generated by Django 4.1.3 on 2023-06-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studata1',
            name='Email',
            field=models.EmailField(max_length=55),
        ),
    ]
