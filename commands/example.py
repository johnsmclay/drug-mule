import getopt

class Example:
	description = 'This is an example command'
	usage = 'example -i <inputfile> -o <outputfile>'

	def execute(self, arguments):
		# Process the arguments
		# see for more info
		#   http://www.tutorialspoint.com/python/python_command_line_arguments.htm
		# ==============================================
		inputfile = ''
		outputfile = ''
		try:
			opts, args = getopt.getopt(arguments,"hi:o:",["ifile=","ofile="])
		except getopt.GetoptError:
			print self.usage
			exit(2)
		for opt, arg in opts:
			if opt in ('-h', '--help'):
				print self.usage
				exit()
			elif opt in ("-i", "--ifile"):
				inputfile = arg
			elif opt in ("-o", "--ofile"):
				outputfile = arg
		# ==============================================

		# Do your work here
		print 'Executed command "example"'