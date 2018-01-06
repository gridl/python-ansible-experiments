import telnetlib
import time
import socket

COMMAND = 'sh run'.encode('utf-8')
USER = 'cisco'.encode('utf-8')
PASSWORD = 'cisco'.encode('utf-8')
ENABLE_PASS = 'cisco'.encode('utf-8')


#DEVICES_IP = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
DEVICES_IP = ['192.168.100.1']


for IP in DEVICES_IP:
    print('Connection to device {}'.format(IP))
    with telnetlib.Telnet(IP, timeout=5) as t:

        t.read_until(b'Username:')
        t.write(USER + b'\n')

        t.read_until(b'Password:')
        t.write(PASSWORD + b'\n')
        t.write(b'enable\n')

        t.read_until(b'Password:')
        t.write(ENABLE_PASS + b'\n')
        t.write(b'terminal length 0\n')

        time.sleep(1)
        t.read_very_eager()
        t.write(COMMAND + b'\n')
        data = b''
        while True:
            try:
                part = t.read_some()
            except socket.timeout:
                break
            data += part
            #if b'#' in part:
            #    break
        print(data.decode('utf-8'))


