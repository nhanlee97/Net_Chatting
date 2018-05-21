#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~SERVER FOR NET CHATTING~~~~~~~~~~~~~~
#   1. Get Public IP
#   2. Socket TCP/IP
#   3. Connect Database Function
#   4. Handle Client Thread
#   5. Wait incoming connection and Login (Main)
#   6. After Login okay, Handle command from client!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import socket
import threading
import sqlite3


#Get Public IP~~~
from requests import get
ip = str(get('https://api.ipify.org').text)
print("My public IP address is:")
print(ip)
port = 5558



#Socket TCP/IP~~~
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
s.bind(('', port))
s.listen()
print('Server Ready...')
print('Ip Address of the Server::%s'%ip)
print('Server Port: %s'%port)
print('---------------Listening! Imcoming connection-----------------')



#Global variable~~~
listusr=['brian']
clients = {}



#Function to connect SQLite3 Database:~~~~
def db():
    global c
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
    c.execute('create table if not exists users(username TEXT NOT NULL,password TEXT NOT NULL)')
    db.commit()
    c.close()
    db.close()



#Thread for Handling Client:~~~~
def handleClient(client, uname):
    clientConnected = True
    keys = clients.keys()
    help = 'There are four commands in Messenger\n1::  **chatlist: gives you the list of the people currently online\n2::  **quit: To end your session\n3::   **sendall: To broadcast your message to each and every person currently present online\n4::   **[name]: To chat with specified person!'

    while clientConnected:
        try:
            msg = client.recv(1024).decode('ascii')
            response = 'Number of People Online\n'
            found = False
            if '**chatlist' in msg:
                clientNo = 0
                for name in keys:
                    clientNo += 1
                    response = response + str(clientNo) +'::' + name+'\n'
                client.send(response.encode('ascii'))
            elif '**help' in msg:
                client.send(help.encode('ascii'))
            elif '**sendall' in msg:
                
                msg = msg.replace('**sendall','')
                for k,v in clients.items():
                    v.send(msg.encode('ascii'))

            elif '**quit' in msg:
                response = 'Stopping Session and exiting...'
                client.send(response.encode('ascii'))
                clients.pop(uname)
                print(uname + ' has been logged out')
                clientConnected = False
            else:
                for name in keys:
                    if('**'+name) in msg:
                        msg = msg.replace('**'+name, '')
                        clients.get(name).send(msg.encode('ascii'))
                        found = True
                if(not found):
                    client.send('Trying to send message to invalid person.'.encode('ascii'))
        except:
            clients.pop(uname)
            print(uname + ' has been logged out')
            clientConnected = False


        
#Main Part!~~~~
while serverRunning:
    global c

    #accept incoming connect from client
    client, address = s.accept()
    print("Client address:") 
    print(address)
    print("--------------------------------")
    

    #Login first
    OK = True
    while OK:
        
        #wait for login/create information from client
        uname = client.recv(1024).decode('ascii')
        userrecv = uname.splitlines()
        print(uname)
        #login information
        if userrecv[0] == 'login' :
            datauser=1
            for index in range(len(listusr)):
                if listusr[index] == uname:
                    datauser=1
                else:
                    datauser=0  
            
            if datauser == 0:
                userrecv = uname.splitlines()
                username = userrecv[1]
                password = userrecv[2]
                #connect database to check whether 'login' information is correct?
                with sqlite3.connect('users.db') as db:
                    c = db.cursor()
                c.execute('SELECT * FROM users WHERE username = ? and password = ?',(username,password))
                data = c.fetchone()
                db.commit()
                
                if data != None:
                    listusr.append(username)
                    client.send('Welcome'.encode('ascii'))
                    print('%s connected to the server'%str(username))
                    client.send('Welcome to Messenger. Type **help to know all the commands'.encode('ascii'))

                    #Connect Okay! Create Thread for handling client
                    if(client not in clients):
                        clients[username] = client
                        threading.Thread(target = handleClient, args = (client, username, )).start()
                        OK= False
                else:
                    client.send('Error'.encode('ascii'))

        #create information            
        if userrecv[0] == 'create' :
            name = userrecv[1]
            age = userrecv[2]
            username = userrecv[3]
            password = userrecv[4]
            gender = userrecv[5]

    
            with sqlite3.connect('users.db') as db:
                c = db.cursor()
            c.execute('SELECT * FROM users WHERE username = ?',[username])
            data = c.fetchone()
            db.commit()
            if data != None:


                print("username has already been taken ")
                client.send('username has already been taken, Try again ! '.encode('ascii'))


            else:

                with sqlite3.connect('users.db') as db:
                    c = db.cursor()
                c.execute('INSERT INTO users VALUES(?,?,?,?,?)',(name,age,username,password,gender))
                db.commit()
                c.execute('SELECT * FROM users')
                db.commit()
                c.close()
                db.close()
                print ("Sucessfull")

            
                





    