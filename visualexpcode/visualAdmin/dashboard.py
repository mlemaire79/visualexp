"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'visualexpcode.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'visualexpcode.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name

from visualAdmin.models import Exposition, Display, Task
from datetime import date, timedelta, datetime

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for visualexpcode.
    """

    template = 'admin/dashboard.html'
    columns = 3

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_("Gestion des Expositions"), "manage/expositions/"],
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Gestionnaire du contenu'),
            draggable=False,
            deletable=False,
            collapsible=False,
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Gestion utilisateurs'),
            draggable=False,
            deletable=False,
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'), 5,
            draggable=False,
            deletable=False,
        ))

        # append an alerts of delivery artworks
        self.children.append(modules.Group(
            title = _('Alertes'),
            display = 'stacked',
            draggable=False,
            deletable=False,
            children=[
                modules.LinkList(
                    title = 'Livraisons',
                    children = self.get_alerts(),
                ),
                modules.LinkList(
                    title = 'Taches',
                    children = self.get_tasks(context),
                ),
            ]
        ))
         
    def get_tasks(self, context):
        task_list = []
        request = context['request']
        if request.user.is_authenticated:
            alert_date = date.today() + timedelta(7)

            user = request.user
            user_tasks = Task.objects.filter(users__id__contains=user.id).filter(is_completed__exact=False).filter(start_date__lte=alert_date)
            for task in user_tasks:
                msg = task.name+ " : "+task.start_date.strftime("%d/%m - %H:%M")
                url = 'visualAdmin/task/'+str(task.id_task)+'/change'
                task_list.append([msg, url])
        return task_list

    # @TODO Find out how to change alert colors 
    def get_alerts(self):
        """
        create alert list for artworks that have not
        been delivered 1 week before exposition start
        """
        alert_list = []
        alert_date = date.today() + timedelta(7)
        soon_expos = Exposition.objects.filter(start_date__lte=alert_date).filter(end_date__gte=date.today())
        
        for expo in soon_expos:

            missing_displays = Display.objects.filter(exposition=expo).filter(has_arrived=False)
            for display in missing_displays:
                classification = ""
                if(expo.start_date - date.today() <= timedelta(2)):
                    classification = "URGENT : "
                msg = classification+"L'oeuvre "+display.artwork.title+" pour l'exposition "+expo.title+" n'est pas encore arrivée."
                url = "manage/expositions/"+str(expo.expo_id)
                alert_list.append([_(msg), url])

        return alert_list


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for visualexpcode.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.models,
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """

        return super(CustomAppIndexDashboard, self).init_with_context(context)