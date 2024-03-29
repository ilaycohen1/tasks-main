# Generated by Django 4.2.7 on 2024-01-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBasic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('dateCreated', models.CharField(max_length=256)),
                ('dueDate', models.CharField(max_length=256)),
                ('notes', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('users', models.ManyToManyField(related_name='tasks', to='tasksApp.userbasic')),
            ],
        ),
    ]
