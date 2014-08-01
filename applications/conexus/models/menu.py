##########################################
####title#################################
##########################################
if request.function == 'index':                                                                                                                                 
    response.title = 'conex.us'    
elif request.function == 'event':  
    event_name = db(db.event.url_title == request.args(0)).select()[0]['title']
    response.title = event_name + ' - conex.us'
elif request.function == 'project':  
	project_name = db(db.project.url_title == request.args(0)).select()[0]['title']
	response.title = project_name + ' - conex.us'                                                                                                                              
else:
    response.title = request.function


## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Trevor Overman <you@example.com>'
response.meta.description = 'paying the way for a better tomorrow'
response.meta.keywords = 'conexus, transparent, network'
response.meta.generator = 'connecting us all'

