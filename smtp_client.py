from socket import *
import ssl
import base64

# ------------ EDIT THESE LINES  ------------ #

email = "XXXX" # YOUR EMAIL HERE
email_bytes = b"XXXX" # YOUR EMAIL HERE
password = b"XXXX" # YOUR APP PASSWORD HERE
target_email = "XXXX" # TARGET EMAIL HERE

# ------------ EDIT THESE LINES  ------------ #


# reference 1: Extension for SMTP
# https://datatracker.ietf.org/doc/html/rfc3207 (section 5)

# reference 2: Python SSL module
# https://docs.python.org/3/library/ssl.html#functions-constants-and-exceptions

# reference 3: Yahoo SMTP Server authentication password guide
# https://mailtrap.io/blog/yahoo-smtp/

# reference 4: SMTP Auth
# https://mailtrap.io/blog/smtp-commands-and-responses/


# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = ("smtp.mail.yahoo.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

# Try to receive the response from the server
recv = clientSocket.recv(1024).decode() 
print(recv) 
if recv[:3] != '220': 
    print('220 reply not received from server.') 

# Send EHLO command and print server response.
# according to RFC 3207, we need to use EHLO for TLS
ehloCommand = 'EHLO Alice\r\n' 
clientSocket.send(ehloCommand.encode()) 
recv1 = clientSocket.recv(1024).decode() 
print(recv1) 
if recv1[:3] != '250': 
    print('250 reply not received from server.') 

# Send TLS command and print server response.
tlsCommand = 'STARTTLS\r\n'
clientSocket.send(tlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '220':
    print('220 reply not recevied from server.')

# Do the SSL wrapper to encrypt the socket for modern communication.
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver[0])
print('The socket has been wrapped in SSL.')

# Send AUTH command and print server response.
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '334':
    print('334 reply not recevied from server.')

# Send the base64 encoded email.
formatted_email = base64.b64encode(email_bytes)
clientSocket.send(formatted_email + b'\r\n')
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '334':
    print('334 reply not recevied from server.')

# Send the base64 encoded password.
formatted_password = base64.b64encode(password)
clientSocket.send(formatted_password + b'\r\n')
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '235':
    print('235 reply not recevied from server.')

# Send MAIL FROM command and print server response. 
mailfromCommand = f'MAIL FROM: <{email}>\r\n'
clientSocket.send(mailfromCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.') 

# Send RCPT TO command and print server response.
rcpttoCommand = f'RCPT TO: <{target_email}>\r\n'
clientSocket.send(rcpttoCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
    print('250 reply not received from server.') 

# Send DATA command and print server response. 
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '354':
    print('354 reply not received from server.')

# Compose the MESSAGE
fromHeader = f'From: {email}\r\n'
toHeader = f'To: {target_email}\r\n'
subjectHeader = 'Subject: This is a test email sent with my SMTP client!\r\n'
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n" # Message ends with a single period.
sendMessage = fromHeader + toHeader + subjectHeader + msg + endmsg

# Send MESSAGE and print server response.
clientSocket.send(sendMessage.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '250':
    print('250 reply not received from server.') 

# Send QUIT command and get server response. 
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv10 = clientSocket.recv(1024).decode()
print(recv10)
if recv10[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()
