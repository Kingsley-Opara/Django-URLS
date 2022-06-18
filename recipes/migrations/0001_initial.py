# Generated by Django 4.0.5 on 2022-06-18 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recieps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About', models.TextField()),
                ('Ingredient', models.TextField(max_length=1000)),
                ('Preperation', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('Featured', models.BooleanField(default=True)),
                ('Owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
