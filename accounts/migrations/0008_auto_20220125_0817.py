# Generated by Django 3.1.7 on 2022-01-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220125_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoors', 'Indoors'), ('OutDoor', 'OutDoor'), ('Sports', 'Sports')], max_length=200, null=True),
        ),
    ]
