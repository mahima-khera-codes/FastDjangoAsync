from django.contrib import admin
from .models import ClientInfo, Client, Endpoint, EndpointStates

admin.site.register(ClientInfo)
admin.site.register(Client)
admin.site.register(Endpoint)
admin.site.register(EndpointStates)
