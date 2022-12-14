# Generated by Django 4.0.3 on 2022-08-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('video', models.FileField(blank=True, null=True, upload_to='post_videos')),
                ('likes', models.IntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
