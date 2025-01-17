"""
WSGI config for django_task_manager project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_task_manager.settings')

application = get_wsgi_application()
