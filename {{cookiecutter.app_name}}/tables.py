import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Table(tables.Table):
    name = tables.LinkColumn('{{ cookiecutter.app_name }}:detail', args=[A('pk')])
    actions = tables.TemplateColumn(orderable=False, empty_values=(), template_name='{{ cookiecutter.app_name }}/{{ cookiecutter.model_name|lower }}_actions.html')

    class Meta:
        model = {{ cookiecutter.model_name }}
        fields = ('name',)
