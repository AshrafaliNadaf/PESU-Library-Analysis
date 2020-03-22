# Generated by Django 3.0.2 on 2020-03-22 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200322_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookirmodel',
            name='usertype',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.loginmodel'),
        ),
        migrations.AddField(
            model_name='departments',
            name='usertype',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.loginmodel'),
        ),
        migrations.AddField(
            model_name='visitorsmodel',
            name='usertype',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.loginmodel'),
        ),
    ]