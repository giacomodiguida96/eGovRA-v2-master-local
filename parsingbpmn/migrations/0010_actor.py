# Generated by Django 4.0.3 on 2022-03-18 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0009_remove_process_process_bpmn_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('process_bpmn_id', models.IntegerField(null=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.system')),
            ],
        ),
    ]