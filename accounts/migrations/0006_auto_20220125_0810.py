# Generated by Django 3.1.7 on 2022-01-25 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220125_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='email',
            new_name='category',
        ),
    ]