# Generated by Django 3.0.8 on 2020-10-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdfmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('subjectcode', models.CharField(max_length=10)),
                ('pdffile', models.FileField(upload_to='pdfs')),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='images')),
                ('subjectcode', models.CharField(max_length=10)),
            ],
        ),
    ]
