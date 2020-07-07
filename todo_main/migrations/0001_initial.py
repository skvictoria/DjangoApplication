# Generated by Django 3.0.8 on 2020-07-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbTodolist',
            fields=[
                ('idnew_table', models.AutoField(primary_key=True, serialize=False)),
                ('todo_title', models.CharField(blank=True, max_length=300, null=True)),
                ('todo_date', models.DateTimeField(blank=True, null=True)),
                ('todo_contents', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'tb_todolist',
                'managed': False,
            },
        ),
    ]
