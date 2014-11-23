import logging.handlers
from logging.handlers import SocketHandler

class TcpLogger( logging.Logger ):
    """
    ctor
    """
    def __init__( self, name ):
        # Call parent class ctor
        super( TcpLogger, self ).__init__( name )
        self.socketHandler = None
    
    """
    dtor
    """
    def __del__( self ):
        self.disconnect()

    """
    Connect to a log server
    """
    def connect( self, serverName='localhost', serverPort=logging.handlers.DEFAULT_TCP_LOGGING_PORT ):
        # Close any existing connection
        self.disconnect()
        
        # Create a TCP handler
        socketHandler = logging.handlers.SocketHandler( serverName, serverPort )
        
        # Register this handler to the logger
        self.addHandler( socketHandler )
        
        # Optimize, otherwise every time we use 'self.' keyword, a lookup to instance's dictionary is done...
        self.socketHandler = socketHandler

    """
    Disconnect from log server
    """
    def disconnect( self ):
        if self.socketHandler != None:
            self.removeHandler( self.socketHandler )
            self.socketHandler = None