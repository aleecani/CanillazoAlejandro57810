# Generated by Django 5.0.6 on 2024-07-02 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_comprador_nombre_alter_vendedor_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comprador',
            options={'ordering': ['nombre'], 'verbose_name': 'Comprador', 'verbose_name_plural': 'Compradores'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='vendedor',
            options={'ordering': ['nombre'], 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
    ]
