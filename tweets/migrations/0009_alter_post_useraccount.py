# Generated by Django 4.2.14 on 2024-07-21 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_alter_post_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='useraccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.useraccount'),
        ),
    ]
