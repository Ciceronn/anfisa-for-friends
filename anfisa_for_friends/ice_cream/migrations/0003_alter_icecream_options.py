# Generated by Django 3.2.16 on 2023-10-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20231010_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ('output_order', 'title'), 'verbose_name': 'мороженое', 'verbose_name_plural': 'Мороженое'},
        ),
    ]