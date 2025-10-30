# from django.apps import AppConfig

# class TodoConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'todo'




# from django.apps import AppConfig

# class MyAppConfig(AppConfig):
#     name = 'myapp'

#     def ready(self):
#         import myapp.receivers  # auto-load receivers
# from django.apps import AppConfig


# from django.apps import AppConfig

# class TodoConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'todo'

#     def ready(self):
#         import todo.signals  # 👈 this ensures signals are loaded


from django.apps import AppConfig

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'

    def ready(self):
        import todo.receivers  # 👈 ensures receivers connect
