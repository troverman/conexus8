# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
request.vars._next = None
auth = Auth(db)
auth.next = None
crud, service, plugins = Crud(db), Service(), PluginManager()
## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
auth.settings.allow_basic_login = True

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

################################################################
####database_tables#############################################
################################################################


################################
####member_account##############
################################
db.define_table('member_account',
    Field('member_id', 'string'),
    Field('facebook_url', 'string'),
    Field('twitter_url', 'string'),
    Field('google_plus_url', 'string'),
    Field('bankingfor_url', 'string'),
    Field('linkedin_url', 'string'),
    Field('inlrn_url', 'string'),
    Field('voetr_url', 'string'),
    Field('lealr_url', 'string'),
)

################################
####member_location#############
################################
db.define_table('member_location',
    Field('member_id','string'),
    Field('time_stamp','datetime'),
    Field('location_lat','string'),
    Field('location_lng','string'),
)

################################
####member_picture##############
################################
db.define_table('member_picture',
    Field('member_id', 'string'),
    Field('picture', 'upload', uploadfield='picture_file'),
    Field('picture_file', 'blob')
)

################################
####testing#####################
################################
db.define_table('testing',
    Field('number_sum','text'),
)

################################
####project#####################
################################
db.define_table('project',
    Field('url_title','string'),
    Field('title','string'),
    Field('description','string'),
)

################################
####project_task################
################################
db.define_table('project_task',
    Field('project_id','string', readable=False, writable=False),
    Field('title','string'),
    Field('description','string'),
    Field('completed','boolean'),
    Field('task_member_array','list:string'),
    Field('task_start_time','datetime'),
    Field('task_end_time','datetime'),
)
#db.project_task.task_member_array.widget = SQLFORM.widgets.autocomplete(request, db.auth.username, id_field=db.auth.id)
################################
####project_task_tag############
################################
db.define_table('project_task_tag',
    Field('project_task_id','string'),
    Field('tag','string'),
)

################################
####project_task_comment########
################################
db.define_table('project_task_comment',
    Field('project_task_id','string'),
    Field('member_id','string'),
    Field('comment_content','string'),
    Field('datetime','datetime'),
)


################################
####project_member##############
################################
db.define_table('project_member',
    Field('member_id','string'),
    Field('project_id','string'),
    Field('join_date','datetime'),
    Field('project_membergroup_id_array','list:string'),
)

################################
####project_page################
################################ 
db.define_table('project_page',
    Field('project_id','string', readable=False, writable=False),
    Field('title','string'),
    Field('page_content','text'),
)

################################
####project_picture#############
################################
db.define_table('project_picture',
    Field('project_id', 'string'),
    Field('picture', 'upload', uploadfield='picture_file'),
    Field('picture_file', 'blob')
)

################################
####project_membergroup#########
################################
db.define_table('project_membergroup',
    Field('project_id','integer'),
    Field('title','string'),
    Field('description','string'),
)


################################
####event#######################
################################
db.define_table('event',
    Field('url_title','string'),
    Field('title','string'),
    Field('description','string'),
    Field('start_time','datetime'),
    Field('end_time','datetime'),
)

################################
####event_member################
################################
db.define_table('event_member',
    Field('member_id','string'),
    Field('event_id','string'),
    Field('event_membergroup_id_array','list:string'),
)

################################
####event_membergroup###########
################################
db.define_table('event_membergroup',
    Field('event_id','integer'),
    Field('title','string'),
    Field('description','string'),
)

################################
####event_thread################
################################
db.define_table('event_thread',
    Field('member_id','string'),
    Field('event_id','string'),
    Field('title','string'),
    Field('thread_content','text'),
)

################################
####event_project###############
################################
db.define_table('event_project',
    Field('event_id','string'),
    Field('project_id','string'),
    Field('date_submitted','string'),
)

################################
####event_page##################
################################
db.define_table('event_page',
    Field('member_id','string'),
    Field('event_id','string'),
    Field('title','string'),
    Field('page_content','text'),
)

################################
####follower####################
################################
db.define_table('follower',
    Field('user_following_id', 'reference auth_user', default=auth.user_id, readable=False, writable=False),
    Field('user_followed_id','reference auth_user', readable=False, writable=False)
)

################################
####message#####################
################################
db.define_table('message',
    Field('member_id_array', 'list:string'),
    Field('message_title','string'),
    Field('message_content','string'),
    Field('message_time', 'datetime', default=request.now),
)




