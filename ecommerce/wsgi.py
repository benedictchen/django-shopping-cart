"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import dotenv

dotenv.read_dotenv('../env')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
