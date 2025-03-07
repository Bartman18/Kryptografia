from django.urls import path
from . import views
urlpatterns = [
    path("encrypt/", views.encrypt_message, name="encrypt_message"),
    path("decrypt/", views.decrypt_message, name="decrypt_message"),
    path("generate-key/", views.generate_key_view, name="generate_key"),
]