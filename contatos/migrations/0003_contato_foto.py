# Generated by Django 4.2.2 on 2023-07-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d'),
        ),
    ]
