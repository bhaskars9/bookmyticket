# Generated by Django 4.1.3 on 2022-12-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='num_seats',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat_num',
            field=models.CharField(max_length=25),
        ),
    ]
