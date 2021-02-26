#!/usr/bin/env python
# source venv/bin/activate
import os
import subprocess
import pyinputplus as pyip

print('#' * 36)
print('#' + ((' ') * 7) + '-- Running Pinger --' + ((' ') * 7) + '#')
print('#' * 36)


''' You can substitute the ping response string for the different OS's e.g. windows, Mac, and Linux'''

#myresponse = ['1 received', '-c']       # for linux response
myresponse = ['Received = 1', '-n']     #for windows response
#myresponse = ['1 packets received', '-c']    #for mac response

proceed = 0


def From_file_2_list(filename):
    # goes through file, creates list and dumps complete list
    with open(filename, 'r') as ftext:
        flist = ftext.readlines()
        mylist = [i[:-1] for i in flist]
    print('Loaded File to List.')
    return mylist


def ping_os(addy, os_response=myresponse):
    try:
        pingout = subprocess.run(
            ['ping', os_response[1], '1', f'{addy}'], stdout=subprocess.PIPE, text=True)
        if os_response[0] in pingout.stdout:
            print(f'{addy} is UP!')
        else:
            print(f'{addy} did not Respond!')
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    return

# -------------------------------------------------------------------
while proceed < 3:
    try:
        ask_to_use_file = pyip.inputYesNo(
            'Do you want to use a file ? [Y or N]: ')

        if ask_to_use_file == 'yes':
            pingfile = pyip.inputStr('Enter filename: ')
            pinglist_file = From_file_2_list(pingfile)
            print(f'Performing ping from file: {pingfile}')

            for i in pinglist_file:
                ping_os(i)
        else:
            pingaddrs = pyip.inputStr(
                'Enter addresses seperated by comma "," : ')
            pinglist_args = pingaddrs.split(',')
            for i in pinglist_args:
                # split method below used to take only address and no further options
                ping_os(i.split()[0], myresponse)
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    ask_to_continue = pyip.inputYesNo('Do you want retry ? [Y or N]: ')
    if ask_to_continue == 'yes':
        proceed += 1
    else:
        break

print('Maximum number of retries reached') if proceed == 3 else print('Done. ')
input('Press Enter to Close: ')
