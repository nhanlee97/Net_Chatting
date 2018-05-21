
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~GUI for Chatbox~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~



from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys
import threading


#Global variable~~~~~~~
global Chattext 
Chattext = 'Default Context'
global ConditionChat
ConditionChat = False
global ReceiveMsgg
ReceiveMsgg = 'Default Context'
global Line 
Line = 1
global ReceiveCondition
ReceiveCondition = 0
#~~~~~~



class Ui_Chatbox(object):
    def setupUi(self, Chatbox):
        Chatbox.setObjectName("Chatbox")
        Chatbox.resize(400, 700)
        Chatbox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.friendlist = QtWidgets.QWidget()
        self.friendlist.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.friendlist.setObjectName("friendlist")
        self.tableView = QtWidgets.QTableView(self.friendlist)
        self.tableView.setGeometry(QtCore.QRect(15, 20, 371, 491))
        self.tableView.setObjectName("tableView")
        self.pushButton_2 = QtWidgets.QPushButton(self.friendlist)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 530, 201, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        Chatbox.addTab(self.friendlist, "")
        self.Chat = QtWidgets.QWidget()
        self.Chat.setObjectName("Chat")
        self.pushButton = QtWidgets.QPushButton(self.Chat)
        self.pushButton.setGeometry(QtCore.QRect(110, 550, 171, 41))
        self.pushButton.setObjectName("pushButton")

        #AAAAA Xem lai cho nay
        
        self.pushButton.clicked.connect(self.Chatbegin)

        self.toolButton = QtWidgets.QToolButton(self.Chat)
        self.toolButton.setGeometry(QtCore.QRect(280, 630, 81, 25))
        self.toolButton.setObjectName("toolButton")

        self.toolButton.clicked.connect(self.QuitProgram)

        self.lineEdit = QtWidgets.QLineEdit(self.Chat)
        self.lineEdit.setGeometry(QtCore.QRect(10, 480, 371, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.Chat)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 371, 461))
        self.textBrowser.setObjectName("textBrowser")

        
        #timer
        self.timer = QtCore.QTimer(self.Chat)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(100)
        
        Chatbox.addTab(self.Chat, "")

        self.retranslateUi(Chatbox)
        Chatbox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Chatbox)

    def retranslateUi(self, Chatbox):
        _translate = QtCore.QCoreApplication.translate
        Chatbox.setWindowTitle(_translate("Chatbox", "Chat"))
        Chatbox.setWhatsThis(_translate("Chatbox", "<html><head/><body><p>Friends List </p></body></html>"))
        self.pushButton_2.setText(_translate("Chatbox", "Load "))
        Chatbox.setTabText(Chatbox.indexOf(self.friendlist), _translate("Chatbox", "Friends List"))
        self.pushButton.setText(_translate("Chatbox", "Send"))
        self.toolButton.setText(_translate("Chatbox", "Quit"))
        Chatbox.setTabText(Chatbox.indexOf(self.Chat), _translate("Chatbox", "Chat Box"))

        

    #After self.timer.start(100) 100ms, update textBrowser 1 time!
    def timerEvent(self):   
        global ReceiveCondition
        if ReceiveCondition:
            ReceiveCondition = 0
            self.textBrowser.append(ReceiveMsgg)
            self.textBrowser.append('====================================')


    #When "send" button clicked!
    def Chatbegin(self):    
        global Chattext
        global ConditionChat
        global Line


        Chattext = str(self.lineEdit.text())
        self.lineEdit.setText('')
        self.textBrowser.append('Me>>    ' + Chattext + '\n')
        ConditionChat = True
       



    #Quit
    def QuitProgram(self):   
        sys.exit()

    
    