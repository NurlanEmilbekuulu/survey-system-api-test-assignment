# Generated by Django 4.0.2 on 2022-02-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_choice_remove_answer_body_remove_answer_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
