from django.urls import path
from .views import (
    home,
    detailView,
)
urlpatterns = [
    path('', home),
    path('detail/<int:id>', detailView, name='detail')

]