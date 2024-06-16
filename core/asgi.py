"""
Configuração ASGI para o projeto core.

Este arquivo expõe o callable ASGI como uma variável de nível de módulo chamada ``application``.

Para mais informações sobre este arquivo, veja
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from game import routing
from authentication.middleware import TokenAuthMiddlewareStack

# Define a variável de ambiente 'DJANGO_SETTINGS_MODULE' com o valor 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
	'http': get_asgi_application(),
	'websocket': AllowedHostsOriginValidator(
		TokenAuthMiddlewareStack(
			URLRouter(
				routing.websocket_urlpatterns
			)
		)
	),
})