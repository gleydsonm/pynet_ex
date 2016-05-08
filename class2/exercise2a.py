#!/usr/bin/env python
'''
Python + ansible - Exercise 2a
I'm using on this example a method to check for login failures. Also, the non
sensitive data are received directly by command line parameters

Gleydson Mazioli da Silva <gleydsonmazioli@gmail.com>
'''

import sys
import time
import telnetlib
import socket
import getpass
import re

# Global variables
TELNET_TIMEOUT = 5

def telnet_connect(l_ip_addr, l_port):
    '''
    Connect to the remote host
    '''
    try:
        return telnetlib.Telnet(l_ip_addr, l_port, TELNET_TIMEOUT)
    except socket.error:
        sys.exit("Telnet: Connection refused")
    except socket.timeout:
        sys.exit("Telnet: Connection timed out")

def telnet_login(remote_conn, username, password):
    '''
    Login on the remote host
    '''
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output


def telnet_logout(remote_conn):
    '''
    Logout from the remote host
    '''
    remote_conn.close()

def send_command(remote_conn, cmd):
    '''
    Send commands to the remote host
    '''
    cmd = cmd.rstrip()
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    '''
    Read connections parameters from the command line
    '''
    print sys.argv
    if len(sys.argv) < 4:
        sys.exit('Parameters: ' + sys.argv[0] + ' [dst_ip] [port] [username]')
    telnet_ip = sys.argv[1]
    telnet_port = sys.argv[2]
    telnet_username = sys.argv[3]
    telnet_password = getpass.getpass()

    conn_handle = telnet_connect(telnet_ip, telnet_port)
    output = telnet_login(conn_handle, telnet_username, telnet_password)
    time.sleep(1)
    output = conn_handle.read_very_eager()

    expr = re.compile('#')
    if not expr.search(output):
        print 'Incorrect login or password. Exiting'
        sys.exit()
    else:
        print 'We are in!'

    output = conn_handle.read_very_eager()
    print output
    send_command(conn_handle, 'terminal lenght 0')
    time.sleep(1)
    output = send_command(conn_handle, 'show ip int brief')
    print output

    telnet_logout(conn_handle)

if __name__ == '__main__':
    main()

