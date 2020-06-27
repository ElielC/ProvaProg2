from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import DeletionMixin, SingleObjectMixin, View
from django.http.response import HttpResponse
from http import HTTPStatus

from core.models import Professor
from core.forms import ProfessorForm


class DeleteViewWithoutRedirect(SingleObjectMixin, DeletionMixin, View):
    def delete(self, request, *args, **kwargs):
        super().delete(request, args, kwargs)

        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    def get_success_url(self):
        return "/"


class HomeView (TemplateView):
    template_name = "home.html"


class ProfessorListView (ListView):
    template_name = "professor_list.html"
    model = Professor


class ProfessorCreateView (CreateView):
    template_name = "professor_form.html"
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('professor-list')


class ProfessorUpdateView (UpdateView):
    template_name = "professor_form.html"
    form_class = ProfessorForm
    success_url = reverse_lazy('professor-list')
    queryset = Professor.objects.all()


class ProfessorDeleteView(DeleteViewWithoutRedirect):
    model = Professor
