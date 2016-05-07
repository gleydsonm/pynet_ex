#!/usr/bin/env python
'''
Exercise 3 - Class 4
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''
import pexpect
import sys

def send_command(conn, cmd, exp, exp2):
    '''
    Send a command to the remote host and expect a reply
    '''
    if len(cmd) == 0:
        return False
    cmd = cmd.strip()
    conn.timeout = 3
    try:
        if len(exp2) >= 0:
            try:
                conn.expect(exp2)
            except pexpect.TIMEOUT:
                return False
        conn.send(cmd +'\n')
        conn.expect(exp)
    except pexpect.TIMEOUT:
        return False
    return [conn.before, conn.after]


def main():
    '''
    Main function
    '''
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    passwd = '88newclass'

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ret = send_command(ssh_conn, passwd, 'pynet-rtr', 'assword:')
    if not ret:
        sys.exit('Invalid login or username')

    ret = send_command(ssh_conn, 'show ip int brief', 'pynet-rtr', '')
    print ret[0]

    # Close the opened connection (to free resources)
    ssh_conn.close()

if __name__ == "__main__":
    main()

