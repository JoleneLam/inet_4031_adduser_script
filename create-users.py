#!/usr/bin/env python2
import os
import re
import sys
def main():
    for line in sys.stdin:
        match = re.match(r'^#', line)
        match = re.match('%', line)
        fields = line.strip().split(':') #strip any whitespace and split into an array
        if match or len(fields) != 5: #checks if the regular expression pattern was found and if the number of elements in 'fields' is not equal to 5. This condition is used to fliter out lines that either start with '#' or do not have the expected number of 'fields'
            continue #if the conditon is not met in the FOR loop, the continue function with end the current iteration.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',') #this line splits the string stored in 'field[4]' into a list of substrings. This line extracts groups associated with the user form input line and store them in a list. 
        print("==> Creating accout for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        print(cmd)
        os.system(cmd) #executes sell commands from within Python script. It runs a specific command in the operating systems's shell and return the exit code of the command.It enables integration between Python script and shell command.
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        os.system(cmd)
        for group in groups: #This FOR loop interates over each element in the 'groups' list. This allows users to access the individual element in 'groups' and execute code for each element (group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)
if __name__ == '__main__':
    main()
