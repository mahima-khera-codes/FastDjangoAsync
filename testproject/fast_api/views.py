from django.http import JsonResponse
from django.views import View
from asgiref.sync import sync_to_async
from .models import EndpointStates
from django.utils.decorators import classonlymethod
import asyncio


class FilteredEndpointStatesView(View):
    async def __get_endpoint_states(self, input_start: str) -> list:
        queryset = await sync_to_async(
            lambda: list(
                EndpointStates.objects.filter(
                    state_start__gte=input_start, endpoint_id=139
                ).order_by("-state_start")
            )
        )()
        return queryset

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, *args, **kwargs):
        input_start = request.GET.get("input_start")

        queryset = await self.__get_endpoint_states(str(input_start))
        filtered_queryset = [item for item in queryset if item.id % 3 == 0]
        filtered_count = len(filtered_queryset)

        client_info = None
        state_id = None
        if len(filtered_queryset) >= 3:
            third_record = filtered_queryset[2]
            client_info = await sync_to_async(
                lambda: third_record.client.client_info.info
            )()
            state_id = await sync_to_async(lambda: third_record.state_id)()

        return JsonResponse(
            {
                "filtered_count": filtered_count,
                "client_info": client_info,
                "state_id": state_id,
            }
        )
