# Generated by Django 3.2.2 on 2021-06-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_App', '0002_books_avail_book_enterdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_avail',
            name='Time',
            field=models.CharField(default='', max_length=120),
        ),
    ]
