# Generated by Django 4.2 on 2023-05-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_asset_invoice', '0010_delete_discounttax_additiontax_addition_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_tax', models.CharField(max_length=100, verbose_name='ضريبة الخصم')),
                ('discount_type', models.CharField(choices=[('percent', 'نسبة'), ('value', 'قيمة')], default='percent', max_length=20, verbose_name='نوع الضريبة')),
                ('choice_field_coast', models.CharField(choices=[('total_price', 'السعر بدون مصروفات'), ('total_invoice_cost', 'السعر شامل المصروفات')], default='total_invoice_cost', max_length=20, verbose_name='ربط الحقول')),
                ('percent_discount_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='نسبة الضريبة')),
                ('value_discount_tax', models.FloatField(blank=True, null=True, verbose_name='قيمة الضريبة')),
            ],
        ),
    ]
