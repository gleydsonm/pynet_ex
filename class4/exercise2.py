#!/usr/bin/env python
'''
Exercise 2 - Class 4
Gleydson Mazioli
'''
import paramiko
import sys
import socket
import time

def get_data(conn):
    '''
    Get the data from buffer
    '''
    if conn.recv_ready():
        return conn.recv(65535)

def send_command(conn, cmd=''):
    '''
    Send a command
    '''
    if len(cmd) == 0:
        return False
    cmd = cmd.strip()
    conn.send(cmd + '\n')
    time.sleep(2)

def disable_page(conn):
    '''
    Disable paging
    '''
    send_command(conn, 'terminal length 0\n')

def main():
    '''
    Main Function
    '''
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    port = 8022

    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    except socket.error:
        sys.exit('Unable to connect to the remote host. Check IP and port')
    shell = conn.invoke_shell()

    disable_page(shell)
    send_command(shell, 'conf t')
    print get_data(shell)
    send_command(shell, 'logging buffered 65535')
    print get_data(shell)

    # Free the connection established with the server (resources saving)
    conn.close()

if __name__ == "__main__":
    main()

