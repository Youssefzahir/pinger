# pinger
Pinger "A Python ping script"


Use:
----------
Used to ping different ip addresses from cli in one line.
It accepts command line arguments to use a file containing IP addresses to ping.
If pinger is run without command argument it will default to presenting prompts to guide user.

  usage: pinger.py [-h] [-f FILE] [address [address ...]]

  Pings IP addresses entered or from file

  positional arguments:
    address               address(s) (default: None)

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  Input file (default: None)


Overview:
---------
Pinger allows you to ping different ip addresses by entering the IP addresses seperated by a comma
or by entering the name of a text file containing the ip addresses when prompted.
It works with hostnames as well as long as your DNS is able to resolve the address. 
This script gives the user 3 attempts at performing the ping test and then quits

Using text file:
---------------
The text file format is to have one ip address per line.
text file must be placed in same directory as script.


NB* If you continue to get "is not reachable" for reachabe addresses or the script gets stuck with the cursor blinking
check to make sure that you have uncommented the correct "myresponse" variable definition 
