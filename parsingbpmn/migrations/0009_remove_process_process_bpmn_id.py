# Generated by Django 4.0.3 on 2022-03-18 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0008_process_process_bpmn_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='process_bpmn_id',
        ),
    ]
