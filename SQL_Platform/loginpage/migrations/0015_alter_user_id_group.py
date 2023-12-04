# Generated by Django 3.2.20 on 2023-11-26 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0014_alter_user_id_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='loginpage.groups'),
        ),
    ]
