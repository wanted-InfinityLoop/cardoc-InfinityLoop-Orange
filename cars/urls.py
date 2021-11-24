from django.urls import path

from cars.views import TireCreateView

urlpatterns = [
    path('/tire', TireCreateView.as_view()),
    path('/users/<str:user_id>', TireCreateView.as_view())
]