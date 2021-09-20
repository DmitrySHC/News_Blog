from django.urls import path
from .views import index

urlpatterns = [
    path('', index),    # path is '' because the "page_1\" part is discarded in firstDJANGO.urls
]
