# Generated by Django 2.0.5 on 2018-08-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching_place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='time_from1',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_from2',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_from3',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_from4',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_from5',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_to1',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_to2',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_to3',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_to4',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='time_to5',
            field=models.CharField(blank=True, default='--:--', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='weekday1',
            field=models.CharField(blank=True, default='-', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='weekday2',
            field=models.CharField(blank=True, default='-', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='weekday3',
            field=models.CharField(blank=True, default='-', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='weekday4',
            field=models.CharField(blank=True, default='-', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='weekday5',
            field=models.CharField(blank=True, default='-', max_length=1, null=True),
        ),
    ]
