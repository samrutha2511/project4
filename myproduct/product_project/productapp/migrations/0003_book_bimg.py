# Generated by Django 3.2.15 on 2022-09-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_auto_20220906_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bimg',
            field=models.ImageField(default='amrutha', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
