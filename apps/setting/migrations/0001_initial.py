# Generated by Django 3.1.5 on 2022-04-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('office_address', models.TextField()),
            ],
            options={
                'verbose_name': 'Company Address',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo')),
            ],
            options={
                'verbose_name': 'Company Logo',
            },
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('google_analytics', models.TextField()),
            ],
            options={
                'verbose_name': 'SEO',
            },
        ),
        migrations.CreateModel(
            name='SocialSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('youtube', models.CharField(max_length=255)),
                ('tripadviser', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Social Setting',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Company Title',
            },
        ),
    ]