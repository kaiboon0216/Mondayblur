# Generated by Django 2.2 on 2019-05-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0008_comment_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='percentage',
            field=models.FloatField(default=0),
        ),
    ]