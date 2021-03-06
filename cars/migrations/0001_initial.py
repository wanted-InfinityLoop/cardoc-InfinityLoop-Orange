# Generated by Django 3.2.9 on 2021-11-23 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontTire',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('id', models.UUIDField(default='87c13ca711b14e55814cc8959c89db8f', editable=False, primary_key=True, serialize=False)),
                ('width', models.PositiveSmallIntegerField()),
                ('aspect_ratio', models.PositiveSmallIntegerField()),
                ('wheel_size', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'front_tires',
            },
        ),
        migrations.CreateModel(
            name='RearTire',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('id', models.UUIDField(default='2db31d1911cf4368840dba53175c0e6e', editable=False, primary_key=True, serialize=False)),
                ('width', models.PositiveSmallIntegerField()),
                ('aspect_ratio', models.PositiveSmallIntegerField()),
                ('wheel_size', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'rears_tires',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('id', models.UUIDField(default='14ebc6a77de74f33a57cb427d7946df8', editable=False, primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=64)),
                ('front_tire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.fronttire')),
                ('rear_tire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.reartire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'rear_tires',
            },
        ),
    ]
