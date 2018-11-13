# Generated by Django 2.1.2 on 2018-11-08 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20181025_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('area', models.FloatField(blank=True, default=None, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.City')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='userrequests',
            name='linkur',
        ),
        migrations.DeleteModel(
            name='Houses',
        ),
        migrations.DeleteModel(
            name='Userrequests',
        ),
        migrations.AddField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.Owner'),
        ),
    ]
