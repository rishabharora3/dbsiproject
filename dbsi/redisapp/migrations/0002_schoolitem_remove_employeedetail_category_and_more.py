# Generated by Django 4.0.5 on 2022-07-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redisapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolItem',
            fields=[
                ('dbn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=100)),
                ('boro', models.CharField(max_length=1)),
                ('overview_paragraph', models.TextField()),
                ('school_10th_seats', models.IntegerField()),
                ('academicopportunities1', models.CharField(max_length=100)),
                ('academicopportunities2', models.CharField(max_length=100)),
                ('ell_programs', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('building_code', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('fax_number', models.CharField(max_length=100)),
                ('school_email', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('subway', models.CharField(max_length=100)),
                ('bus', models.CharField(max_length=100)),
                ('grades2018', models.CharField(max_length=100)),
                ('finalgrades', models.CharField(max_length=100)),
                ('total_students', models.IntegerField()),
                ('extracurricular_activities', models.CharField(max_length=100)),
                ('school_sports', models.CharField(max_length=100)),
                ('attendance_rate', models.CharField(max_length=100)),
                ('pct_stu_enough_variety', models.CharField(max_length=100)),
                ('pct_stu_safe', models.CharField(max_length=100)),
                ('school_accessibility_description', models.CharField(max_length=100)),
                ('directions1', models.CharField(max_length=100)),
                ('requirement1_1', models.CharField(max_length=100)),
                ('requirement2_1', models.CharField(max_length=100)),
                ('requirement3_1', models.CharField(max_length=100)),
                ('requirement4_1', models.CharField(max_length=100)),
                ('requirement5_1', models.CharField(max_length=100)),
                ('offer_rate1', models.CharField(max_length=100)),
                ('program1', models.CharField(max_length=100)),
                ('code1', models.CharField(max_length=100)),
                ('interest1', models.CharField(max_length=100)),
                ('method1', models.CharField(max_length=100)),
                ('seats9ge1', models.IntegerField()),
                ('grade9gefilledflag1', models.CharField(max_length=100)),
                ('grade9geapplicants1', models.IntegerField()),
                ('seats9swd1', models.IntegerField()),
                ('grade9swdfilledflag1', models.CharField(max_length=100)),
                ('grade9swdapplicants1', models.IntegerField()),
                ('seats101', models.CharField(max_length=100)),
                ('admissionspriority11', models.CharField(max_length=100)),
                ('admissionspriority21', models.CharField(max_length=100)),
                ('admissionspriority31', models.CharField(max_length=100)),
                ('grade9geapplicantsperseat1', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='category',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='EmployeeDetail',
        ),
    ]