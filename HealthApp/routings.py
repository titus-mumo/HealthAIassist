from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from app.consumers import ProcessingConsumer
from django.core.asgi import get_asgi_application

websocket_urlpatterns = [
    path('ws/processing/', ProcessingConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
})