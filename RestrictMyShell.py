#!/usr/bin/python
import os
import re
import readline
import sys
import subprocess
os.system('clear')
print 'WELCOME TO THE RESTRICTED SHELL'
if not os.path.exists('/etc/restrictmyshell'):
    open('/etc/restrictmyshell','w')
    print '\nEdit /etc/restrictmyshell with Whitelisted Commands'
    sys.exit(1)
while True:
    File = open('/etc/restrictmyshell', 'r')
    allowedcommands = []
    for word in File:
        allowedcommands.append(word.rstrip('\n'))
    try:
        command = raw_input('%s@PyShell> ' %
                            subprocess.check_output(["whoami"]).rstrip('\n'))
        command = command.lstrip(' ')
    except (KeyboardInterrupt, EOFError):
        print '\n'
        continue
    command = command.split(' ')
    flag = False
    newCommand = ''
    for x in allowedcommands:
        if command[0] == 'exit':
            sys.exit(0)
        try:
            if command[0] == 'cd':
                os.chdir(command[1])
        except:
            pass
        if command[0] == x:
            for f in command:
                newCommand += re.sub(r'([\|\$\&\<\>\|\(\)\:\!\{\}\[\]\;\`].*)', r'', f) + ' '
                if command[0] == 'ls':
                    newCommand += ' --color=always '
            break

    if newCommand == '':
        print "You Are Not Allowed To Run This Command!"
    else:
        subprocess.call(newCommand, shell=True)
