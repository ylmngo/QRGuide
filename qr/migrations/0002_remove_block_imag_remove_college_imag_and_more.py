# Generated by Django 4.1.5 on 2023-01-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='imag',
        ),
        migrations.RemoveField(
            model_name='college',
            name='imag',
        ),
        migrations.RemoveField(
            model_name='floor',
            name='imag',
        ),
        migrations.AddField(
            model_name='block',
            name='img',
            field=models.CharField(default='qr/', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='img',
            field=models.CharField(default='qr/', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='floor',
            name='img',
            field=models.CharField(default='qr/', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='aimg',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='college',
            name='aimg',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='floor',
            name='aimg',
            field=models.CharField(max_length=64),
        ),
    ]