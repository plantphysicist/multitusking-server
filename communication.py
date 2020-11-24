# sockets module for sockets duh
import socket

# for use later, msg buffer so packets will be handled one by one
import queue

# config file changes from enviorment to enviorment
import config

# bit to data stracture conversion
import pickle

DEFAULT_MSG_LENGTH = 1024

class Handler:
    """
    for shared funcions
    """

    def send_only_msg(self, msg):
        """
        just translate msg to byteArray and send it
        """
        
        byte_msg = pickle.dumps(msg)

        self.sock.send(byte_msg)


    def recv_only_msg(self, size = DEFAULT_MSG_LENGTH) -> object:
        """
        just recv the msg and decode it
        """
        
        msg = self.sock.recv(size)

        return pickle.loads(msg)

    
    def send(self, msg):
        """
        send msg size (with default size length)
        |
        \/
        ack
        |
        \/
        send msg
        """

        # send length
        send_only_msg(len(pickle.dumps(msg)))

        # wait for confirmation
        if (recv_only_msg() == 'ack'):

            # send msg
            send_only_msg(msg)

        # if didn't recv ack for some reason
        else:
            raise ConnectionRefusedError


    def recv(self) -> object:
        """
        other side to the send func (recv size -> send ack -> recv msg)
        """

        # recv length
        size = recv_only_msg()

        # send ack
        send_only_msg('ack')

        # recv and return msg
        return recv_only_msg(size)

class Server(Handler):
    """
    class for the server side of things
    """

    def __init__(self):

        # create the socket on in self and bind it to what's
        # configured in the config file
        self.sock = socket.socket()
        self.sock.bind((config.IP, config.PORT))
        self.sock.listen(1)
        

class Client(Handler):
    """
    class for the client side of things
    """

    def __init__(self):
        
        # create socket and connect to the info configured
        # in the config file
        self.sock = socket.socket()
        self.sock.connect((config.IP, config.PORT))