#!/usr/bin/env python
import sys
import tools.system as system_tools

COMMANDS_MODULE = 'commands'

def get_command_class_info(command_text):
	command_module_path = '%s.%s' % (COMMANDS_MODULE,command_text)
	command_class_name = command_text.title()
	return (command_module_path, command_class_name)

def print_usage():
	print 'Usage: "./main.py <command> [<parameter>] ..."'
	print '   all parameters after the command are passed to the command'
	print 'Available Commands:'

	command_descriptions = {}
	command_mods = system_tools.package_contents('commands') #.discard('__init__')
	for command_mod_text in command_mods:
		if str(command_mod_text) in ['__init__']:
			continue
		#command = get_command_instance(command_mod_text)
		command = system_tools.get_dynamic_class(*get_command_class_info(command_mod_text))()
		command_descriptions[command_mod_text] = command.description

	max_len = 0
	for name, description in command_descriptions.iteritems():
		if len(name) > max_len:
			max_len = len(name)
	for name, description in command_descriptions.iteritems():
		padded_name = ('"%s"' % name).ljust(max_len+2)
		print '    %s -- %s' % (padded_name, description)
	exit()

if len(sys.argv) > 1:
	command_text = sys.argv[1]
else:
	print 'Please supply a command'
	print_usage()

command_mods = system_tools.package_contents('commands')
if command_text not in command_mods:
	print 'Command "%s" supplied does not exist.' % (command_text)
	print_usage()

command = system_tools.get_dynamic_class(*get_command_class_info(command_text))()

command_arguments = sys.argv[2:]

command.execute(command_arguments)