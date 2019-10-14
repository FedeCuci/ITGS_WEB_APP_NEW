# Generated by Django 2.2.6 on 2019-10-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='choices',
            field=models.ManyToManyField(to='users.Choices'),
        ),
    ]
