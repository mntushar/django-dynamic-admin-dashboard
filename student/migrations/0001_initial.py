# Generated by Django 2.2.8 on 2021-07-31 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAcademicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, choices=[('psc', 'PSC'), ('jsc', 'JSC'), ('ssc', 'SSC'), ('hsc', 'HSC'), ('bsc-engineering', 'Bsc.Engineering'), ('m.engineering', 'M.Engineering'), ('d.engr.', 'D.Engr.'), ('doctor', 'Doctor'), ('md', 'MD'), ('ph.d', 'Ph.D'), ('b.sc.', 'B.sc.'), ('m.sc.', 'M.sc.'), ('bba', 'BBA'), ('mba', 'MBA'), ('ba', 'BA'), ('ma', 'Ma')], max_length=100, null=True)),
                ('last_passing_institution_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_passing_year', models.DateField(blank=True, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(blank=True, max_length=50, null=True)),
                ('village_name', models.CharField(blank=True, max_length=50, null=True)),
                ('post_office', models.CharField(blank=True, max_length=50, null=True)),
                ('thana_name', models.CharField(blank=True, max_length=50, null=True)),
                ('district_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'This email has already been registered.'}, max_length=100, null=True, unique=True)),
                ('designation', models.CharField(blank=True, choices=[('student', 'Student')], max_length=10, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_academic', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.UserAcademicInfo')),
                ('user_address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.UserAddressInfo')),
                ('user_basic', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.UserBasicInfo')),
            ],
        ),
    ]
