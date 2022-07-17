# Generated by Django 4.0.5 on 2022-07-17 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Marshrut nomi')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name="Umumiy yo'l vaqti")),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Qaysi shahardan')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='Qaysi shaharga')),
                ('trains', models.ManyToManyField(to='trains.train', verbose_name="Poyezdlar ro'yhati")),
            ],
            options={
                'verbose_name': 'Marshrut',
                'verbose_name_plural': 'Marshrutlar',
                'ordering': ['travel_times'],
            },
        ),
    ]
