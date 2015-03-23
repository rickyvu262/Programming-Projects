# Darpan Patel 35198867 Thanh Vu 17627579 Lab 4 ICS 32
import socket
import collections

#create a namedtuple for connection that takes 3 fields: socket, socket_input and socket_output
connect_connection = collections.namedtuple('connect_connection',['socket','socket_input','socket_output'])


def connectfour_conversation(echo_host:str,echo_port:int)->None:
    '''Makes a socket/ connects with host/makes 2 pseudo file and assigns a namedtuple to those'''
    connect_four_socket = socket.socket()
    connect_four_socket_input = None
    connect_four_socket_output = None

    print('Connecting to connect_four server...')
    connect_four_socket.connect((echo_host,echo_port))
    connect_four_socket_input = connect_four_socket.makefile('r')
    connect_four_socket_output = connect_four_socket.makefile('w')

    print('Connected successfully!')
    return connect_connection( socket = connect_four_socket, socket_input = connect_four_socket_input, socket_output = connect_four_socket_output)


def close(connection: connect_connection)->None:
    '''Closes the socket and the input and output psuedo file
'''
    print('Closing...')
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()
    print('Closed!')
    
    
def request_game(connection:connect_connection)->None:
    '''
Initiates the game
'''
    _connect_write(connection,'AI_GAME')

    _line_check(connection,'READY')


def send_valid_move(connection:connect_connection, user_move:str):
    ''' Sends the user move to the server while returning a move
'''
    _connect_write(connection,user_move)
    
    computer_move = []
    if _read_line(connection).strip()!= 'INVALID':#if its invalid need to specify what to do
        for message in range(2):
            computer_move.append(_read_line(connection))#We get back the computer counter move


    return computer_move[0]


   
def connect_login(connection:connect_connection, username : str):
    ''' Connects the user with a login username
'''
    _connect_write(connection,'I32CFSP_HELLO '+ username.strip())

    _line_check(connection,'WELCOME '+ username)


    
def _read_line(connection:connect_connection) -> str:
    '''Reads the input that the server sends without the end-of-line sequence
'''
    return connection.socket_input.readline()[:-1]


def _line_check(connection:connect_connection,line:str)->bool:
    '''Checks if the server sends anything at all
'''

    return _read_line(connection)== line
    
def _connect_write(connection:connect_connection,line:str)->None:
    '''Writes the output into a psuedo file
'''
    connection.socket_output.write(line +'\r\n')
    connection.socket_output.flush()



