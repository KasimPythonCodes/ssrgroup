# Generated by Django 4.0.2 on 2022-05-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0005_customer_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookplot',
            name='phase',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]