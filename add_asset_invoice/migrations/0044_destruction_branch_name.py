# Generated by Django 4.2 on 2023-07-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_asset_invoice', '0043_assetitems_branch_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='destruction',
            name='branch_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='add_asset_invoice.branch', verbose_name='الفرع'),
            preserve_default=False,
        ),
    ]
