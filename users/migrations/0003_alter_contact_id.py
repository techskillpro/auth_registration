# Generated by Django 4.1 on 2023-02-15 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_contact_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
