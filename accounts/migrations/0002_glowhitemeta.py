# Generated by Django 4.0.3 on 2022-03-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlowhiteMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=130, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
