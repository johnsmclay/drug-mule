# drug-mule
FTP/SFTP/SCP/Etc. Daemon for pushing/pulling files on a schedule.

## System Information
### Command Framework
The entire system is built around different "commands" that function much like the views from an MVC framework.

Each command is in it's own python file inside the `commands/` directory.  Inside the Python file is a class with the same name as the command, but with the first letter capitalized.  For example, the command "example" is located in `commands/example.py` and has a class that starts with `class Example:`.

Commands are called like this:
```
> ./main.py <command> [parameter1 parameter2 ...]
```

Each command class has the following components and can be seen in the example command file mentioned above.

 - Class Variables
   - "description": holds a description of what the command does and is displayed when the --help or -h parameters are passed in the main app with no command.
   - "usage": holds an explanation of how to use the command and is displayed when the --help or -h parameters are passed in with the command.
 - Methods
   - `execute(self, arguments)`: when the command is called this is the method that will be executed.  All parameters after the parameter for the command are passed on to the method in the `arguments` variable. 