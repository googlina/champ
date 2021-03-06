# Generated by Django 3.2 on 2021-04-21 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='location',
            field=models.ManyToManyField(to='main.Depot'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.designation'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='superwiser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='backend.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.user_type'),
        ),
        migrations.AddField(
            model_name='employee',
            name='work_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.depot'),
        ),
        migrations.AddField(
            model_name='designation',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.department'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.employee'),
        ),
    ]
