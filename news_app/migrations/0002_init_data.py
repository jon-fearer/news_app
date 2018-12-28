from django.core.management import call_command
from django.db import migrations


def load_fixture(apps, schema_editor):
    fixtures = ['region_data', 'publishing_organization_data']
    for fixture in fixtures:
        call_command('loaddata', fixture, app_label='news_app')


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."
    models = ['region', 'region_category', 'publishing_organization']
    for model in models:
        MyModel = apps.get_model('news_app', model)
        MyModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
