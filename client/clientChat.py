#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~CLIENT FOR CHATTING~~~~~~~~~~~~~~
# 1. Include Library for GUI
# 2. Initialise GUI
# 3. Draw GUI
# 4. Connect to server
# 5. Login
# 6. After login okay, Open GUI Chatbox!
# 7. Receive and Send message, command!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#Include Library
import socket
import threading
import sqlite3

#Library for GUI
from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Chat import Ui_Chatbox
import Chat #from file Chat.py

import time
import sys


#Global variable
global loginpass
loginpass = False


#Create/Initialise GUI~~~~~~~~
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)



#def db():
#    with sqlite3.connect('users.db') as db:
#        c = db.cursor()
#    c.execute('create table if not exists users(name TEXT NOT NULL,age INT NOT NULL,username TEXT NOT NULL,password TEXT NOT NULL, gender TEXT NOT NULL)')
#    db.commit()
#    c.close()
#    db.close()


#Draw GUI~~~~~~~~~~~~~~~~~
class Ui_win(object):
    def setupUi(self, win):
        win.setObjectName(_fromUtf8("win"))
        win.resize(622, 512)
        win.setMinimumSize(QtCore.QSize(622, 512))
        win.setMaximumSize(QtCore.QSize(622, 512))
        self.label = QtWidgets.QLabel(win)
        self.label.setGeometry(QtCore.QRect(210, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans CJK SC"))
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtWidgets.QTabWidget(win)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 621, 431))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.accTab = QtWidgets.QWidget()
        self.accTab.setObjectName(_fromUtf8("accTab"))
        self.label_2 = QtWidgets.QLabel(self.accTab)
        self.label_2.setGeometry(QtCore.QRect(180, 0, 271, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans CJK SC"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.firstname = QtWidgets.QLineEdit(self.accTab)
        self.firstname.setGeometry(QtCore.QRect(100, 70, 201, 41))
        self.firstname.setObjectName(_fromUtf8("firstname"))
        self.lastname = QtWidgets.QLineEdit(self.accTab)
        self.lastname.setGeometry(QtCore.QRect(320, 70, 191, 41))
        self.lastname.setObjectName(_fromUtf8("lastname"))
        self.cr_username = QtWidgets.QLineEdit(self.accTab)
        self.cr_username.setGeometry(QtCore.QRect(100, 130, 351, 41))
        self.cr_username.setObjectName(_fromUtf8("cr_username"))
        self.cr_password = QtWidgets.QLineEdit(self.accTab)
        self.cr_password.setGeometry(QtCore.QRect(100, 180, 351, 41))
        #----------------------------
        self.cr_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cr_password.setText(_fromUtf8(""))
        self.cr_password.setObjectName(_fromUtf8("cr_password"))
        self.cr_age = QtWidgets.QLineEdit(self.accTab)
        self.cr_age.setGeometry(QtCore.QRect(100, 240, 101, 31))
        self.cr_age.setMaxLength(2)
        self.cr_age.setObjectName(_fromUtf8("cr_age"))
        self.male_radio = QtWidgets.QRadioButton(self.accTab)
        self.male_radio.setGeometry(QtCore.QRect(310, 240, 115, 31))
        self.male_radio.setObjectName(_fromUtf8("male_radio"))
        self.female_radio = QtWidgets.QRadioButton(self.accTab)
        self.female_radio.setGeometry(QtCore.QRect(410, 240, 115, 31))
        self.female_radio.setObjectName(_fromUtf8("female_radio"))
        self.label_4 = QtWidgets.QLabel(self.accTab)
        self.label_4.setGeometry(QtCore.QRect(220, 240, 81, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.createAccount = QtWidgets.QPushButton(self.accTab)
        self.createAccount.setGeometry(QtCore.QRect(100, 300, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.createAccount.setFont(font)
        self.createAccount.setObjectName(_fromUtf8("createAccount"))
        self.cr_clear = QtWidgets.QPushButton(self.accTab)
        self.cr_clear.setGeometry(QtCore.QRect(350, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.cr_clear.setFont(font)
        self.cr_clear.setObjectName(_fromUtf8("cr_clear"))
        self.tabWidget.addTab(self.accTab, _fromUtf8(""))
        self.log = QtWidgets.QWidget()
        self.log.setObjectName(_fromUtf8("log"))
        self.label_3 = QtWidgets.QLabel(self.log)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 301, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans CJK SC"))
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.log_username = QtWidgets.QLineEdit(self.log)
        self.log_username.setGeometry(QtCore.QRect(110, 90, 401, 51))
        self.log_username.setObjectName(_fromUtf8("log_username"))
        self.log_password = QtWidgets.QLineEdit(self.log)
        self.log_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_password.setGeometry(QtCore.QRect(110, 170, 401, 51))
        self.log_password.setObjectName(_fromUtf8("log_password"))
        self.log_in = QtWidgets.QPushButton(self.log)
        self.log_in.setGeometry(QtCore.QRect(110, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.log_in.setFont(font)
        self.log_in.setObjectName(_fromUtf8("log_in"))
        self.log_clear = QtWidgets.QPushButton(self.log)
        self.log_clear.setGeometry(QtCore.QRect(320, 250, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.log_clear.setFont(font)
        self.log_clear.setObjectName(_fromUtf8("log_clear"))
        self.tabWidget.addTab(self.log, _fromUtf8(""))

        self.retranslateUi(win)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        win.setWindowTitle(_translate("win", "Login Form", None))
        self.label.setText(_translate("win", "LOGIN FORM", None))
        self.label_2.setText(_translate("win", "Create Account ", None))
        self.firstname.setPlaceholderText(_translate("win", "First Name", None))
        self.lastname.setPlaceholderText(_translate("win", "Last Name", None))
        self.cr_username.setPlaceholderText(_translate("win", "Type a username...", None))
        self.cr_password.setPlaceholderText(_translate("win", "Type a password...", None))
        self.cr_age.setPlaceholderText(_translate("win", "Age....", None))
        self.male_radio.setText(_translate("win", "Male", None))
        self.female_radio.setText(_translate("win", "Female", None))
        self.label_4.setText(_translate("win", "Gender: ", None))
        self.createAccount.setText(_translate("win", "Create Account", None))
        self.cr_clear.setText(_translate("win", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accTab), _translate("win", "Create Account", None))
        self.label_3.setText(_translate("win", "Log In", None))
        self.log_username.setPlaceholderText(_translate("win", "Type username here ....", None))
        self.log_password.setPlaceholderText(_translate("win", "Type password here ....", None))
        self.log_in.setText(_translate("win", "Log In", None))
        self.log_clear.setText(_translate("win", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("win", "Log In", None))
        self.cr_clear.clicked.connect(self.clear1)
        self.log_clear.clicked.connect(self.clear2)
        self.createAccount.clicked.connect(self.create_account)
        self.log_in.clicked.connect(self.login)

    def clear1(self):
        self.firstname.setText('')
        self.lastname.setText('')
        self.cr_username.setText('')
        self.cr_password.setText('')
        self.cr_age.setText('')

    def clear2(self):
        self.log_username.setText('')
        self.log_password.setText('')



    #Function for login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def login(self):
        global loginpass
        loginpass = False
        global uname
        global username

        global Sendcondition
        Sendcondition = 0
        global ack #receive msg
        ack = 0 #sai

        
        #get username, password from GUI
        username = str(self.log_username.text())
        password = str(self.log_password.text())
        uname = 'login' + '\n' + username + '\n' + password
        time.sleep(1)
        Sendcondition = 1
        

        #timeout: If wait too long!
        timeout = 0
        while ack == 0:
            timeout = timeout + 1
            time.sleep(1)
            if timeout == 5:
                break

        #Login succeed!
        if ack == 1:
            loginpass = True
            self.widget = QtWidgets.QTabWidget()
            self.ui = Ui_Chatbox()
            self.ui.setupUi(self.widget)
            win.hide()
            self.widget.show()
        else:
            QMessageBox.critical(win,"Error", 'No Account With That Username And Password')



    #Function for creating account!~~~~~~~~~~~~~~~
    def create_account(self):
        global uname
        global Sendcondition
        Sendcondition = 0

        gender = None
        name = str(self.firstname.text()+' '+self.lastname.text())
        age = int(self.cr_age.text())
        username = str(self.cr_username.text())
        password = str(self.cr_password.text())

        if self.male_radio.isChecked():
            gender = 'Male'
        if self.female_radio.isChecked():
            gender = 'Female'

        #send CREATE FRAME to server
        uname = 'create' + '\n' + name + '\n' + str(age) + '\n' + username + '\n' + password + '\n' + gender
        Sendcondition = 1
        QMessageBox.information(win,"Success!!", 'Account Created Successfully.')
        self.clear1()
            

    


#Ket noi Server~~~~~~
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input('Enter the Server Address:: ')
port = input('Enter PORT:: ')
s.connect((ip, int(port)))




#Receive Message Thread!~~~~~~~~~~
def receiveMsg(sock):
    #var: global Chat.ReceiveMsgg
    #login
    global loginpass
    global ack
    global username



    print("receive Message is ready!")
    global condit
    condit = 0
    serverDown = True
    while serverDown:
        try:
            if (loginpass == False):
                data = sock.recv(1024).decode('ascii')
                print(data)
                if 'Welcome' in data:
                    ack = 1
                    loginpass = True
                    time.sleep(1)
                    Chat.ReceiveMsgg = data
                    Chat.ReceiveCondition = 1
            else:
                msg = sock.recv(1024).decode('ascii')
                print("Recieve chat")
                Chat.ReceiveMsgg = msg
                Chat.ReceiveCondition = 1
                print(Chat.ReceiveMsgg)

        except:
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = False
        

#Send Message Thread!~~~~~~~        
def sendMsg(sock):

    #Login Part
    print("Login first!")
    global loginpass

    global uname  #uname = 'login' + '\n' + username + '\n' + password
    global username

    global Sendcondition
    Sendcondition = 0

    #login first
    while loginpass == False:
        if Sendcondition == 1:
            print("send username + password to server")
            print(uname)
            sock.send(uname.encode('ascii'))
            Sendcondition = 0
        
    print("======================Login Successfully!======================\n")

    #SendMsg
    #chat box   Chat.Chattext, Chat.ConditionChat
    clientRunning = True
    print("Send Message is ready!")

    while clientRunning:    
        
        if Chat.ConditionChat:
            msg = username + '>>' + Chat.Chattext
            Chat.ConditionChat = False
            if '**quit' in msg:
                clientRunning = False
                sock.send('**quit'.encode('ascii'))
            else:
                sock.send(msg.encode('ascii'))







#Create Receive and Send Thread!
threading.Thread(target = receiveMsg, args = (s,)).start()
threading.Thread(target = sendMsg, args = (s,)).start()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()
    timer = QtCore.QTimer()
    ui = Ui_win()
    ui.setupUi(win)
    win.show()
    #db()
    sys.exit(app.exec_())

