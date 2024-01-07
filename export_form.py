# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportForm(object):
    def setupUi(self, ExportForm):
        ExportForm.setObjectName("ExportForm")
        ExportForm.resize(750, 480)
        self.qrcode = QtWidgets.QLabel(ExportForm)
        self.qrcode.setGeometry(QtCore.QRect(430, 90, 240, 240))
        self.qrcode.setText("")
        self.qrcode.setObjectName("qrcode")
        self.login_status = QtWidgets.QLabel(ExportForm)
        self.login_status.setGeometry(QtCore.QRect(500, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.login_status.setFont(font)
        self.login_status.setObjectName("login_status")
        self.export_bt = QtWidgets.QPushButton(ExportForm)
        self.export_bt.setGeometry(QtCore.QRect(520, 400, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.export_bt.setFont(font)
        self.export_bt.setObjectName("export_bt")
        self.export_status = QtWidgets.QLabel(ExportForm)
        self.export_status.setEnabled(True)
        self.export_status.setGeometry(QtCore.QRect(530, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.export_status.setFont(font)
        self.export_status.setObjectName("export_status")
        self.frame_charge = QtWidgets.QFrame(ExportForm)
        self.frame_charge.setGeometry(QtCore.QRect(20, 80, 361, 271))
        self.frame_charge.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_charge.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_charge.setLineWidth(5)
        self.frame_charge.setObjectName("frame_charge")
        self.selet_title = QtWidgets.QLabel(self.frame_charge)
        self.selet_title.setGeometry(QtCore.QRect(20, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.selet_title.setFont(font)
        self.selet_title.setObjectName("selet_title")
        self.begin_lb = QtWidgets.QLabel(self.frame_charge)
        self.begin_lb.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.begin_lb.setObjectName("begin_lb")
        self.end_lb = QtWidgets.QLabel(self.frame_charge)
        self.end_lb.setGeometry(QtCore.QRect(40, 210, 71, 21))
        self.end_lb.setObjectName("end_lb")
        self.begin_date = QtWidgets.QDateEdit(self.frame_charge)
        self.begin_date.setGeometry(QtCore.QRect(120, 170, 110, 22))
        self.begin_date.setObjectName("begin_date")
        self.end_date = QtWidgets.QDateEdit(self.frame_charge)
        self.end_date.setGeometry(QtCore.QRect(120, 210, 110, 22))
        self.end_date.setObjectName("end_date")
        self.status_radio_group = QtWidgets.QGroupBox(self.frame_charge)
        self.status_radio_group.setGeometry(QtCore.QRect(20, 40, 281, 71))
        self.status_radio_group.setObjectName("status_radio_group")
        self.rb1 = QtWidgets.QRadioButton(self.status_radio_group)
        self.rb1.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.rb1.setObjectName("rb1")
        self.rb2 = QtWidgets.QRadioButton(self.status_radio_group)
        self.rb2.setGeometry(QtCore.QRect(90, 30, 81, 20))
        self.rb2.setObjectName("rb2")
        self.rb3 = QtWidgets.QRadioButton(self.status_radio_group)
        self.rb3.setGeometry(QtCore.QRect(180, 30, 95, 20))
        self.rb3.setObjectName("rb3")
        self.logout = QtWidgets.QPushButton(ExportForm)
        self.logout.setGeometry(QtCore.QRect(160, 410, 75, 24))
        self.logout.setObjectName("logout")
        self.switch_account = QtWidgets.QPushButton(ExportForm)
        self.switch_account.setGeometry(QtCore.QRect(40, 410, 91, 24))
        self.switch_account.setObjectName("switch_account")
        self.register_bt = QtWidgets.QPushButton(ExportForm)
        self.register_bt.setGeometry(QtCore.QRect(240, 10, 61, 24))
        self.register_bt.setObjectName("register_bt")
        self.login_bt = QtWidgets.QPushButton(ExportForm)
        self.login_bt.setGeometry(QtCore.QRect(320, 10, 61, 24))
        self.login_bt.setObjectName("login_bt")
        self.remain_point = QtWidgets.QLabel(ExportForm)
        self.remain_point.setGeometry(QtCore.QRect(420, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remain_point.setFont(font)
        self.remain_point.setObjectName("remain_point")
        self.recharge = QtWidgets.QPushButton(ExportForm)
        self.recharge.setGeometry(QtCore.QRect(600, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recharge.setFont(font)
        self.recharge.setObjectName("recharge")

        self.retranslateUi(ExportForm)
        QtCore.QMetaObject.connectSlotsByName(ExportForm)

    def retranslateUi(self, ExportForm):
        _translate = QtCore.QCoreApplication.translate
        ExportForm.setWindowTitle(_translate("ExportForm", "导出页面"))
        self.login_status.setText(_translate("ExportForm", "扫码登录店铺"))
        self.export_bt.setText(_translate("ExportForm", "导出订单"))
        self.export_status.setText(_translate("ExportForm", "导出状态：未开始"))
        self.selet_title.setText(_translate("ExportForm", "时间选择"))
        self.begin_lb.setText(_translate("ExportForm", "开始时间"))
        self.end_lb.setText(_translate("ExportForm", "结束时间"))
        self.status_radio_group.setTitle(_translate("ExportForm", "订单状态"))
        self.rb1.setText(_translate("ExportForm", "待发货"))
        self.rb2.setText(_translate("ExportForm", "已发货"))
        self.rb3.setText(_translate("ExportForm", "全部"))
        self.logout.setText(_translate("ExportForm", "退出登录"))
        self.switch_account.setText(_translate("ExportForm", "切换店铺号"))
        self.register_bt.setText(_translate("ExportForm", "注册"))
        self.login_bt.setText(_translate("ExportForm", "登录"))
        self.remain_point.setText(_translate("ExportForm", "剩余点数：0"))
        self.recharge.setText(_translate("ExportForm", "充值"))
