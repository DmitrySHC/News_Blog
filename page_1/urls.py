from django.urls import path
from .views import index

urlpatterns = [
    path('', index, 'index'),    # path is '' because "page_1\" is discarded in firstDJANGO.urls
]
