from django.db import models
from django.utils.translation import ugettext_lazy as _
ACTIVE_VALUE 		=	'active'
INACTIVE_VALUE	=	'inactive'
LOCK_VALUE 			= 'lock'
REMOVE_VALUE 		= 'remove'

STATUS_CHOICES 	=	(
	(ACTIVE_VALUE,'Active'),
	(INACTIVE_VALUE,'Inactive')
)
# Models for UAM.


class GroupModel(models.Model):
	'''
	Purpose : This table is to manage group information.
	Fields 	: This table will managed by UI and referred by rpx::agent recipe.
		gid						: Primary Key 
		gname					:	Group name
		display_name	:	Visiable name in forms
		mail_pdl			: mail address to report any stealth activities with the group users
		status				: Represents the state of environment,
										active 		-> available and managed by chef recipe. Show up in search results. Appear in report result if not filtered out.
										inactive	-> not available and managed by chef server. Dont show up in search results. Appear in report results if not filtered out
		update_by			: User who currently active on UI session during this transaction
		update_date		: Timestamp of the transaction
	'''
	
	STATUS_CHOICES 	=	(
	(ACTIVE_VALUE,'Active'),
	(INACTIVE_VALUE,'Inactive'),
	(LOCK_VALUE, 'Lock'),
	(REMOVE_VALUE,'Remove')
)
	gid = models.AutoField(primary_key=True)
	gname = models.CharField(max_length=255,verbose_name= _("Group Name"))
	display_name = models.CharField(max_length=255,verbose_name= _("Display Name"))
	mail_pdl = models.EmailField(max_length=255, verbose_name = _("Group Email"))
	status = models.CharField(max_length=45,choices=STATUS_CHOICES,default=ACTIVE_VALUE)
	update_by = models.CharField(max_length=255)
	update_date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.display_name
	
	class Meta:
		db_table="uam_group"

class CmdAliasModel(models.Model):
	aliasid	=	models.AutoField(primary_key=True)
	cmd_alias	=	models.CharField(max_length=255,verbose_name =_("Command Aliases"))
	cmd_list	=	models.TextField(verbose_name =_("Command List"),help_text=_("Comma seperated Values"))
	gid	=	models.ForeignKey(GroupModel,db_column='gid',null=True,blank=True,default=None)
	status	=	models.CharField(max_length=45,choices=STATUS_CHOICES,default=ACTIVE_VALUE)
	update_by = models.CharField(max_length=255)
	update_date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.cmd_alias
	
	class Meta:
		db_table="uam_cmdaliases"