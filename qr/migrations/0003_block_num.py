# Generated by Django 4.1.5 on 2023-01-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_remove_block_imag_remove_college_imag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='num',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]