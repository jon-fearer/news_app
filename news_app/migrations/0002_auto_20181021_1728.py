# Generated by Django 2.1 on 2018-10-21 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RegionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.Region')),
            ],
        ),
        migrations.DeleteModel(
            name='UserQueries',
        ),
        migrations.AddField(
            model_name='region',
            name='region_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.RegionCategory'),
        ),
    ]
