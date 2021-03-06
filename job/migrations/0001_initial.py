# Generated by Django 3.2.7 on 2021-10-02 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('status', models.CharField(choices=[('created', 'создана'), ('in_progress', 'в исполнении'), ('canceled', 'отменена'), ('executed', 'выполнена')], max_length=16, verbose_name='статус')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='подробное описание')),
                ('finished_at', models.DateTimeField(blank=True, null=True, verbose_name='время окончания')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to='employee.employee', verbose_name='создатель')),
                ('executors', models.ManyToManyField(related_name='executors', to='employee.Employee', verbose_name='исполнители')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('name', models.CharField(help_text='Например, "разработка приложения для Burger King".', max_length=64, verbose_name='название проекта')),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('created', 'создана'), ('in_progress', 'в исполнении'), ('canceled', 'отменена'), ('executed', 'выполнена')], max_length=16, verbose_name='статус')),
                ('tasks', models.ManyToManyField(to='job.Task', verbose_name='задачи')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
