"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'MeeseeksInc.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'MeeseeksInc.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name

import inventory


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for MeeseeksInc.
    """
     # we want a 3 columns layout
    columns = 2
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=True,
            deletable=False,
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
                
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))
        
        # append my own module
        self.children.append(HistoryDashboardModule())
        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))

        # append a feed module
        self.children.append(modules.Feed(
            _('Latest Django News'),
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ]
        ))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for MeeseeksInc.
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
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)

class CiuvoAnalytics(modules.DashboardModule):
     """ Dashboard Module which shows a Ciuvo Analytics Graph.
     """
     def __init__(self, **kwargs):
         super(CiuvoAnalytics, self).__init__(**kwargs)
         self.title = kwargs.get('title', _('Ciuvo Analytics'))
         self.show_title = kwargs.get('show_title', True)
#          self.template = kwargs.get('template', 
# 'admin_tools/analytics_module.html')
         self.layout = kwargs.get('layout', 'stacked')



class HistoryDashboardModule(modules.LinkList):
    title = 'Pending Requests'
    
    def init_with_context(self, context):
        request = context['request']
        # we use sessions to store the visited pages stack
        history = request.session.get('history', [])
        request_list = inventory.models.Request.objects.all()
        print(request_list)
        for item in request_list:
            print(item)
            self.children.append({
                    'title': item,
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },)
            # add the current page to the history
            

# class RequestsDashboardModule(modules.LinkList):
#     title = 'Pending Item Requests'
#     enabled=True
#     draggable=True
#     deletable=False
#     collapsible=False
#     
#     content="hi"
#     def init_with_context(self, context):
#         request = context['request']
# #         
# # #         print(request)
# #         # we use sessions to store the visited pages stack
# #         history = request.session.get('history', [])
# #         for item in history:
# #             self.children.append(item)
# #         # add the current page to the history
# #         history.insert(0, {
# #             'title': context['title'],
# #             'url': request.META['PATH_INFO']
# #         })
# #         if len(history) > 10:
# #             history = history[:10]
# #         request.session['history'] = history
