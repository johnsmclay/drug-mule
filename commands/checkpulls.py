import getopt
from tools import database
from models.connection import Connection
from models.system_variable import SystemVariable

class Checkpulls:
	description = 'This check all the scheduled file pulls.'
	usage = 'checkpulls'

	def execute(self, arguments):
		# Process the arguments
		# ==============================================
		try:
			opts, args = getopt.getopt(arguments,"h",[])
		except getopt.GetoptError:
			print self.usage
			exit(2)
		for opt, arg in opts:
			if opt in ('-h', '--help'):
				print self.usage
				exit()
		# ==============================================

		session = database.get_app_session()

		ed_user = Connection(name='ed', fullname='Ed Jones', password='edspassword')

		print ed_user.name
		print ed_user.password

		session.add(ed_user)
		our_user = session.query(Connection).filter_by(name='ed').first()

		print our_user