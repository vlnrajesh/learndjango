from django import forms
from .models import CmdAliasModel,GroupModel
from django_select2.widgets import Select2MultipleWidget
from django.forms.formsets import formset_factory
import re
class GroupForm(forms.ModelForm):
  '''
  Standard Group From
  '''
  class Meta:
    model = GroupModel
    exclude = ['gid','update_date']

class CmdAliasForm(forms.ModelForm):
  '''
  Command Alias Form
  '''
  class Meta:
    model = CmdAliasModel
    exclude = ['aliasid','update_date']
  
class AddCmdAliasForm(forms.Form):
  title = "Add Command Dictionary"
  cmd_alias = forms.CharField(label= 'Command Alias', max_length=255)
  cmd_list = forms.CharField(widget=forms.Textarea(),help_text= "Comma seperated list of commands")
  
  #Command Alias Validations
  def clean_cmd_alias(self):
    _cmd_alias = self.cleaned_data.get('cmd_alias')
    if _cmd_alias.find(' ') > -1:
      raise forms.ValidationError("%s Command Alias cannot be with spaces" %(_cmd_alias))
    return _cmd_alias.upper()
  
  #Command List Validations
  def clean_cmd_list(self):
    _cmd_list = self.cleaned_data.get('cmd_list')
    print _cmd_list.split(',')
    _cmd_list = _cmd_list.split(',')
    _cmd_array = list()
    for _each_command in _cmd_list:
      _each_command = _each_command.strip(' \t\n\r')
      if not _each_command[0]=='/':
        raise forms.ValidationError(_each_command +" should start with /")
      _cmd_array.append(str(_each_command))
    return _cmd_array

  #Form Level validations
  def clean(self):
    cleaned_data = self.cleaned_data
    _cmd_alias = cleaned_data.get('cmd_alias')
    cmdalias_objects = CmdAliasModel.objects.filter(cmd_alias=_cmd_alias)
    if len(cmdalias_objects)>0:
      raise forms.ValidationError(_cmd_alias+" already exists")
    return cleaned_data

CommandAliasFormSet = formset_factory(AddCmdAliasForm,extra=1)

class groupAddForm(forms.Form):
  """
  Group Add Form
  """
  title = "Add Group & Commands"
  gname = forms.CharField(label='Group Name',max_length=255)
  display_name = forms.CharField(label='Display Name', max_length=255)
  mail_pdl = forms.EmailField(label='Group PDL')

  cmd_aliases = forms.ModelMultipleChoiceField(
      widget=Select2MultipleWidget(select2_options={'width':'resolve'}),
      label='Command Alias',
      queryset=CmdAliasModel.objects.filter(gid__isnull=True)
  )
  
  #Group Name field level validations
  def clean_grpname(self):
    group_name=self.cleaned_data.get('gname')
    if  group_name.find(' ') > -1:
      raise forms.ValidationError("Group Name cannot be with spaces")
    
    if not re.match(r'^[A-Za-z0-9_]+$',group_name):
      raise forms.ValidationError(group_name +" should be in alphanumeric string")
    
    return group_name

  #DisPlay Name Validations
  def clean_display_name(self):
    display_name = self.cleaned_data.get('display_name')
    if display_name[0]==' ':
      raise forms.ValidationError(display_name+" cannot start with spaces")
    return display_name

  #Clean Mail PDL 
  def clean_mail_pdl(self):
    mailadd=self.cleaned_data.get('mail_pdl')
    domain,provider=mailadd.split('@')
    if not provider =='rpxcorp.com':
      raise forms.ValidationError("Mail address required to be RPX Corporation domain")
    return mailadd
  
  #Form Level Validations
  def clean(self):
    cleaned_data = self.cleaned_data
    gname = cleaned_data.get('gname')
    groupmodel_data = GroupModel.objects.filter(gname=gname)
    if len(groupmodel_data)>0:
      raise forms.ValidationError(gname+" Already Exists")
    return cleaned_data
