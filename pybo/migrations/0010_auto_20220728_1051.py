# Generated by Django 3.1.3 on 2022-07-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_auto_20220725_1617'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='question',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
