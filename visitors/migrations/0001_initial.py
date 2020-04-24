# Generated by Django 3.0.2 on 2020-04-24 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitorsmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('students', models.PositiveIntegerField(default=0)),
                ('staff', models.PositiveIntegerField(default=0)),
                ('visitors', models.PositiveIntegerField(default=0)),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='register.loginmodel', to_field='username')),
            ],
        ),
    ]
