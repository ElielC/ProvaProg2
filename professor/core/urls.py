from django.urls import path
from core import views as v

urlpatterns = [
    path("", v.HomeView.as_view(), name="home"),
    path("create/", v.ProfessorCreateView.as_view(), name="professor-create"),
    path("delete/<int:pk>/", v.ProfessorDeleteView.as_view(), name="professor-delete"),
    path("list/", v.ProfessorListView.as_view(), name="professor-list"),
    path("update/<int:pk>/", v.ProfessorUpdateView.as_view(), name="professor-update"),
]
