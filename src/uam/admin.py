from django.contrib import admin
from .models import GroupModel, CmdAliasModel
from .forms import GroupForm, CmdAliasForm
# Register your models here.

class GroupAdminForm(admin.ModelAdmin):
  list_display = ["__unicode__", "status", "update_by" ]
  form = GroupForm
class CmdAliasAdminForm(admin.ModelAdmin):
  list_display = ["__unicode__", "status", "update_by" ]
  form = CmdAliasForm

admin.site.register(GroupModel,GroupAdminForm)
admin.site.register(CmdAliasModel,CmdAliasAdminForm)
