from PyQt5 import QtCore, QtGui, QtWidgets
import math

def recognize_n(n):
    counter = 0
    nums = []
    for i in range(1, n+1):
        if n % i == 0:
            nums.append(i)

    if len(nums) <= 2:
        return "prime", nums
    else:
        return "composite", nums


def prime_nums_under(n):
    nums_list= []
    count = 0
    for j in range(2, n+1):
        if all(j%i!=0 for i in range(2,int(math.sqrt(j))+1)):
            nums_list.append(str(j))
            count = count + 1
    return count, nums_list


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 730)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color:#c0c0c0\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_gif.setGeometry(QtCore.QRect(590, 10, 170, 170))
        self.movie = QtGui.QMovie("AAqY.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.label_gif.setScaledContents(True)
        self.label_gif.setObjectName("label_gif")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 130, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 290, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.spinBox_number = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_number.setGeometry(QtCore.QRect(230, 120, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox_number.setFont(font)
        self.spinBox_number.setStyleSheet("QSpinBox{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px\n"
"}\n"
"QSpinBox:hover{\n"
"background-color:#444444\n"
"}")
        self.spinBox_number.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_number.setObjectName("spinBox_number")
        self.checkBox_prime = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_prime.setGeometry(QtCore.QRect(80, 310, 110, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.checkBox_prime.setFont(font)
        self.checkBox_prime.setStyleSheet("QCheckBox{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px;\n"
"padding:8px\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"background-color:#444444\n"
"}")
        self.checkBox_prime.setObjectName("checkBox_prime")
        self.checkBox_composite = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_composite.setGeometry(QtCore.QRect(220, 310, 160, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.checkBox_composite.setFont(font)
        self.checkBox_composite.setStyleSheet("QCheckBox{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px;\n"
"padding:8px\n"
"}\n"
"QCheckBox:hover{\n"
"background-color:#444444\n"
"}")
        self.checkBox_composite.setObjectName("checkBox_composite")
        self.pushButton_detect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detect.setGeometry(QtCore.QRect(150, 190, 170, 50))
        self.pushButton_detect.setIcon(QtGui.QIcon("calculator.png"))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_detect.setFont(font)
        self.pushButton_detect.setStyleSheet("QPushButton{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px;\n"
"padding:8px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#444444\n"
"}\n"
"")
        self.pushButton_detect.setObjectName("pushButton_detect")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 285, 340, 101))
        self.label_4.setStyleSheet("QLabel{\n"
"background-color:#929292;\n"
"border:2px solid black;\n"
"border-radius:20px\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 90, 340, 181))
        self.label_5.setStyleSheet("QLabel{\n"
"background-color:#929292;\n"
"border:2px solid black;\n"
"border-radius:20px\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 222, 290, 70))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px\n"
"}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 207, 310, 330))
        self.label_7.setStyleSheet("QLabel{\n"
"background-color:#929292;\n"
"border:2px solid black;\n"
"border-radius:20px\n"
"}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.listWidget_prime_nums = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_prime_nums.setGeometry(QtCore.QRect(490, 300, 230, 220))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_prime_nums.setFont(font)
        self.listWidget_prime_nums.setStyleSheet("QListWidget{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px;\n"
"padding-left:85px;\n"
"padding-top:5px\n"
"}\n"
"QListWidget:hover{\n"
"background-color:#444444\n"
"}")
        self.listWidget_prime_nums.setObjectName("listWidget_prime_nums")
        self.label_gif2 = QtWidgets.QLabel(self.centralwidget)
        self.label_gif2.setGeometry(QtCore.QRect(430, 540, 360, 230))
        self.label_gif2.setText("")
        self.label_gif2.setPixmap(QtGui.QPixmap("1757252.gif"))
        self.label_gif2.setScaledContents(True)
        self.label_gif2.setObjectName("label_gif2")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(60, 20, 121, 51))
        self.pushButton_exit.setIcon(QtGui.QIcon("door-open-out.png"))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#444444\n"
"}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.listWidget_prime_nums_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_prime_nums_2.setGeometry(QtCore.QRect(110, 475, 230, 220))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_prime_nums_2.setFont(font)
        self.listWidget_prime_nums_2.setStyleSheet("QListWidget{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px;\n"
"padding-left:85px;\n"
"padding-top:5px\n"
"}\n"
"QListWidget:hover{\n"
"background-color:#444444\n"
"}")
        self.listWidget_prime_nums_2.setObjectName("listWidget_prime_nums_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 415, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"background-color:black;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:20px\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 400, 340, 310))
        self.label_9.setStyleSheet("QLabel{\n"
"background-color:#929292;\n"
"border:2px solid black;\n"
"border-radius:20px\n"
"}")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.spinBox_number.raise_()
        self.checkBox_prime.raise_()
        self.checkBox_composite.raise_()
        self.pushButton_detect.raise_()
        self.label_6.raise_()
        self.pushButton_exit.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.listWidget_prime_nums_2.raise_()
        self.label_gif2.raise_()
        self.listWidget_prime_nums.raise_()
        self.label_gif.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_detect.clicked.connect(self.detect_prime)
        self.pushButton_exit.clicked.connect(lambda:MainWindow.close())


    def detect_prime(self):
        self.listWidget_prime_nums.clear()
        self.listWidget_prime_nums_2.clear()
        self.checkBox_prime.setChecked(False)
        self.checkBox_composite.setChecked(False)
        
        number = self.spinBox_number.value()
        
        status, counters = recognize_n(number)
        count, nums_under = prime_nums_under(number)
        counters = [str(num) for num in counters]
        
        if status == "prime":
                self.checkBox_prime.setChecked(True)  
                self.listWidget_prime_nums.addItems(nums_under)
                self.listWidget_prime_nums_2.addItems(counters)
        else:
                self.checkBox_composite.setChecked(True)  
                self.listWidget_prime_nums.addItems(nums_under)  
                self.listWidget_prime_nums_2.addItems(counters)

                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "prime numbers"))
        self.label_2.setText(_translate("MainWindow", "Number : "))
        self.label_3.setText(_translate("MainWindow", "Detect prime number"))
        self.checkBox_prime.setText(_translate("MainWindow", "Prime"))
        self.checkBox_composite.setText(_translate("MainWindow", "Composite"))
        self.pushButton_detect.setText(_translate("MainWindow", "Detect"))
        self.label_6.setText(_translate("MainWindow", "Prime numbers under\n"
"the number :  "))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.label_8.setText(_translate("MainWindow", "Counters : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
