import getopt
from tools import database
from models.connection import Connection
from models.system_variable import SystemVariable

class Migrate:
	description = 'Run database migrations.'
	usage = 'migrate'

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

		

		print database.Base.metadata.create_all(database.get_engine)


		#session = database.get_app_session()