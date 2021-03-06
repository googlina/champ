# Generated by Django 3.2 on 2021-04-21 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('punch_in', models.DateField(unique_for_date=True)),
                ('punch_out', models.DateField()),
                ('logged_time', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On leave', 'On Leave')], default='Absent', max_length=20)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=40, unique=True)),
                ('created_by', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Left', 'Left'), ('Active', 'Active')], default='Active', max_length=30)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('separation_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100)),
                ('files', models.FileField(blank=True, null=True, upload_to='media/project_files')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='Pending', max_length=100)),
                ('completed_date', models.DateField(auto_now=True, null=True)),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='backend.employee')),
                ('assigned_to', models.ManyToManyField(related_name='_backend_project_assigned_to_+', to='backend.Employee')),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='User_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('todo', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('activity', models.CharField(max_length=200)),
                ('time_taken', models.CharField(max_length=5)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=500)),
                ('created_date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In process', 'In process'), ('Closed', 'Closed')], default='Pending', max_length=50)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('update_date', models.DateField()),
                ('closed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='backend.employee')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100)),
                ('files', models.FileField(blank=True, null=True, upload_to='media/project_files')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='Pending', max_length=100)),
                ('completed_date', models.DateField(auto_now=True, null=True)),
                ('assigned_to', models.ManyToManyField(related_name='_backend_task_assigned_to_+', to='backend.Employee')),
                ('leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='backend.employee')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.project')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Half day', 'Half day'), ('Short Leave', 'Short Leave'), ('Multiple days', 'Multiple days'), ('One day', 'One day')], max_length=50)),
                ('from_date', models.DateField()),
                ('remarks', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=30)),
                ('leave_balance', models.CharField(default=0, max_length=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.employee')),
            ],
        ),
    ]
