# Generated by Django 3.1.3 on 2022-05-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20220511_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeentry',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='empimg-'),
        ),
    ]