# Generated by Django 3.1.7 on 2021-03-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210305_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/', upload_to='images/'),
        ),
    ]