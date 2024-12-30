from django.db import migrations
from datetime import datetime, timedelta


def add_test_data(apps, schema_editor):
    ClientInfo = apps.get_model("fast_api", "ClientInfo")
    Client = apps.get_model("fast_api", "Client")
    Endpoint = apps.get_model("fast_api", "Endpoint")
    EndpointStates = apps.get_model("fast_api", "EndpointStates")

    client_info_records = [ClientInfo(info=f"ClientInfo {i}") for i in range(6, 21)]
    ClientInfo.objects.bulk_create(client_info_records)

    client_info_objects = ClientInfo.objects.all()
    client_records = [
        Client(client_name=f"Client {i}", client_info=client_info_objects[i - 1])
        for i in range(6, 21)
    ]
    Client.objects.bulk_create(client_records)

    endpoint_records = [
        Endpoint(id=i + 143, endpoint_name=f"Endpoint {i+143}") for i in range(6, 21)
    ]
    Endpoint.objects.bulk_create(endpoint_records)

    client_objects = Client.objects.all()
    endpoint_objects = Endpoint.objects.all()
    state_start_time = datetime(2023, 12, 22, 00, 00, 00)

    endpoint_states_records = []
    for i in range(15):
        start_time = state_start_time + timedelta(hours=i)
        end_time = start_time + timedelta(minutes=30)
        endpoint_states_records.append(
            EndpointStates(
                client=client_objects[i % len(client_objects)],
                endpoint=endpoint_objects[i % len(endpoint_objects)],
                state_name=f"State {i+1}",
                state_reason=f"Reason {i+1}",
                state_start=start_time.isoformat(),
                state_end=end_time.isoformat(),
                state_id=str(i + 1),
                group_id=str(i + 1),
                reason_group=f"Group {i+1}",
                info={},
            )
        )
    EndpointStates.objects.bulk_create(endpoint_states_records)


class Migration(migrations.Migration):

    dependencies = [
        ("fast_api", "0002_adding_test_data"),
    ]

    operations = [
        migrations.RunPython(add_test_data),
    ]
