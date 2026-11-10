from django.apps import AppConfig
# Import Django's AppConfig class
# This is used to configure application-specific settings


class StoreConfig(AppConfig):
    # This class defines configuration for the 'store' app

    default_auto_field = 'django.db.models.BigAutoField'
    # Sets the default type for automatically created primary keys (IDs)
    # BigAutoField = large integer auto-incrementing ID (recommended for most apps)

    name = 'store'
    # The name of the app
    # Must match the app folder name