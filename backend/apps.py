from django.apps import AppConfig
from django.conf import settings

class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        # Example usage of BASE_DIR in apps.py
        static_files_directory = settings.BASE_DIR / 'backend' / 'static'

       
        # Your other app-specific code here...
