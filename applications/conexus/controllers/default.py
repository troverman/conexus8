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

        form_create_event_project = SQLFORM(db.event_project)
        if form_create_event_project.process(formname='form_create_event_project').accepted:
            #db.collection_member.insert(collection_id = form_create_collection.vars.id, user_id = auth.user_id, collection_usergroup_id=0)
            session.flash = 'project submitted'
            redirect(URL('/event/' + str(event_from_url['url_title']) + '/projects/'))     
        elif form_create_event_project.errors:
            session.flash = 'Error'   
            redirect(URL(''))

        event_member_list = db(db.event_member.event_id == event_from_url['id']).select()

        the_event_member_list = []
        for member in event_member_list:
            the_event_member_list.append(db(db.auth_user.id == member['member_id']).select()[0])


    except IndexError:
        redirect(URL('events'))

    return dict(
        form_create_event_project=form_create_event_project,
        event_threads=event_threads,
        event_from_url=event_from_url,
        form_create_thread=form_create_thread,
        event_pages=event_pages,
        form_create_page=form_create_page,
        event_member_list=event_member_list,
        the_event_member_list=the_event_member_list,

    )

################################
####event#######################
################################
def events():
    event_list = db(db.event).select()

    form_create_event = SQLFORM(db.event)
    if form_create_event.process(formname='form_create_event').accepted:
        #db.collection_member.insert(collection_id = form_create_collection.vars.id, user_id = auth.user_id, collection_usergroup_id=0)
        session.flash = 'event created'
        redirect(URL('/event/' + str(form_create_collection.vars.url_title) + '/admin/'))     
    elif form_create_event.errors:
        session.flash = 'Error'   
        redirect(URL('events'))
    return dict(
        event_list=event_list,
        form_create_event=form_create_event,
    )  
  
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

    message_list = db(db.message.member_id_array.contains(auth.user_id)).select()

    form_create_message = SQLFORM(db.message)
    if form_create_message.process(formname='form_create_message').accepted:
        #db.collection_member.insert(collection_id = form_create_collection.vars.id, user_id = auth.user_id, collection_usergroup_id=0)
        session.flash = 'message sent'
        redirect(URL('/inbox/' + str(form_create_message.vars.id)))  
    elif form_create_message.errors:
        session.flash = 'Error'   
        redirect(URL(''))


    return dict(
        form_create_message=form_create_message,
        message_list=message_list,
    )

################################
####index#######################
################################
def index():
    project_list = db(db.project).select()
    project_list_array = []
    for project in project_list:
        picture = db(db.project_picture.project_id == project['id']).select()
        project_list_array.append([project, picture])


    event_list = db(db.event).select()

    return dict(
        project_list=project_list,
        event_list=event_list,
        project_list_array=project_list_array,
    )

################################
####member######################
################################
def member():
    try:
        member_from_url = db(db.auth_user.username == request.args(0)).select()[0]
        project_list = db(db.project_member.member_id == member_from_url['id']).select()
        message_list = db(db.message.member_id_array.contains(member_from_url['id'])).select()
        event_list = db(db.event_member.member_id == member_from_url['id']).select()

        the_project_list = []
        for project in project_list:
            the_project_list.append(db(db.project.id == project['project_id']).select())

        the_event_list = []
        for event in event_list:
            the_event_list.append(db(db.event.id == event['event_id']).select())

        member_picture = db(db.member_picture.member_id == member_from_url['id']).select()
        member_account = db(db.member_account.member_id == member_from_url['id']).select()

    except IndexError:
        redirect(URL('index'))

    return dict(
        member_from_url=member_from_url,
        the_project_list=the_project_list,
        the_event_list=the_event_list,
        message_list=message_list,
        member_picture=member_picture,
        member_account=member_account,
    )
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
    if create_project.process(formname='create_new_page_form').accepted:           
        db.project_membergroup.insert(project_id=create_project.vars.id, title="admin", description="this is the admin")
        db.project_membergroup.insert(project_id=create_project.vars.id, title="member", description="project member")
        db.project_member.insert(project_id=create_project.vars.id, member_id=auth.user_id, join_date=request.now, project_membergroup_id_array=[])

        session.flash = 'project created'
        redirect(URL('/project/' + create_project.vars.url_title))
    elif create_project.errors:
        session.flash = 'Error' 
        redirect(URL(''))
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
        the_project_member_list = []
        for member in project_member_list:
            the_project_member_list.append(db(db.auth_user.id == member['member_id']).select()[0])


        create_new_page_form = SQLFORM(db.project_page)
        if create_new_page_form.process(formname='create_new_page_form').accepted:           
            db(db.project_page.id==create_new_page_form.vars.id).update(project_id=project_from_url['id'])
            session.flash = 'page created'
            redirect(URL('/project/' + project_from_url['url_title'] + '/pages'))
        elif create_new_page_form.errors:
            session.flash = 'Error' 
            redirect(URL(''))



        form_create_task = SQLFORM(db.project_task)
        if form_create_task.process(formname='form_create_task').accepted:
            db(db.project_task.id==form_create_task.vars.id).update(project_id=project_from_url['id'])
            session.flash = 'task created'
            redirect(URL('/project/' + str(project_from_url['url_title'])))     
        elif form_create_task.errors:
            session.flash = 'Error'   
            redirect(URL(''))


        task_list = db(db.project_task.project_id == project_from_url['id']).select()
        page_list = db(db.project_page.project_id == project_from_url['id']).select()

        task_tag_list = []
        for task in task_list:
            task_tag_list.append((db(db.project_task_tag.project_task_id == task['id']).select()))

        task_tag_list_array = []
        for tag_list in task_tag_list:
            for tag in tag_list:
                task_tag_list_array.append(tag['tag'])   

        set_task_tag_list = set(task_tag_list_array)
        tag_task_list_unsorted = list(set_task_tag_list)
        combined_count_and_tag_array=[]
        for tag in tag_task_list_unsorted:
            combined_count_and_tag_array.append([tag, task_tag_list_array.count(tag)])
        from operator import itemgetter
        tag_task_list_sorted_by_total_count = sorted(combined_count_and_tag_array, key=itemgetter(1))  

        feed_array = []
        for task in task_list:
            feed_array.append(task)
        for page in page_list:
            feed_array.append(page)
        for member in project_member_list:
            feed_array.append(member)

        project_picture = db(db.project_picture.project_id == project_from_url['id']).select()

        page_content=''
        membergroup_array=''
        if request.args(1) == 'page':
            if request.args(2):
                page_content = db(db.project_page.id == request.args(2)).select()

        if request.args(1) == 'settings':
            membergroup_array = db(db.project_membergroup.project_id == project_from_url['id']).select()


    except IndexError:
        redirect(URL('projects'))

    return dict(
        membergroup_array=membergroup_array,
        page_list=page_list,
        create_new_page_form=create_new_page_form,
        project_from_url=project_from_url,
        form_create_task=form_create_task,
        task_list=task_list,
        the_project_member_list=the_project_member_list,
        tag_task_list_sorted_by_total_count=tag_task_list_sorted_by_total_count,
        feed_array=feed_array,
        project_picture=project_picture,
        page_content=page_content,
    )


################################
####search######################
################################
def search():
    return dict(message=T('Hello World'))


################################
####streams#####################
################################
def streams():
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
    import base64
    from xmlrpclib import ServerProxy
    from google.appengine.api import urlfetch
    URL = "https://troverman-inlrn.appspot.com/inlrn/default/call/xmlrpc"
    urlfetch.set_default_fetch_deadline(60)
    #result = urlfetch.fetch(URL, headers={"Authorization": "Basic %s" % base64.b64encode("troverman:trev77922")})

    service = ServerProxy(URL, verbose=True)
    test = service.test_add(50, 2)


    return test

def test_deliveryfor():

    from gluon.contrib.simplejsonrpc import ServerProxy
    from google.appengine.api import urlfetch
    URL = "https://troverman-deliveryfor.appspot.com/deliveryfor/default/call/jsonrpc"
    urlfetch.set_default_fetch_deadline(60)
    service = ServerProxy(URL, verbose=True)
    test = service.test_add(50, 2)
    #test=''
    return test








################################################################
####ajax########################################################
################################################################
################################
####ajax_discover###############
################################                     
def ajax_discover():
    discover_content = DIV('lolololol') + BR()
    jquery = "$('#discover-content').append('%s');" % discover_content
    jquery += "jQuery('.flash').html('check it out').slideDown().delay(1000).slideUp();"

    return jquery 

################################
####ajax_join_event#############
################################                     
def ajax_join_event():
    event_id = int(request.vars.id)
        
    if auth.user_id is not None:
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
        
    if auth.user_id is not None:
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

################################
####ajax_follow_member##########
################################                                         
def ajax_follow_member():
    member_id = int(request.vars.id)
    #LOGIC
    #db.follower.insert(user_following_id = auth.user_id, user_followed_id = member_id_trim)
    jquery = "jQuery('.flash').html('following').slideDown().delay(1000).slideUp();"
    return jquery
    
################################
####ajax_un_follow_member#######
################################ 
def ajax_un_follow_member():
    #member_id = request.vars.itervalues()
    #for x in member_id:
        #member_id_trim = int(x)  
    #db((db.follower.user_following_id==auth.user_id) & (db.follower.user_followed_id==member_id_trim)).delete()
    jquery = "jQuery('.flash').html('unfollowed').slideDown().delay(1000).slideUp();"
    #jquery += "$('#unfollow').fadeToggle(100);"
    #jquery += "$('#follow').delay(100).fadeToggle(100);"
    return jquery


