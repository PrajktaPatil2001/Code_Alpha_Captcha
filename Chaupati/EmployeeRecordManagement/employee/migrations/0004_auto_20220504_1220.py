# Generated by Django 3.1.3 on 2022-05-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20220503_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeentry',
            name='salary',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeeentry',
            name='photo',
            field=models.FileField(null=True, upload_to='media/empimg'),
        ),
    ]
