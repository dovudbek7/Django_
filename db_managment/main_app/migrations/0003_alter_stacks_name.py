# Generated by Django 4.1.5 on 2023-03-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stacks',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
