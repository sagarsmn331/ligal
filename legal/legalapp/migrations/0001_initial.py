# Generated by Django 3.0.6 on 2020-06-15 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(blank=True, max_length=70, null=True)),
                ('amount', models.IntegerField()),
                ('discount', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField()),
                ('plans', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Previous_Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('transection_id', models.CharField(blank=True, max_length=40, null=True)),
                ('staus', models.CharField(blank=True, max_length=40, null=True)),
                ('planfor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planfor', to='legalapp.Plan')),
                ('uerfors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uerfors', to='legalapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='userfor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfor', to='legalapp.User'),
        ),
    ]
