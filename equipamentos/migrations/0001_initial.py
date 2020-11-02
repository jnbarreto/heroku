# Generated by Django 3.0.3 on 2020-11-02 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('num_controle', models.IntegerField(verbose_name='Número de controle')),
                ('img_equip', models.ImageField(blank=True, null=True, upload_to='equipamentos', verbose_name='Imagem do equipamento')),
            ],
        ),
    ]
