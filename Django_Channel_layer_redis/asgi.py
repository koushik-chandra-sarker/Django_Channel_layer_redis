import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Channel_layer_redis.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        app.routing.websocket_urlpatterns
    )
    # Just HTTP for now. (We can add other protocols later.)
})
