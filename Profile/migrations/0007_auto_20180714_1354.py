# Generated by Django 2.0 on 2018-07-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_auto_20180714_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='imag/shailesh.png', upload_to='cover_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='imag/shailesh.png', upload_to='profile_images'),
        ),
    ]