from django.db import migrations


def update_endpoint_ids(apps, schema_editor):
    EndpointStates = apps.get_model("fast_api", "EndpointStates")
    EndpointStates.objects.update(endpoint_id=139)


class Migration(migrations.Migration):

    dependencies = [
        ("fast_api", "0003_adding_test_data"),
    ]

    operations = [
        migrations.RunPython(update_endpoint_ids),
    ]
