from django.urls import path, include
from .views import GetListView

urlpatterns = [
    path('list/',GetListView.as_view()),
]
