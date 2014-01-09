################################################################
####controllers#################################################
################################################################

################################
####api#########################
################################
def api():

    return dict(message=T('Hello World'))
    
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
####index#######################
################################
def index():

    return dict(message=T('Hello World'))

################################
####member######################
################################
def member():
    
    return dict()

################################
####projects####################
################################    
def projects():

    return dict(message=T('Hello World'))

################################
####project#####################
################################
def project():

    return dict(message=T('Hello World'))

################################
####thread######################
################################
def thread():

    return dict(message=T('Hello World'))

################################
####threads#####################
################################
def index():

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
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
