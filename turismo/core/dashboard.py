from django.template.loader import render_to_string

from jet.utils import context_to_dict
from jet.dashboard.dashboard import Dashboard

try:
    from django.template.context_processors import csrf
except ImportError:
    from django.core.context_processors import csrf


class CustomDashboard(Dashboard):
    columns = 4

    def init_with_context(self, context):
        # Lista de Apps (models)
        pass

    def render_tools(self):
        context = context_to_dict(self.context)
        context.update({
            'children': self.children,
            'app_label': self.app_label,
            'available_children': self.available_children
        })
        context.update(csrf(context['request']))

        return render_to_string('admin/dashboard_tools.html', context)