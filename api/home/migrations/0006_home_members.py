# Generated by Django 4.1.4 on 2022-12-31 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_user_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="home",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.home"
            ),
        ),
    ]
