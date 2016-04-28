from sqlalchemy import Column, Integer, String, Sequence
from tools.database import Base

class SystemVariable(Base):
	__tablename__ = 'system_variable'

	id = Column(Integer, Sequence('connection_id_seq'), primary_key=True)
	key = Column(String)
	value_type = Column(String)
	value = Column(String)

	def __repr__(self):
		return "<User(key='%s', value_type='%s')>" % (
	    	self.key,
	    	self.value_type
	    )