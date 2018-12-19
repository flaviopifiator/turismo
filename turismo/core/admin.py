from django.contrib import admin
from django.utils import timezone
from django.template.loader import render_to_string


class CustomAdmin(admin.AdminSite):
    site_header = site_title = 'Turismo'
    index_title = 'Administración'
    index_template = 'admin/index.html'

admin_general = CustomAdmin(name='admin_general')


class ControlsAdminMixin(object):
    list_controls_template = None
    list_display_links = None

    def get_controls(self, instance):
        if not self.list_controls_template:
            self.list_controls_template = 'core/generic-list-controls.html'

        return render_to_string(self.list_controls_template, {
            'instance': instance,
            'has_change_permission': self.has_change_permission(self.request),

        })

    get_controls.short_description = 'Controles'

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request)) + ['get_controls']
        return list_display

    def get_queryset(self, request):
        self.request = request  # Use in template list_controsl_template
        return super().get_queryset(request)


class ReadOnlyModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that prevents modifications through the admin.
    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    Source: https://gist.github.com/aaugustin/1388243
    """
    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return (request.method in ['GET', 'HEAD'] and
                super().has_change_permission(request, obj))

    def has_delete_permission(self, request, obj=None):
        return False


# ModelAdmin para Publicado -> Modelo Abstracto.
class PublicadoAdmin(admin.ModelAdmin):
    change_form_template = 'core/change_form.html'
    actions = ['publicar', 'despublicar']

    def render_change_form(self, req, ctxt, add=False, change=False, form_url='', obj=None):
        if req.user.is_superuser:
            if obj and obj.publicado is not None:
                ctxt.update(checked=True)
        return super().render_change_form(req, ctxt, add=add, change=change, form_url=form_url, obj=obj)

    def response_change(self, request, obj):
        if request.user.is_superuser:
            if '_publicar' in request.POST:
                obj.publicar()
            else:
                if obj.publicado is not None:
                    obj.publicar(False)

        return super().response_change(request, obj)

    def response_add(self, request, obj, post_url_continue=None):
        response = super().response_add(request, obj, post_url_continue)
        if request.user.is_superuser:
            if '_publicar' in request.POST:
                obj.publicar()
        return response

    def publicar(self, request, queryset):
        rows_update = queryset.update(publicado=timezone.now())
        message = "%s " % rows_update
        self.message_user(request, "%s registro/s publicado/s." % message)

    publicar.short_description = 'Publicar registros seleccionados'

    def despublicar(self, request, queryset):
        rows_update = queryset.update(publicado=None)
        message = "%s " % rows_update
        self.message_user(request, "%s registro/s despublicado/s." % message)

    despublicar.short_description = 'Despublicar registros seleccionados'

    def get_actions(self, request):
        actions = super().get_actions(request)
        # TODO:
        # If user haven't permission or not member in group "publicar"
        # delete publicar and despublicar of actions.
        # del actions['publicar'] ...
        return actions

    def get_list_filter(self, request):
        list_filter = [
                          filters.PublicadoListFilter
                      ] + list(super().get_list_filter(request))

        return list_filter

    def get_list_display(self, request):
        return list(super().get_list_display(request)) + ['publicado']


