from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render
from pyramid.view import view_config
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy import create_engine
from busroutes import BusRoute
from busroutes import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pyramid.renderers import render
from pyramid.renderers import render_to_response
from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config
from server import get_session
from json import loads
# loads(request.body, encoding=request.charset)
from pyramid.static import static_view
static_view = static_view('/path/to/static/dir', use_subpath=True)

@view_config(route_name='home', renderer='templates/index.pt')
def home_view(request):	
	return Response('<h1><p>Welcome</p></h1>')


@view_config(route_name='bus')
def form_view(request):
	result = render('templates/index.pt',
	                {'start_point':'Majestic','end_point':'Uttarahalli','route':'Chamrajpet Lalbagh'},
	                request=request)
	response = Response(result)
	return response

# @view_config(route_name='controller', renderer='app/js/controller.js')
# def contr_view(request):
# 	return Response('<p>Controller file</p>')

# @view_config(route_name='angular')
# def ang_view(request):
# 	result = render('app/js/angular.min.js',
# 		{'angular':'library minified version'}, request=request)
# 	response = Response(result)
# 	return response


@view_config(route_name='busroutes', renderer='busroutes.json')
def resource_view(request):
	return Response(contentType="application/json")

#
# def static_view(request):
# 	js_url1 = request.static_url('app:js/controller.js')
# 	js_url2 = request.static_url('app:angular.min.js')
# 	return render_to_response('templates/index.pt',
#                               dict(js_url=js_url2),
#                               request=request)