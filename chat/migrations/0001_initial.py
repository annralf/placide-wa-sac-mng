# Generated by Django 3.0.5 on 2021-05-20 18:47

import chat.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', djongo.models.fields.EmbeddedField(model_container=chat.models.Message)),
            ],
        ),
    ]