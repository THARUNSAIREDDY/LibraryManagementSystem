# Generated by Django 3.2.2 on 2021-06-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_avail',
            name='Book_Enterdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
