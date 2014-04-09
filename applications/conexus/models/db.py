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
####member_location#############
################################
db.define_table('member_location',
    Field('member_id','string'),
    Field('time_stamp','datetime'),
    Field('location_lat','string'),
    Field('location_lng','string'),
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
)

################################
####project_member##############
################################
db.define_table('project_member',
    Field('member_id','string'),
    Field('project_id','string'),
    Field('project_membergroup_id_array','list:string'),
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
####event_page##################
################################
db.define_table('event_page',
    Field('member_id','string'),
    Field('event_id','string'),
    Field('title','string'),
    Field('page_content','text'),
)




