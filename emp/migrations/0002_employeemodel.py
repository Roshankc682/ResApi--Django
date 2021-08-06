# Generated by Django 3.1.1 on 2020-10-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
