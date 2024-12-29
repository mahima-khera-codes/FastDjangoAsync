from django.urls import path
from .views import FilteredEndpointStatesView

urlpatterns = [
    path(
        "filtered-endpoint-states/",
        FilteredEndpointStatesView.as_view(),
        name="filtered_endpoint_states",
    ),
]
