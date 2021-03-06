# Generated by Django 2.0.1 on 2018-01-18 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20180110_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='contributors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='board', to='users.UserProjectTeam'),
        ),
        migrations.AlterField(
            model_name='list',
            name='board_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='boards.Board'),
        ),
        migrations.AlterField(
            model_name='task',
            name='list_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='boards.List'),
        ),
    ]
