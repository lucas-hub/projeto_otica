# Generated by Django 3.2.25 on 2024-05-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
    ]
