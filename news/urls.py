from django.urls import path
from .views import index

urlpatterns = [
    path('', index, ),    # path is '' because "news/" discarded in firstDJANGO.urls
]
