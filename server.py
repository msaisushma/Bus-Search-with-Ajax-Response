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

DOMAIN = '0.0.0.0'
PORT = 8008

DB_NAME = 'buses.db'

def get_engine():
	"""Creates engine every single time this method is called"""
	print "inside bus create engine"
	engine = create_engine('sqlite:///%s' % DB_NAME, echo=True)
	return engine

def get_session(engine):
	"""
	Creates session object every single time this method is called
	"""
	return sessionmaker(bind=engine)()


def create_configuration():
	"""
	Prepares configuration and adds routes to it
	"""
	config = Configurator()
	config.add_route('home', '/')
	config.add_route('bus', '/bus/')
	config.add_route('response', '/response')
	config.add_route('first','/first')
	config.add_route('source','/source')
	config.include('pyramid_chameleon')
	config.scan('views')
	return config


def start_server(config):
	"""
	Runs a pyramid server at the configured domain:port
	"""
	app = config.make_wsgi_app()
	server = make_server(DOMAIN, PORT, app)
	print 'Server Started listening on %s:%s' % (DOMAIN, PORT)
	server.serve_forever()
 
if __name__ == '__main__':
	config = create_configuration()
	start_server(config)
