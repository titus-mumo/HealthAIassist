"""
ASGI config for HealthApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthApp.settings')

application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from .routings import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django_asgi_app = get_asgi_application()

application = application
