# Generated by Django 2.1.7 on 2019-04-04 21:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import employees.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), employees.models.max_value_current_year])),
                ('total_marks', models.PositiveIntegerField()),
                ('obtained_marks', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=employees.models.user_directory_path, verbose_name='Profile Picture')),
                ('temporary_address', models.CharField(max_length=200, verbose_name='Temporary Address')),
                ('permanent_address', models.CharField(max_length=200, verbose_name='Permanent Address')),
                ('linkdin_url', models.URLField(max_length=60, verbose_name='Linkdin URL')),
                ('facebook_url', models.URLField(blank=True, max_length=60, verbose_name='Facebook URL')),
                ('github_url', models.URLField(blank=True, max_length=60, verbose_name='Github URL')),
                ('father_name', models.CharField(max_length=50)),
                ('father_cnic', models.CharField(max_length=13)),
                ('fathers_phone_no', models.CharField(default='0000000', max_length=11)),
                ('verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='RecordImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('cnic', 'CNIC'), ('domicile', 'Domicile'), ('metric', 'Metric Certificate'), ('intermediate', 'Intermediate Certificate'), ('graduation', 'Graduation Certificate'), ('other', 'Other Documents')], max_length=15)),
                ('image', models.ImageField(upload_to=employees.models.employee_certificates_path, verbose_name='Document Photo')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='educationrecord',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee'),
        ),
    ]
