import os

os.system('cls')

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel

from PyQt5.QtWidgets import QDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sudoku 15')

        self.h_box0 = QHBoxLayout()

        self.h_box1 = QHBoxLayout()
        
        self.h_box2 = QHBoxLayout()

        self.h_box3 = QHBoxLayout()

        self.h_box4 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.count = 0

        self.counter  = QLabel(str(self.count))

        self.label = QLabel('')        

        self.label.setStyleSheet('font-weight:bold;  ')

        self.label.setFixedSize(40, 40)

        self.btn_1 = QPushButton(self)
        self.btn_1.setFixedSize(70, 70)
        self.btn_1.setText('4')
        # self.btn_1.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")
        self.btn_1.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")

        self.btn_2 = QPushButton(self)
        self.btn_2.setFixedSize(70, 70)
        self.btn_2.setText('12')
        self.btn_2.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_2.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")
        

        self.btn_3 = QPushButton(self)
        self.btn_3.setFixedSize(70, 70)
        self.btn_3.setText('7')
        self.btn_3.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_3.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        
        self.btn_4 = QPushButton(self)
        self.btn_4.setFixedSize(70, 70)
        self.btn_4.setText('11')
        self.btn_4.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_4.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")


        self.btn_5 = QPushButton(self)
        self.btn_5.setFixedSize(70, 70)
        self.btn_5.setText('')
        self.btn_5.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_5.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

    
        self.btn_6 = QPushButton(self)
        self.btn_6.setFixedSize(70, 70)
        self.btn_6.setText('3')
        self.btn_6.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_6.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_7 = QPushButton(self)
        self.btn_7.setFixedSize(70, 70)
        self.btn_7.setText('8')
        self.btn_7.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_7.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_8 = QPushButton(self)
        self.btn_8.setFixedSize(70, 70)
        self.btn_8.setText('13')
        self.btn_8.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_8.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")
        
        self.btn_9 = QPushButton(self)
        self.btn_9.setFixedSize(70, 70)
        self.btn_9.setText('2')
        self.btn_9.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_9.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_10 = QPushButton(self)
        self.btn_10.setFixedSize(70, 70)
        self.btn_10.setText('5')
        self.btn_10.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_10.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_11 = QPushButton(self)
        self.btn_11.setFixedSize(70, 70)
        self.btn_11.setText('15')
        self.btn_11.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_11.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_12 = QPushButton(self)
        self.btn_12.setFixedSize(70, 70)
        self.btn_12.setText('10')
        self.btn_12.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_12.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_13 = QPushButton(self)
        self.btn_13.setFixedSize(70, 70)
        self.btn_13.setText('1')
        self.btn_13.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_13.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_14 = QPushButton(self)
        self.btn_14.setFixedSize(70, 70)
        self.btn_14.setText('6')
        self.btn_14.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_14.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_15 = QPushButton(self)
        self.btn_15.setFixedSize(70, 70)
        self.btn_15.setText('9')
        self.btn_15.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_15.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")

        self.btn_16 = QPushButton(self)
        self.btn_16.setFixedSize(70, 70)
        self.btn_16.setText('14')
        self.btn_16.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        # self.btn_16.setStyleSheet('QPushButton::hover'"{""background-color :#7FFFD4" "}")


        self.h_box0.addWidget(self.label)

        self.h_box0.addWidget(self.counter)

        self.h_box1.addWidget(self.btn_1)
        
        self.h_box1.addWidget(self.btn_2)
        
        self.h_box1.addWidget(self.btn_3)
        
        self.h_box1.addWidget(self.btn_4)
        
        self.h_box2.addWidget(self.btn_5)
        
        self.h_box2.addWidget(self.btn_6)
        
        self.h_box2.addWidget(self.btn_7)
        
        self.h_box2.addWidget(self.btn_8)
        
        self.h_box3.addWidget(self.btn_9)
        
        self.h_box3.addWidget(self.btn_10)
        
        self.h_box3.addWidget(self.btn_11)
        
        self.h_box3.addWidget(self.btn_12)
        
        self.h_box4.addWidget(self.btn_13)
        
        self.h_box4.addWidget(self.btn_14)
        
        self.h_box4.addWidget(self.btn_15)

        self.h_box4.addWidget(self.btn_16)


        self.v_box.addLayout(self.h_box0)

        self.v_box.addLayout(self.h_box1)

        self.v_box.addLayout(self.h_box2)

        self.v_box.addLayout(self.h_box3)

        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

        self.show()

        self.btn_1.clicked.connect(self.press_btn1)
        # self.btn_1.clicked.connect(self.check_color1)

        self.btn_2.clicked.connect(self.press_btn2)
        # self.btn_2.clicked.connect(self.check_color2)

        self.btn_3.clicked.connect(self.press_btn3)
        # self.btn_3.clicked.connect(self.check_color3)

        self.btn_4.clicked.connect(self.press_btn4)
        # self.btn_4.clicked.connect(self.check_color4)

        self.btn_5.clicked.connect(self.press_btn5)
        # self.btn_5.clicked.connect(self.check_color5)

        self.btn_6.clicked.connect(self.press_btn6)
        # self.btn_6.clicked.connect(self.check_color6)

        self.btn_7.clicked.connect(self.press_btn7)
        # self.btn_7.clicked.connect(self.check_color7)

        self.btn_8.clicked.connect(self.press_btn8)
        # self.btn_8.clicked.connect(self.check_color8)

        self.btn_9.clicked.connect(self.press_btn9)
        # self.btn_9.clicked.connect(self.check_color9)

        self.btn_10.clicked.connect(self.press_btn10)
        # self.btn_10.clicked.connect(self.check_color10)

        self.btn_11.clicked.connect(self.press_btn11)
        # self.btn_11.clicked.connect(self.check_color11)

        self.btn_12.clicked.connect(self.press_btn12)
        # self.btn_12.clicked.connect(self.check_color12)

        self.btn_13.clicked.connect(self.press_btn13)
        # self.btn_13.clicked.connect(self.check_color13)

        self.btn_14.clicked.connect(self.press_btn14)
        # self.btn_14.clicked.connect(self.check_color14)

        self.btn_15.clicked.connect(self.press_btn15)
        # self.btn_15.clicked.connect(self.check_color15)

        self.btn_16.clicked.connect(self.press_btn16)

        # self.btn_16.clicked.connect(self.check_color16)
        self.btn_16.clicked.connect(self.check)
        self.btn_15.clicked.connect(self.check)
        self.btn_14.clicked.connect(self.check)
        self.btn_13.clicked.connect(self.check)
        self.btn_12.clicked.connect(self.check)
        self.btn_11.clicked.connect(self.check)

        # if self.btn_1.text() == 1:
            # self.btn_1.setStyleSheet("background-color : red; color : black; font-weight: bold")


    def press_btn1(self):
        if self.btn_2.text() == '':
            self.btn_2.setText(self.btn_1.text())
            self.btn_1.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_5.text() == '':
            self.btn_5.setText(self.btn_1.text())
            self.btn_1.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_1.text() != '1':
            self.btn_1.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        
        if self.btn_2.text() == '2':
            self.btn_2.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_5.text() == '5':
            self.btn_5.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn2(self):
        if self.btn_1.text() == '':
            self.btn_1.setText(self.btn_2.text())
            self.btn_2.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_3.text() == '':
            self.btn_3.setText(self.btn_2.text())
            self.btn_2.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_6.text() == '':
            self.btn_6.setText(self.btn_2.text())
            self.btn_2.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_2.text() != '2':
            self.btn_2.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
                
        if self.btn_1.text() == '1':
            self.btn_1.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_3.text() == '3':
            self.btn_3.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_6.text() == '6':
            self.btn_6.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")


    def press_btn3(self):
        if self.btn_2.text() == '':
            self.btn_2.setText(self.btn_3.text())
            self.btn_3.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_4.text() == '':
            self.btn_4.setText(self.btn_3.text())
            self.btn_3.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_7.text() == '':
            self.btn_7.setText(self.btn_3.text())
            self.btn_3.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_3.text() != '3':
            self.btn_3.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_2.text() == '2':
            self.btn_2.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_4.text() == '4':
            self.btn_4.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_7.text() == '7':
            self.btn_7.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn4(self):
        if self.btn_3.text() == '':
            self.btn_3.setText(self.btn_4.text())
            self.btn_4.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_8.text() == '':
            self.btn_8.setText(self.btn_4.text())
            self.btn_4.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_4.text() != '4':
            self.btn_4.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_3.text() == '3':
            self.btn_3.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_8.text() == '8':
            self.btn_8.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")


    def press_btn5(self):
        if self.btn_1.text() == '':
            self.btn_1.setText(self.btn_5.text())
            self.btn_5.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_6.text() == '':
            self.btn_6.setText(self.btn_5.text())
            self.btn_5.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_9.text() == '':
            self.btn_9.setText(self.btn_5.text())
            self.btn_5.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_5.text() != '5':
            self.btn_5.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        
        if self.btn_1.text() == '1':
            self.btn_1.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_6.text() == '6':
            self.btn_6.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_9.text() == '9':
            self.btn_9.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        
    def press_btn6(self):
        if self.btn_2.text() == '':
            self.btn_2.setText(self.btn_6.text())
            self.btn_6.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_5.text() == '':
            self.btn_5.setText(self.btn_6.text())
            self.btn_6.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_7.text() == '':
            self.btn_7.setText(self.btn_6.text())
            self.btn_6.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_10.text() == '':
            self.btn_10.setText(self.btn_6.text())
            self.btn_6.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_6.text() != '6':
            self.btn_6.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_2.text() == '2':
            self.btn_2.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_5.text() == '5':
            self.btn_5.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_7.text() == '7':
            self.btn_7.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_10.text() == '10':
            self.btn_10.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn7(self):
        if self.btn_3.text() == '':
            self.btn_3.setText(self.btn_7.text())
            self.btn_7.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_6.text() == '':
            self.btn_6.setText(self.btn_7.text())
            self.btn_7.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_8.text() == '':
            self.btn_8.setText(self.btn_7.text())
            self.btn_7.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_11.text() == '':
            self.btn_11.setText(self.btn_7.text())
            self.btn_7.setText('')  
            self.count+=1 
            self.label.setText(str(self.count))
        if self.btn_7.text() != '7':
            self.btn_7.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_3.text() == '3':
            self.btn_3.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_6.text() == '6':
            self.btn_6.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_8.text() == '8':
            self.btn_8.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_11.text() == '11':
            self.btn_11.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn8(self):
        if self.btn_4.text() == '':
            self.btn_4.setText(self.btn_8.text())
            self.btn_8.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_7.text() == '':
            self.btn_7.setText(self.btn_8.text())
            self.btn_8.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_12.text() == '':
            self.btn_12.setText(self.btn_8.text())
            self.btn_8.setText('') 
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_8.text() != '8':
            self.btn_8.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_4.text() == '4':
            self.btn_4.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_7.text() == '7':
            self.btn_7.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_12.text() == '12':
            self.btn_12.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold") 

    def press_btn9(self):
        if self.btn_5.text() == '':
            self.btn_5.setText(self.btn_9.text())
            self.btn_9.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_10.text() == '':
            self.btn_10.setText(self.btn_9.text())
            self.btn_9.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_13.text() == '':
            self.btn_13.setText(self.btn_9.text())
            self.btn_9.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_9.text() != '9':
            self.btn_9.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")    
        if self.btn_5.text() == '5':
            self.btn_5.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_10.text() == '10':
            self.btn_10.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_13.text() == '13':
            self.btn_13.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn10(self):
        if self.btn_6.text() == '':
            self.btn_6.setText(self.btn_10.text())
            self.btn_10.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_9.text() == '':
            self.btn_9.setText(self.btn_10.text())
            self.btn_10.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_11.text() == '':
            self.btn_11.setText(self.btn_10.text())
            self.btn_10.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_14.text() == '':
            self.btn_14.setText(self.btn_10.text())
            self.btn_10.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_10.text() != '10':
            self.btn_10.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_6.text() == '6':
            self.btn_6.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_9.text() == '9':
            self.btn_9.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_11.text() == '11':
            self.btn_11.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_14.text() == '14':
            self.btn_14.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn11(self):
        if self.btn_7.text() == '':
            self.btn_7.setText(self.btn_11.text())
            self.btn_11.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_10.text() == '':
            self.btn_10.setText(self.btn_11.text())
            self.btn_11.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_12.text() == '':
            self.btn_12.setText(self.btn_11.text())
            self.btn_11.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_15.text() == '':
            self.btn_15.setText(self.btn_11.text())
            self.btn_11.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_11.text() != '11':
            self.btn_11.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_7.text() == '7':
            self.btn_7.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_10.text() == '10':
            self.btn_10.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_12.text() == '12':
            self.btn_12.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_15.text() == '15':
            self.btn_15.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn12(self):
        if self.btn_8.text() == '':
            self.btn_8.setText(self.btn_12.text())
            self.btn_12.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_11.text() == '':
            self.btn_11.setText(self.btn_12.text())
            self.btn_12.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_16.text() == '':
            self.btn_16.setText(self.btn_12.text())
            self.btn_12.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_12.text() != '12':
            self.btn_12.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_8.text() == '8':
            self.btn_8.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_11.text() == '11':
            self.btn_11.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn13(self):
        if self.btn_9.text() == '':
            self.btn_9.setText(self.btn_13.text())
            self.btn_13.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_14.text() == '':
            self.btn_14.setText(self.btn_13.text())
            self.btn_13.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_13.text() != '13':
            self.btn_13.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_9.text() == '9':
            self.btn_9.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_14.text() == '14':
            self.btn_14.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn14(self):
        if self.btn_10.text() == '':
            self.btn_10.setText(self.btn_14.text())
            self.btn_14.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_13.text() == '':
            self.btn_13.setText(self.btn_14.text())
            self.btn_14.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_15.text() == '':
            self.btn_15.setText(self.btn_14.text())
            self.btn_14.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_14.text() != '14':
            self.btn_14.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_10.text() == '10':
            self.btn_10.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_13.text() == '13':
            self.btn_13.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_15.text() == '15':
            self.btn_15.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn15(self):
        if self.btn_11.text() == '':
            self.btn_11.setText(self.btn_15.text())
            self.btn_15.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_14.text() == '':
            self.btn_14.setText(self.btn_15.text())
            self.btn_15.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_16.text() == '':
            self.btn_16.setText(self.btn_15.text())
            self.btn_15.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_15.text() != '15':
            self.btn_15.setStyleSheet("background-color : 	#7FFFD4; color : black; font-weight: bold")
        if self.btn_11.text() == '11':
            self.btn_11.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_14.text() == '14':
            self.btn_14.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def press_btn16(self):
        if self.btn_12.text() == '':
            self.btn_12.setText(self.btn_16.text())
            self.btn_16.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        elif self.btn_15.text() == '':
            self.btn_15.setText(self.btn_16.text())
            self.btn_16.setText('')
            self.count+=1
            self.label.setText(str(self.count))
        if self.btn_12.text() == '12':
            self.btn_12.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")
        if self.btn_15.text() == '15':
            self.btn_15.setStyleSheet("background-color :	#FF9912; color : black; font-weight: bold")

    def check(self):
        if self.btn_1.text() == '1' and self.btn_2.text() == '2' and self.btn_3.text() == '3' and self.btn_4.text() == '4' and self.btn_5.text() == '5' and self.btn_6.text() == '6' and self.btn_7.text() == '7' and self.btn_8.text() == '8' and self.btn_9.text() == '9' and self.btn_10.text() == '10' and self.btn_11.text() == '11' and self.btn_12.text() == '12' and self.btn_13.text() == '13' and self.btn_14.text() == '14' and self.btn_15.text() == '15' :
            win.close()
    
# class CustomDialog(QDialog):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Winner!')

#         self.qbtn = QDialogButtonBox.Cancel

#         self.buttonBox = QDialogButtonBox(self.qbtn)

#         self.buttonBox.accepted
        
  
        
app = QApplication(sys.argv)

win = MainWindow()

sys.exit(app.exec_())
