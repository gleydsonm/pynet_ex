#!/usr/bin/env python
'''
Exercise 1 - Class 4
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''
import paramiko
import sys
import socket
import time

def get_data(conn):
    '''
    Get the data from the buffer
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
    Disable the paging
    '''
    send_command(conn, 'terminal length 0\n')

def main():
    '''
    Main function
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
    send_command(shell, 'show version')
    ret = get_data(shell)
    print ret
    # Close the established connection with the remote router (resource saving)
    conn.close()

if __name__ == "__main__":
    main()

