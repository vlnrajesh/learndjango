from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from models import CmdAliasModel,GroupModel
from forms import AddCmdAliasForm,groupAddForm,GroupForm,CmdAliasForm,CommandAliasFormSet
from datetime import datetime
# Create your views here.
class ContractView(FormView):
	template_name='cmdalias.html'
	form_class = AddCmdAliasForm
	success_url = '/'
	def form_valid(self, form):
		form.clean()
		return super()
	

def add_cmdalias(request):
	title = "Add Command Alias"
	_cmdalias_form = AddCmdAliasForm(request.POST or None)
	context = {
		"title" : title,
		"form" : _cmdalias_form
	}
	if _cmdalias_form.is_valid():
		current_user = 'admin'
		if request.user.is_authenticated():
			current_user = request.user.username
		_cmdalias_object = CmdAliasModel(cmd_alias=_cmdalias_form.cleaned_data['cmd_alias'],cmd_list=_cmdalias_form.cleaned_data['cmd_list'],update_by=current_user)
		_cmdalias_object.save()
		message = "%s added successfully" %(_cmdalias_form.cleaned_data['cmd_alias'])
		return render_to_response('confirm.html',{'message': message})
	
	return render(request,"add_command.html",context)
@login_required
def test_group(request):
	title = "Add New Group"
	group_add_form = groupAddForm(request.POST or None)
	cmdformset = CommandAliasFormSet(request.POST or None, prefix="AddCmdAliasForm")
	context = {
		'title' : title,
		'form' : group_add_form,
		'cmdformset': cmdformset
	}
	if group_add_form.is_valid():
		current_user = 'admin'
		if request.user.is_authenticated():
			current_user = request.user.username 
		
		group_obj = GroupModel(gname=group_add_form.cleaned_data['gname'],display_name=group_add_form.cleaned_data['display_name'],mail_pdl=group_add_form.cleaned_data['mail_pdl'],update_by=current_user)
		group_obj.save()
		for _each_selection in group_add_form.cleaned_data['cmd_aliases']:
			cmd_alias_model=CmdAliasModel.objects.get(cmd_alias=_each_selection)
			cmd_alias_model.update_by=current_user
			cmd_alias_model.update_date=datetime.now()
			cmd_alias_model.gid=group_obj
			cmd_alias_model.save()
		message = "%s added successfully" %(group_add_form.cleaned_data['display_name'])
		return render_to_response('confirm.html',{'message':message})

	return render(request,"add_group.html",context)
