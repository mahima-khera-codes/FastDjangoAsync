from django.db import migrations
from django.utils import timezone
from datetime import datetime


def convert_to_europe_moscow_timezone(apps, schema_editor):
    EndpointStates = apps.get_model("fast_api", "EndpointStates")
    moscow_timezone = timezone.get_default_timezone()

    for endpoint_state in EndpointStates.objects.all():
        state_start = endpoint_state.state_start
        state_end = endpoint_state.state_end

        start_dt = datetime.fromisoformat(state_start).replace(tzinfo=timezone.utc)
        end_dt = datetime.fromisoformat(state_end).replace(tzinfo=timezone.utc)

        start_dt_moscow = timezone.localtime(start_dt, timezone=moscow_timezone)
        end_dt_moscow = timezone.localtime(end_dt, timezone=moscow_timezone)

        endpoint_state.state_start = start_dt_moscow.isoformat()
        endpoint_state.state_end = end_dt_moscow.isoformat()
        endpoint_state.save()


class Migration(migrations.Migration):

    dependencies = [
        ("fast_api", "0004_updating_endpoints_states"),
    ]

    operations = [
        migrations.RunPython(convert_to_europe_moscow_timezone),
    ]
