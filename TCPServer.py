#BIANCA TOLEDO
# DUE 3/6/17
#SERVER SIDE OF APPLICATION
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) #CREATES CLIENT SOCKET USING THE FIRST PARAMETER INDICATING THE UNDERLYING NETWORK USING IPv4. SECOND PARAMETER INDICATES THAT THE SOCKET IS OF TYPE SOCK_STREAM(TCP)
serverSocket.bind(('',serverPort)) #ACTS AS THE WELCOMING DOOR
serverSocket.listen(1) #WAITS FOR CONNECTION REQUESTS FROM CLIENT (0 > 1)
print ('The server is ready to receive') #OUTPUT LINE
while 1:
connectionSocket, addr = serverSocket.accept() #ACCEPTS KNOCK AND CREATES NEW SOCKET
sentence = connectionSocket.recv(1024) #PLACES STRING IN modifiedSentence UNTIL RETURN CHARACTER
capitalizedSentence = sentence.upper() #CAPITALIZES SENTENCE
connectionSocket.send(capitalizedSentence) #SENDS CAPILIZED SENTENCE THRU CONNECTION SOCKET
connectionSocket.close() #CLOSES THE CONNECTION SOCKET