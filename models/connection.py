from sqlalchemy import Column, Integer, String, Sequence
from tools.database import Base

class Connection(Base):
	__tablename__ = 'connection'

	id = Column(Integer, Sequence('connection_id_seq'), primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (
	    	self.name,
	    	self.fullname,
	    	self.password
	    )