from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class BusRoute(Base):
	"""class for creating table to store the busroutes into the database
	"""
	__tablename__ = 'busroutes'
	
	bus_no = Column(Integer, primary_key=True)
	start_point = Column(String(100))
	end_point = Column(String(100))
	route = Column(String(200))


	def __repr__(self):
		"""Method to display bus routes"""
		return "<BusClass(start_point='%s', end_point='%s', route='%s')>" % (
                             self.start_point, self.end_point, self.route)
