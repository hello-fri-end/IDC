# Generated by Django 3.0.5 on 2020-05-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0003_club_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='displayImage',
            field=models.ImageField(default='defaultProject.png', upload_to='images/clubs'),
        ),
    ]
