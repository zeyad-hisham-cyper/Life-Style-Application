from os import path
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), 'main.ui'))

amount_used = 0
cal_num = 0
bed_time = ""


class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('.img\logo.png'))
        self.setWindowTitle("Regulated Life Style")
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        self.setFixedSize(self.size())
        self.handle_buttons()
        self.frame.hide()


    # Funiction to handle Buttons

    def handle_buttons(self):
        self.Home.clicked.connect(self.home_page)
        self.personal.clicked.connect(self.personal_page)
        self.food.clicked.connect(self.food_page)
        self.sleep.clicked.connect(self.sleep_page)
        self.dev.clicked.connect(self.dev_page)
        self.pushButton.clicked.connect(self.foodsystem)
        self.next.clicked.connect(self.chal_calc)
        self.calc.clicked.connect(self.meals)
        self.pushButton_8.clicked.connect(self.sleeping)


    #funictions to connect Widget with buttons

    def home_page(self):
        self.tabWidget.setCurrentIndex(0)

    def personal_page(self):
        self.tabWidget.setCurrentIndex(1)

    def food_page(self):
        self.tabWidget.setCurrentIndex(2)

    def sleep_page(self):
        self.tabWidget.setCurrentIndex(4)

    def dev_page(self):
        self.tabWidget.setCurrentIndex(5)

    def chal_calc(self):
        self.tabWidget.setCurrentIndex(3)


    # Funiction to system f00d and calculate the calories
    def foodsystem(self):
        global cal_num

        wh = str(self.comboBox.currentText())
        n = self.name.text()
        Age = self.age.text()
        l = self.length.text()
        w = self.weight.text()
        shift = str(self.comboBox_2.currentText())
        gender = str(self.comboBox_3.currentText())
        Age = float(Age)
        l = float(l)
        w = float(w)
        if gender == "Male":
            cal_num = ((w * 10) + (l * 6.25) - (Age * 5) + 5) * 1.375
            cal_num = round(cal_num, 2)
            water_amount = (w / 0.4536) / 50
            water_amount = round(water_amount, 2)
            fsys = "Your body need {} number of chalories\nand {} liter of water.\nUse the following table to know should you\neat:".format(
                cal_num, water_amount)

        if gender == "Female":
            cal_num = ((w * 10) + (l * 6.25) - (Age * 5) - 161) * 1.375
            cal_num = round(cal_num, 2)
            water_amount = (w / 0.4536) / 50
            water_amount = round(water_amount, 2)
            fsys = "Your body need {} number of chalories\nand {} liter of water.\nUse the following table to know should you\neat:".format(
                cal_num, water_amount)

        self.label_5.setText(fsys)
        self.frame.show()
        self.tabWidget.setCurrentIndex(2)


    #Funiction to calculate calories per meal
    def meals(self):
        global cal_num
        global amount_used
        msg = QMessageBox()
        msg.setWindowTitle("Alert ^_^")
        
        if self.checkBox.isChecked:
            Pastries = self.lineEdit_2.text()
            cakes = int(Pastries)
            amount_used += (cakes/100) * 129
        if self.checkBox_2.isChecked:
            Pasta = self.lineEdit_3.text()
            PPPP = int(Pasta)
            amount_used += (PPPP/100) * 157
        if self.checkBox_4.isChecked:
            Rice = self.lineEdit_4.text()
            roz = int(Rice)
            amount_used += (roz/100) * 130
        if self.checkBox_3.isChecked:
            Bread = self.lineEdit_5.text()
            eish = int(Bread)
            amount_used += (eish/100) * 285
        if self.checkBox_8.isChecked:
            Potato = int(self.lineEdit_6.text())
            amount_used += (Potato / 100) * 77
        if self.checkBox_7.isChecked:
            egg = int(self.lineEdit_7.text())
            amount_used += egg * 78
        if self.checkBox_5.isChecked:
            checkien = int(self.lineEdit_8.text())
            amount_used += checkien * 284
        if self.checkBox_6.isChecked:
            cups = int(self.lineEdit_9.text())
            amount_used += cups * 149
        if self.checkBox_10.isChecked:
            beef = int(self.lineEdit_10.text())
            amount_used += beef * 216
        if self.checkBox_14.isChecked:
            fish = int(self.lineEdit_11.text())
            amount_used += fish * 206


        self.lcdNumber.display(amount_used)
        rest = cal_num - amount_used
        msg.setText("Your Meal have {} numbers\nof calories and you have\n{} calories left".format(amount_used, rest))
        msg.exec_()

    # Funiction to schedule sleep
    def sleeping(self):
        global bed_time
        wake_time = str(self.comboBox_4.currentText())
        if wake_time == "05:00 AM":
            bed_time = "09:30 PM"
        if wake_time == "06:00 AM":
            bed_time = "10:30 PM"
        if wake_time == "07:00 AM":
            bed_time = "11:30 PM"
        if wake_time == "08:00 AM":
            bed_time = "12:30 AM"
        if wake_time == "09:00 AM":
            bed_time = "01:30 AM"
        if wake_time == "10:00 AM":
            bed_time = "02:30 AM"
        if wake_time == "11:00 AM":
            bed_time = "03:30 AM"
        if wake_time == "12:00 PM":
            bed_time = "04:30 AM"
        if wake_time == "01:00 PM":
            bed_time = "05:30 AM"
        if wake_time == "02:00 PM":
            bed_time = "06:30 AM"
        if wake_time == "03:00 PM":
            bed_time = "07:30 AM"
        if wake_time == "04:00 PM":
            bed_time = "08:30 AM"
        if wake_time == "05:00 PM":
            bed_time = "09:30 AM"

        msg = QMessageBox()
        msg.setWindowTitle("Alert ^_^")
        msg.setText("Your must go to bed at {} I will remind you in this time".format(bed_time))
        msg.exec_()
        self.label_8.setText(bed_time)
        text = "NOTE:\nYou Should go to bed 14 minutes early"
        self.label_9.setText(text)

def main():
    import sys
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
