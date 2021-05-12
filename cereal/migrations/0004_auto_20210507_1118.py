# Generated by Django 3.2 on 2021-05-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0003_alter_cereal_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cereal',
            name='category',
        ),
        migrations.AddField(
            model_name='cereal',
            name='category',
            field=models.ManyToManyField(to='cereal.CerealCategory'),
        ),
    ]
