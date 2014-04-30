################################################################
####controllers#################################################
################################################################
  
################################
####about#######################
################################
def about():
    return dict(message=T('Hello World'))

################################
####account#####################
################################
def account():
    return dict(message=T('Hello World'))    

################################
####contact#####################
################################
def contact():
    return dict(message=T('Hello World'))
    
################################
####discover####################
################################
def discover():
    return dict()

################################
####event#######################
################################
def event():
    try:
        event_from_url = db(db.event.url_title == request.args(0)).select()[0]
        event_threads = db(db.event_thread.event_id == event_from_url['id']).select()
        event_pages = db(db.event_page.event_id == event_from_url['id']).select()

        form_create_thread = SQLFORM(db.event_thread)
        if form_create_thread.process(formname='form_create_comment').accepted:
            #db.collection_member.insert(collection_id = form_create_collection.vars.id, user_id = auth.user_id, collection_usergroup_id=0)
            session.flash = 'thread created'
            redirect(URL('/event/' + str(event_from_url['url_title'])))     
        elif form_create_thread.errors:
            session.flash = 'Error'   
            redirect(URL(''))

        form_create_page = SQLFORM(db.event_page)
        if form_create_page.process(formname='form_create_page').accepted:
            #db.collection_member.insert(collection_id = form_create_collection.vars.id, user_id = auth.user_id, collection_usergroup_id=0)
            session.flash = 'page created'
            redirect(URL('/event/' + str(event_from_url['url_title'])))     
        elif form_create_page.errors:
            session.flash = 'Error'   
            redirect(URL(''))

        event_member_list = db(db.event_member.event_id == event_from_url['id']).select()

    except IndexError:
        redirect(URL('events'))

    return dict(
        event_threads=event_threads,
        event_from_url=event_from_url,
        form_create_thread=form_create_thread,
        event_pages=event_pages,
        form_create_page=form_create_page,
        event_member_list=event_member_list,

    )

################################
####event#######################
################################
def events():
    event_list = db(db.event).select()
    return dict(event_list=event_list)  
  
################################
####faq#########################
################################
def faq():
    return dict()

################################
####feed########################
################################
def feed():
    return dict()

################################
####group#######################
################################
def group():
    return dict(message=T('Hello World'))

################################
####groups######################
################################
def groups():
    return dict(message=T('Hello World'))    

################################
####help########################
################################
def help():
    return dict()

################################
####inbox#######################
################################
def inbox():
    return dict()

################################
####index#######################
################################
def index():
    project_list = db(db.project).select()
    event_list = db(db.event).select()

    return dict(
        project_list=project_list,
        event_list=event_list,
    )

################################
####member######################
################################
def member():
    try:
        member_from_url = db(db.auth_user.username == request.args(0)).select()[0]
    except IndexError:
        redirect(URL('index'))

    return dict(member_from_url=member_from_url)
################################
####mission#####################
################################
def mission():
    return dict()

################################
####notifications###############
################################
def notifications():
    return dict()

################################
####positions###################
################################
def positions():
    return dict()
    
################################
####privacy#####################
################################
def privacy():
    return dict()

################################
####projects####################
################################    
def projects():
    project_list = db(db.project).select()
    create_project = SQLFORM(db.project)
    return dict(
        project_list=project_list,
        create_project=create_project,
    )

################################
####project#####################
################################
def project():
    try:
        project_from_url = db(db.project.url_title == request.args(0)).select()[0]
        project_member_list = db(db.project_member.project_id == project_from_url['id']).select()

    except IndexError:
        redirect(URL('projects'))

    return dict(
        project_from_url=project_from_url,
        project_member_list=project_member_list,
    )


################################
####search######################
################################
def search():
    return dict(message=T('Hello World'))

################################
####tasks#######################
################################
def tasks():
    return dict()

################################
####terms#######################
################################
def terms():
    return dict()

################################
####thread######################
################################
def thread():
    return dict(message=T('Hello World'))

################################
####stats#######################
################################
def stats():
    return dict(message=T('Hello World'))

################################
####threads#####################
################################
def thread():
    return dict(message=T('Hello World'))

################################
####transparency################
################################
def transparency():
    return dict(message=T('Hello World'))    



################################################################
####helpers#####################################################
################################################################

@cache.action()
def download():
    return response.download(request, db)

@auth.requires_login()
def call():
    return service()

@auth.requires_signature()
def data():
    return dict(form=crud())

@service.xmlrpc
def test_add(a,b):
    number_sum = a+b
    db.testing.insert(number_sum=number_sum)
    return a+b

def test():
    from xmlrpclib import ServerProxy
    from google.appengine.api import urlfetch
    URL = "https://troverman:trev77922@troverman-conexus.appspot.com/conexus/default/call/xmlrpc"
    urlfetch.set_default_fetch_deadline(60)
    service = ServerProxy(URL, verbose=True)
    test = service.test_add(1, 2)
    return test



def inlrn_login():
    from xmlrpclib import ServerProxy
    from google.appengine.api import urlfetch
    URL = "https://troverman:trev77922@troverman-inlrn.appspot.com/inlrn/default/call/xmlrpc"
    urlfetch.set_default_fetch_deadline(60)
    service = ServerProxy(URL, verbose=True)
    test = service.test_add(50, 2)

    return test












################################################################
####ajax########################################################
################################################################

################################
####ajax_join_event#############
################################                     
def ajax_join_event():
    event_id = int(request.vars.id)
        
    #LOGIC
    db.event_member.insert(member_id = auth.user_id, event_id = event_id, event_membergroup_id_array=1)
    jquery = "jQuery('.flash').html('joined event').slideDown().delay(1000).slideUp();"

    return jquery 


    
################################
####ajax_leave_event############
################################     
def ajax_leave_event():
    event_id = request.vars.itervalues()
    for x in event_id:
        event_id_trim = int(x)

    #LOGIC
    db((db.event_member.member_id==auth.user_id) & (db.event_member.collection_id==event_id_trim)).delete()
    jquery = "jQuery('.flash').html('left event').slideDown().delay(1000).slideUp();"

    return jquery
       

################################
####ajax_join_project###########
################################                     
def ajax_join_project():
    project_id = int(request.vars.id)
        
    #LOGIC
    db.project_member.insert(member_id = auth.user_id, project_id = project_id, project_membergroup_id_array=1)
    jquery = "jQuery('.flash').html('joined project').slideDown().delay(1000).slideUp();"


    return jquery      
    
################################
####ajax_leave_project##########
################################     
def ajax_leave_project():
    project_id = request.vars.itervalues()
    for x in project_id:
        project_id_trim = int(x)

    #LOGIC
    db((db.project_member.member_id==auth.user_id) & (db.project_member.project_id==project_id_trim)).delete()
    jquery = "jQuery('.flash').html('left project').slideDown().delay(1000).slideUp();"

    #jquery += "$('#leave-collection-%s').fadeToggle(100);" % collection_id_trim
    #jquery += "$('#join-collection-%s').delay(100).fadeToggle(400);" % collection_id_trim   
    return jquery




