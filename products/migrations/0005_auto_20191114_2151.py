# Generated by Django 2.2.6 on 2019-11-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ROH', 'ROH'), ('AEW', 'AEW'), ('WWE', 'WWE'), ('NJPW', 'NJPW'), ('IMPACT WRESTLING', 'Impact Wrestling')], max_length=50, verbose_name='Company'),
        ),
    ]
