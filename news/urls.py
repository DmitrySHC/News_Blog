from django.urls import path
from .views import index, get_category

urlpatterns = [
    path('', index, ),  # path is '' because "news/" discarded in News_Blog.urls
    path('category/<int:category_id>/', get_category),
    # '<int:category_id>' mean that after '/' will be integer object
    # save it into var 'category_id' and pass by named parameter to called function 'get_category'
]
