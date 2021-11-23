from django.urls import path

from cars.views import TireCreateView

urlpatterns = [
    path('/tire', TireCreateView.as_view())
]