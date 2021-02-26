# pinger
Pinger "A Python ping script"


Use:
----------
I was looking for a way to ping a number of different ip addresses and get a response to wether the addresses were up or not.
So I came up with Pinger a python script that is able to achieve this.

Overview:
---------
Pinger allows you to ping different ip addresses by entering the IP addresses seperated by a comma
or by entering the name of a text file containing the ip addresses when prompted.
It works with hostnames as well as long as your DNS is able to resolve the address. 
This script gives the user 3 attempts at performing the ping test and then quits

using text file:
---------------
The text file format is to have one ip address per line.
text file must be placed in same directory as script.


NB* If you continue to get "is not reachable" for reachabe addresses or the script gets stuck with the cursor blinking
check to make sure that you have uncommented the correct myresponse variable definition 
