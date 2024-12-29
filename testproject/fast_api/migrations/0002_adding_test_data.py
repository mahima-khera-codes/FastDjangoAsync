from django.db import migrations


def add_test_data(apps, schema_editor):
    ClientInfo = apps.get_model("fast_api", "ClientInfo")
    Client = apps.get_model("fast_api", "Client")
    Endpoint = apps.get_model("fast_api", "Endpoint")
    EndpointStates = apps.get_model("fast_api", "EndpointStates")

    ClientInfo.objects.bulk_create(
        [
            ClientInfo(info="ClientInfo 1"),
            ClientInfo(info="ClientInfo 2"),
            ClientInfo(info="ClientInfo 3"),
            ClientInfo(info="ClientInfo 4"),
            ClientInfo(info="ClientInfo 5"),
        ]
    )

    client_info_objects = ClientInfo.objects.all()
    Client.objects.bulk_create(
        [
            Client(client_name="Client 1", client_info=client_info_objects[0]),
            Client(client_name="Client 2", client_info=client_info_objects[1]),
            Client(client_name="Client 3", client_info=client_info_objects[2]),
            Client(client_name="Client 4", client_info=client_info_objects[3]),
            Client(client_name="Client 5", client_info=client_info_objects[4]),
        ]
    )

    Endpoint.objects.bulk_create(
        [
            Endpoint(id=137, endpoint_name="Endpoint 137"),
            Endpoint(id=138, endpoint_name="Endpoint 138"),
            Endpoint(id=139, endpoint_name="Endpoint 139"),
            Endpoint(id=140, endpoint_name="Endpoint 140"),
            Endpoint(id=141, endpoint_name="Endpoint 141"),
            Endpoint(id=142, endpoint_name="Endpoint 142"),
        ]
    )

    client_objects = Client.objects.all()
    endpoint_objects = Endpoint.objects.all()
    EndpointStates.objects.bulk_create(
        [
            EndpointStates(
                client=client_objects[0],
                endpoint=endpoint_objects[0],
                state_name="State 1",
                state_reason="Reason 1",
                state_start="2023-12-20T22:39:40.000",
                state_end="2023-12-20T22:59:59.000",
                state_id="1",
                group_id="1",
                reason_group="Group 1",
                info={},
            ),
            EndpointStates(
                client=client_objects[1],
                endpoint=endpoint_objects[1],
                state_name="State 2",
                state_reason="Reason 2",
                state_start="2023-12-20T23:00:00.000",
                state_end="2023-12-21T00:00:00.000",
                state_id="2",
                group_id="2",
                reason_group="Group 2",
                info={},
            ),
            EndpointStates(
                client=client_objects[2],
                endpoint=endpoint_objects[2],
                state_name="State 3",
                state_reason="Reason 3",
                state_start="2023-12-21T00:01:00.000",
                state_end="2023-12-21T01:00:00.000",
                state_id="3",
                group_id="3",
                reason_group="Group 3",
                info={},
            ),
            EndpointStates(
                client=client_objects[3],
                endpoint=endpoint_objects[3],
                state_name="State 4",
                state_reason="Reason 4",
                state_start="2023-12-21T01:01:00.000",
                state_end="2023-12-21T02:00:00.000",
                state_id="4",
                group_id="4",
                reason_group="Group 4",
                info={},
            ),
            EndpointStates(
                client=client_objects[4],
                endpoint=endpoint_objects[4],
                state_name="State 5",
                state_reason="Reason 5",
                state_start="2023-12-21T02:01:00.000",
                state_end="2023-12-21T03:00:00.000",
                state_id="5",
                group_id="5",
                reason_group="Group 5",
                info={},
            ),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("fast_api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_test_data),
    ]
