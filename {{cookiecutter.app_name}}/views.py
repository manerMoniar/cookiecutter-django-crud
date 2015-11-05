from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from vanilla import CreateView, DetailView, UpdateView, RedirectView
from django_tables2 import SingleTableView
from .forms import {{ cookiecutter.model_name }}Form
from .models import {{ cookiecutter.model_name }}
from .tables import {{ cookiecutter.model_name }}Table


class {{ cookiecutter.model_name }}List(SingleTableView):
    model = {{ cookiecutter.model_name }}
    table_class = {{ cookiecutter.model_name }}Table
    table_pagination = {'per_page': 10}


class {{ cookiecutter.model_name }}Create(SuccessMessageMixin, CreateView):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form
    template_name_suffix = '_create'
    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')
    success_message = "%(name)s was created successfully"


class {{ cookiecutter.model_name }}Detail(DetailView):
    model = {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Update(SuccessMessageMixin, UpdateView):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form
    template_name_suffix = '_update'
    success_url = reverse_lazy('{{ cookiecutter.app_name }}:list')
    success_message = "%(name)s was updated successfully"


class {{ cookiecutter.model_name }}Delete(RedirectView):
    model = {{ cookiecutter.model_name }}

    def get_redirect_url(self, *args, **kwargs):
        self.url = reverse_lazy('{{ cookiecutter.app_name }}:list')
        model = get_object_or_404({{ cookiecutter.model_name }}, pk=kwargs['pk'])
        name = model.name
        model.delete()
        messages.success(self.request, name + ' was deleted successfully')
        return super({{ cookiecutter.model_name }}Delete, self).get_redirect_url(*args, **kwargs)
