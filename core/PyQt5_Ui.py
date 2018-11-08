#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:python
@file: PyQt5_Ui.py
@time: 2018/10/30
"""

import sys, os, re, hashlib, hmac
from core import excel_module
from core import main
from core import logger
from conf import settings
# from PyQt5.QtWidgets import (QWidget, QDialog, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton,
#     QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget, QGroupBox, QMessageBox, QApplication, QMainWindow, QDesktopWidget)
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPixmap
# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 调试信息句柄
accoountlog = logger.logger("account")

i = 1
picture_dir = settings.BASE_DIR + os.sep + "picture" + os.sep

class LoginAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()
    def center(self):
        # qr = self.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        # self.move(qr.topLeft())

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, \
                  (screen.height() - size.height()) / 2)

    def initGui(self):
        # 左侧
        self.Pic_lable = QLabel(self)
        self.Pic_lable.setPixmap(QPixmap(picture_dir+'1.jpeg'))
        self.Pic_lable.setScaledContents (True)
        # 固定标签大小
        # self.Pic_lable.resize(500,370)
        # self.Pic_lable.setFixedSize(500, 370)
        LeftLayout = QGridLayout()
        LeftLayout.addWidget(self.Pic_lable, 1, 1, 5, 5)
        LeftGridGroupBox = QGroupBox()
        LeftGridGroupBox.setLayout(LeftLayout)

        # 右侧
        self.AccountEdit = QLineEdit()
        # 编辑框内容提示
        # self.AccountEdit.setPlaceholderText("Account")
        self.PasswordEdit = QLineEdit(self)
        # self.PasswordEdit.setPlaceholderText("Password")
        self.PasswordEdit.setEchoMode(QLineEdit.Password)
        self.Accountlabe = QLabel("账号:")
        self.Accountlabe.setAlignment(Qt.AlignRight)
        self.Passwordlabe = QLabel("密码:")
        self.Passwordlabe.setAlignment(Qt.AlignRight)
        self.LoginButton = QPushButton("登录")
        self.LoginButton.clicked.connect(self.login)

        self.BtnCheck = QRadioButton("显示密码")
        self.BtnCheck.setStyleSheet('''color: rgb(253,129,53);;''')
        self.BtnCheck.clicked.connect(self.yanma)

        # RightLayout = QGridLayout()
        # RightLayout.setSpacing(1)
        # RightLayout.addWidget(self.Accountlabe, 1, 0)
        # RightLayout.addWidget(self.AccountEdit, 1, 1)
        # RightLayout.addWidget(self.Passwordlabe, 2, 0)
        # RightLayout.addWidget(self.PasswordEdit, 2, 1)
        # RightLayout.addWidget(self.BtnCheck, 3, 1)
        # RightLayout.addWidget(self.LoginButton, 4, 1)
        # RightGridGroupBox = QGroupBox("用户登录")
        # RightGridGroupBox.setLayout(RightLayout)

        layout1 = QHBoxLayout()
        layout1.addWidget(self.Accountlabe)
        layout1.addWidget(self.AccountEdit)
        layout2 = QHBoxLayout()
        layout2.addWidget(self.Passwordlabe)
        layout2.addWidget(self.PasswordEdit)
        layout3 = QHBoxLayout()
        layout3.addWidget(self.BtnCheck)
        layout3.addStretch(1)
        layout4 = QHBoxLayout()
        layout4.addStretch(1)
        layout4.addWidget(self.LoginButton)
        layout4.addStretch(1)
        RightLayout = QVBoxLayout()
        RightLayout.addLayout(layout1)
        RightLayout.addLayout(layout2)
        RightLayout.addLayout(layout3)
        RightLayout.addLayout(layout4)
        RightLayout.setContentsMargins(20, 20, 20, 20)
        RightGridGroupBox = QGroupBox("用户登录")
        RightGridGroupBox.setLayout(RightLayout)

        # 底部
        self.RegisteredButton = QPushButton("注册")
        self.RegisteredButton.clicked.connect(self.registered_clicked)
        self.FindPasswordButton = QPushButton("找回密码")
        self.FindPasswordButton.clicked.connect(self.findpassword)
        BottomLayout = QHBoxLayout()
        BottomLayout.addStretch(1)
        BottomLayout.addWidget(self.FindPasswordButton)
        BottomLayout.addWidget(self.RegisteredButton)

        # 将左侧和右侧放到一个水平的布局中，构成顶部
        TopLayout = QHBoxLayout()
        TopLayout.addWidget(LeftGridGroupBox)
        TopLayout.addWidget(RightGridGroupBox)

        MainLayout = QVBoxLayout()
        MainLayout.addStretch(1)
        MainLayout.addLayout(TopLayout)
        MainLayout.addLayout(BottomLayout)
        self.setLayout(MainLayout)

        # 定时器来动态切换图片
        self.Timer = QBasicTimer()
        self.Timer.start(2000, self)

        self.center()
        # self.setGeometry(300, 300, 800, 350)
        self.resize(800, 350)
        self.setFixedSize(800, 350)
        self.setToolTip("HealthCareSystem")
        QToolTip.setFont(QFont \
                ("微软雅黑", 12))
        self.setWindowTitle("健康监护系统")
        # self.show()
        # self.close()
        # self.hide()

    def login(self):
        h = hmac.new('healthcaresystem'.encode('utf-8'), self.PasswordEdit.text().encode('utf-8'))
        password = h.hexdigest()
        if excel_module.account_check(self.AccountEdit.text(), password):
            print("系统登录成功")
            # self.close()
            self.hide()
            userdata = UserDate()
            userdata.center()
            userdata.show()
            userdata.exec_()
            self.center()
            self.show()
        else:
            print("用户名或者密码错误")
            QMessageBox.warning(self, "登录错误提示", "用户名或密码错误", QMessageBox.Yes)

    def registered_clicked(self):
        self.hide()
        # self.close()

        registered = Registered()
        registered.show()
        registered.exec_()
        self.show()

    def findpassword(self):
        pass

    def yanma(self):
        if self.BtnCheck.isChecked():
            self.PasswordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.PasswordEdit.setEchoMode(QLineEdit.Password)
    def timerEvent(self, e):
        global i
        global picture_dir
        picture = (picture_dir+"%d.jpeg" % i)
        self.Pic_lable.setPixmap(QPixmap(picture))
        i += 1
        if i > 2:
            i = 1
    def closeEvent(self, event):
        # 重新定义colseEvent
        reply = QMessageBox.question\
        (self,"信息",
        "你确定要退出吗？",
        QMessageBox.Yes,
        QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class UserDate(QDialog):
    def __init__(self):
        super().__init__()
        self.initGui()

    def center(self):
        # qr = self.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        # self.move(qr.topLeft())
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, \
                  (screen.height() - size.height()) / 2)

    def initGui(self):
    #左侧
        text_leber = QLabel("实时上传数据：")
        userdataListBox = QListWidget()
        applications = []
        for i in range(1, 31):
            applications.append("Application %d" % i)

        userdataListBox.insertItems(0, applications)

        Left_layout = QVBoxLayout()
        Left_layout.addWidget(text_leber)
        Left_layout.addSpacing(12)
        Left_layout.addWidget(userdataListBox)
    #右侧
        user_label = QLabel("用户:")
        blood_label = QLabel("血压: 0 sbp   0 dbp")
        sugar_label = QLabel("血糖: 0 mmol")
        time_label = QLabel("时间:")

        RightLayout = QVBoxLayout()
        RightLayout.addWidget(user_label)
        RightLayout.addWidget(blood_label)
        RightLayout.addWidget(sugar_label)
        RightLayout.addWidget(time_label)
        RightLayout.setContentsMargins(40, 10, 40, 40)

        mainLayout = QHBoxLayout()

        mainLayout.setContentsMargins(40, 40, 40, 40)
        mainLayout.addLayout(Left_layout)
        # mainLayout.setSpacing(60)

        # mainLayout.addStretch(1)
        mainLayout.addLayout(RightLayout)


        self.setLayout(mainLayout)
        self.center()
        # self.setGeometry(300, 300, 800, 250)
        # self.resize(800, 250)
        # self.setFixedSize(800, 350)

        self.setWindowIcon(QIcon(picture_dir+"1.jpeg"))
        self.setWindowTitle("健康监护系统")

class Registered(QDialog):
    def __init__(self):
        super().__init__()
        self.initGui()

    def center(self):
        # qr = self.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        # self.move(qr.topLeft())
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, \
                  (screen.height() - size.height()) / 2)

    def initGui(self):
        # 左侧
        self.Pic_lable = QLabel(self)
        self.Pic_lable.adjustSize()
        self.Pic_lable.setPixmap(QPixmap(picture_dir+'2.jpeg'))

        LeftGridGroupBox = QGroupBox()
        LeftLayout = QGridLayout()
        LeftLayout.addWidget(self.Pic_lable, 1, 1, 5, 5)
        LeftGridGroupBox.setLayout(LeftLayout)

        # 右侧
        self.PhoneNumberEdit = QLineEdit(self)
        # self.PhoneNumberEdit.textChanged.connect(self.phonenumbercheck)
        self.PasswordEdit = QLineEdit(self)
        self.ConfirmPasswordEdit =QLineEdit(self)
        self.PasswordEdit.setEchoMode(QLineEdit.Password)
        self.ConfirmPasswordEdit.setEchoMode(QLineEdit.Password)

        self.PhoneNumberlabe = QLabel("手机号码:")
        self.PhoneNumberlabe.setAlignment(Qt.AlignRight)
        self.Passwordlabe = QLabel("密码:")
        self.Passwordlabe.setAlignment(Qt.AlignRight)
        self.ConfirmPasswordlabe = QLabel("确认密码:")
        self.ConfirmPasswordlabe.setAlignment(Qt.AlignRight)

        RightLayout = QGridLayout()
        RightLayout.addWidget(self.PhoneNumberlabe, 0, 0)
        RightLayout.addWidget(self.PhoneNumberEdit, 0, 1, 1, 4)
        RightLayout.addWidget(self.Passwordlabe, 1, 0)
        RightLayout.addWidget(self.PasswordEdit, 1, 1, 1, 4)
        RightLayout.addWidget(self.ConfirmPasswordlabe, 2, 0)
        RightLayout.addWidget(self.ConfirmPasswordEdit, 2, 1, 1, 4)

        # RightLayout.setColumnStretch(1, 10)
        # RightLayout.setColumnStretch(2, 20)
        RightGridGroupBox = QGroupBox("用户注册")
        RightGridGroupBox.setLayout(RightLayout)

        # 底部
        self.RegisteredButton = QPushButton("注册")
        self.RegisteredButton.clicked.connect(self.registered)
        self.LoginButton = QPushButton("登录")
        self.LoginButton.clicked.connect(self.login)
        BottomLayout = QHBoxLayout()
        BottomLayout.addStretch(1)
        BottomLayout.addWidget(self.LoginButton)
        BottomLayout.addWidget(self.RegisteredButton)

        # 将左侧和右侧放到一个水平的布局中，构成顶部
        TopLayout = QHBoxLayout()
        TopLayout.addWidget(LeftGridGroupBox)
        TopLayout.addWidget(RightGridGroupBox)

        MainLayout = QVBoxLayout()
        MainLayout.addStretch(1)
        MainLayout.addLayout(TopLayout)
        MainLayout.addLayout(BottomLayout)
        self.setLayout(MainLayout)

        self.center()
        # self.setGeometry(300, 300, 800, 350)
        self.resize(800, 350)
        self.setFixedSize(800, 350)
        self.setWindowTitle("健康监护系统")
        # self.show()

    def login(self):
        # loginaccount.show()
        # registered.close()
        self.close()

    def registered(self):
        if self.phonenumbercheck(self.PhoneNumberEdit.text()) is False:
            return
        if self.password(self.PasswordEdit.text()) is False:
            return
        if self.PasswordEdit.text() != self.ConfirmPasswordEdit.text():
            QMessageBox.warning(self,"Warning", "两次输入的密码不相同", QMessageBox.Yes)
            return

        main.account_info["account"] = self.PhoneNumberEdit.text()
        main.account_info["password"] = self.PasswordEdit.text()
        h = hmac.new('healthcaresystem'.encode('utf-8'),self.PasswordEdit.text().encode('utf-8'))
        # h = hashlib.sha256(self.PasswordEdit.text().encode('utf-8'))
        # print(h.hexdigest())
        main.account_info["password_sh256"] = h.hexdigest()
        excel_module.account_save(main.account_info)
        # QMessageBox.information(self, "注册提示", "账号注册成功,请返回登录界面", QMessageBox.Yes)
        reply = QMessageBox.information(self,
                "注册提示", "账号注册成功,点击ok返回登录界面")
        if reply == QMessageBox.Ok:
            self.close()

        accoountlog.info("account [%s] registration successfully" % self.PhoneNumberEdit.text())

    def phonenumbercheck(self, phonenumber):
        # 十一位的纯数字
        if re.match(r'^\d{11}$', phonenumber) is None:
            QMessageBox.warning(self, "手机号码输入错误", "请输入11位数子的手机号码", QMessageBox.Yes)
            return False
        else:
            if excel_module.account_isexit(phonenumber):
                return True
            else:
                print("该号码已注册过")
                QMessageBox.warning(self,"Warning", "该号码已注册过", QMessageBox.Yes)
                return False

    def password(self, password):
        # 密码必须由字母和数字组成
        if re.match(r'[0-9a-zA-Z\_]{6,12}', password) is None:
            QMessageBox.warning(self, "密码输入错误", "请输入6~12位由数字、字母、下划线组成的密码", QMessageBox.Yes)
            return False
        else:
            return True

def loginaccount():
    app = QApplication(sys.argv)
    loginaccount = LoginAccount()
    loginaccount.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    # app = QApplication(sys.argv)
    # loginaccount = LoginAccount()
    # registered = Registered()
    # loginaccount.show()
    # sys.exit(app.exec_())
    loginaccount()