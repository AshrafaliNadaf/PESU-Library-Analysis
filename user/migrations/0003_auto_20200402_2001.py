# Generated by Django 3.0.2 on 2020-04-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200325_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorsmodel',
            name='username',
        ),
        migrations.AlterField(
            model_name='newbookmodel',
            name='copies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='newbookmodel',
            name='edition',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='visitorsmodel',
            name='staff',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='visitorsmodel',
            name='students',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='visitorsmodel',
            name='visitors',
            field=models.PositiveIntegerField(default=0),
        ),
    ]