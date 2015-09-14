# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmdAliasModel',
            fields=[
                ('aliasid', models.AutoField(serialize=False, primary_key=True)),
                ('cmd_alias', models.CharField(max_length=255, verbose_name='Command Aliases')),
                ('cmd_list', models.TextField(help_text='Comma seperated Values', verbose_name='Command List')),
                ('status', models.CharField(default=b'active', max_length=45, choices=[(b'active', b'Active'), (b'inactive', b'Inactive')])),
                ('update_by', models.CharField(max_length=255)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'uam_cmdaliases',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('gname', models.CharField(max_length=255, verbose_name='Group Name')),
                ('display_name', models.CharField(max_length=255, verbose_name='Display Name')),
                ('mail_pdl', models.EmailField(max_length=255, verbose_name='Group Email')),
                ('status', models.CharField(default=b'active', max_length=45, choices=[(b'active', b'Active'), (b'inactive', b'Inactive'), (b'lock', b'Lock'), (b'remove', b'Remove')])),
                ('update_by', models.CharField(max_length=255)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'uam_group',
            },
        ),
        migrations.AddField(
            model_name='cmdaliasmodel',
            name='gid',
            field=models.ForeignKey(db_column=b'gid', default=None, blank=True, to='uam.GroupModel', null=True),
        ),
    ]
