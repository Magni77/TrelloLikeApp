# Generated by Django 2.0 on 2018-01-10 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20171231_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='performer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Task', to=settings.AUTH_USER_MODEL),
        ),
    ]
