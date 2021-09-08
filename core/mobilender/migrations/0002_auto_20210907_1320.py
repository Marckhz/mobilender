# Generated by Django 3.2.7 on 2021-09-07 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobilender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='sites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.orders'),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]