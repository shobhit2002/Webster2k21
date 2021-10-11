# Generated by Django 3.1 on 2021-10-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forgotpassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('token', models.CharField(max_length=500)),
                ('datastamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
