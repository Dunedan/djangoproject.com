import certifi
from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class DocsConfig(AppConfig):
    name = 'docs'
    verbose_name = _('Documentation')
