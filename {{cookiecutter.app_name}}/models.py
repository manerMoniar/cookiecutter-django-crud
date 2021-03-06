from django.core.urlresolvers import reverse
from django.db import models


class {{ cookiecutter.model_name }}(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('{{ cookiecutter.app_name }}:detail', args=[str(self.id)])
