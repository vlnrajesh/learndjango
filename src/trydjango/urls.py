from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
  # Examples:
  #url(r'^commands/', 'uam.views.add_cmdalias',name="add_commands"),
  url(r'^$','uam.views.test_group',name='default_page'),
  url(r'^add_group/','uam.views.test_group',name='add_group'),
  url(r'^add_command/','uam.views.add_cmdalias',name='add_cmd_alias'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^login/','django.contrib.auth.views.login',{ 'template_name':'registration/login.html'},name='login_page'),
	url(r'^logout/','django.contrib.auth.views.logout',{'template_name':'registration/logout.html'},name='logout_page'),
  url(r'^select2/',include('django_select2.urls')),
]
if settings.DEBUG:
  urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
