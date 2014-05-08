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
from pyramid.response import Response
from pyramid.view import view_config
from server import get_session
import json

@view_config(route_name='home', renderer='templates/testajax.pt')
def home_view(request):
	#res = "Route Info for Bus number 210:{0} {1} {2}".format('Chamrajpet','Lalbagh','NR Colony')	
	return Response('<h2><p>Welcome</p></h2>')


@view_config(route_name='bus')
def form_view(request):
	result = render('templates/testajax.pt',
	                {'start_point':'Majestic','end_point':'Uttarahalli','route':'Chamrajpet Lalbagh'},
	                request=request)
	response = Response(result)
	return response


@view_config(route_name='first')
def resource_view(request):
	result = render('json',
		"Starting:{0} Ending:{1} Route info:{2} {3} {4} {5}".format('Majestic','Uttarahalli','Corporation','Chamrajpet','NRcolony','Chikkallasandra'),
			request=request)
	response = Response(result)
	return response
