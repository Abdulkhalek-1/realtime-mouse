from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/group/<str:group_id>/<str:username>/", consumers.MouseConsumer.as_asgi()),
]
