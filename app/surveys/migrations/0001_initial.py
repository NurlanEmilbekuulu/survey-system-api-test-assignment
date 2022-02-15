# Generated by Django 4.0.2 on 2022-02-15 04:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('publish_date', models.DateField(default=datetime.date.today, editable=False, verbose_name='Publication date')),
                ('expire_date', models.DateField(default=datetime.date.today, verbose_name='Expiration date')),
            ],
            options={
                'verbose_name': 'Survey',
                'verbose_name_plural': 'Surveys',
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='surveys.survey')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('type', models.CharField(choices=[('text', 'text'), ('single', 'Select single'), ('multiple', 'Select multiple')], default='text', max_length=200, verbose_name='Type')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='surveys.survey')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveys.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveys.response')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
