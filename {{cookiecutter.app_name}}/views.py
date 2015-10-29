from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DetailView, UpdateView, DeleteView
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import {{ cookiecutter.model_name }}Form
from .models import {{ cookiecutter.model_name }}
from .tables import {{ cookiecutter.model_name }}Table


class {{ cookiecutter.model_name }}List(SingleTableView):
    model = {{ cookiecutter.model_name }}
    table_class = {{ cookiecutter.model_name }}Table


class {{ cookiecutter.model_name }}Create(SuccessMessageMixin, CreateView):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form
    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')
    success_message = "%(name)s was created successfully"


class {{ cookiecutter.model_name }}Detail(DetailView):
    model = {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Update(SuccessMessageMixin, UpdateView):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form
    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')
    success_message = "%(name)s was updated successfully"


class {{ cookiecutter.model_name }}Delete(DeleteView):
    model = {{ cookiecutter.model_name }}
    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')
