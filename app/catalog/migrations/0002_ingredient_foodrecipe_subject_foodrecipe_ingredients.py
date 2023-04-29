# Generated by Django 4.2 on 2023-04-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='foodrecipe',
            name='subject',
            field=models.CharField(default='lanche', max_length=100),
        ),
        migrations.AddField(
            model_name='foodrecipe',
            name='ingredients',
            field=models.ManyToManyField(to='catalog.ingredient'),
        ),
    ]