# Generated by Django 3.2.20 on 2023-10-24 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0002_groups_solutions_tasks_themes'),
    ]

    operations = [
        migrations.AddField(
            model_name='themes',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='solutions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='loginpage.solutions'),
        ),
    ]
