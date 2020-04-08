import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
 
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def RedLED():
        GPIO.output(10, GPIO.HIGH)
        
        GPIO.output(8, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)

def GreenLED():
        GPIO.output(8, GPIO.HIGH)

        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)  
def BlueLED():
        GPIO.output(12, GPIO.HIGH)

        GPIO.output(8, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        
def Quit():
        GPIO.output(10, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        win.destroy()
        GPIO.cleanup()
        
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,500,500)
    win.setWindowTitle("LED Application")
    
    label = QtWidgets.QLabel(win)
    label.setText("LED Toggle")
    label.move(0,0)
    
    redb = QtWidgets.QPushButton(win)
    redb.setText("Red LED")
    redb.move(0,50)
    redb.clicked.connect(RedLED) 
    
    greenb = QtWidgets.QPushButton(win)
    greenb.setText("Green LED")
    greenb.move(0,100)
    greenb.clicked.connect(GreenLED) 
    
    blueb = QtWidgets.QPushButton(win)
    blueb.setText("Blue LED")
    blueb.move(0,150)
    blueb.clicked.connect(BlueLED)
    
    quiT = QtWidgets.QPushButton(win)
    quiT.setText("QUIT")
    quiT.move(0,200)
    quiT.clicked.connect(Quit) 
    
    win.show()
    sys.exit(app.exec_())
    
window()
    
