"""
WSGI config for resume_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

# from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_app.settings')

# if settings._DEPLOY:
# 	os.system('python manage.py makemigrations')
# 	os.system('python manage.py migrate')
# 	os.system('python manage.py collectstatic')

application = get_wsgi_application()
