# Generated by Django 3.2.20 on 2023-11-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0008_auto_20231121_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='benchmark_query',
            field=models.TextField(default="SELECT * FROM public.'employees'", max_length=2000, null=True),
        ),
    ]
