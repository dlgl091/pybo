# Generated by Django 3.1.3 on 2022-07-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_question_imgfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='Uploaded Files/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='imgfile',
        ),
    ]
