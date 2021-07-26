from django.urls import path
from api.views import OsdView, DetailView

urlpatterns = [
    path('', OsdView.as_view()),
    path('<slug:machine_name>/', DetailView.as_view()),
]