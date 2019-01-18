# Generated by Django 2.1.4 on 2019-01-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('update_date', models.DateTimeField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
