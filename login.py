# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1381, 863)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.app = QtWidgets.QFrame(self.centralwidget)
        self.app.setMaximumSize(QtCore.QSize(1200, 850))
        self.app.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app.setLineWidth(1)
        self.app.setObjectName("app")
        self.stackedWidget = QtWidgets.QStackedWidget(self.app)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 821))
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1200, 850))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.login_frame = QtWidgets.QFrame(self.login)
        self.login_frame.setGeometry(QtCore.QRect(430, 140, 391, 481))
        self.login_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.label_user_login = QtWidgets.QLabel(self.login_frame)
        self.label_user_login.setGeometry(QtCore.QRect(120, 90, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_login.setFont(font)
        self.label_user_login.setObjectName("label_user_login")
        self.username = QtWidgets.QLineEdit(self.login_frame)
        self.username.setGeometry(QtCore.QRect(80, 130, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setKerning(True)
        self.username.setFont(font)
        self.username.setMaxLength(10)
        self.username.setFrame(False)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.label_pass_login = QtWidgets.QLabel(self.login_frame)
        self.label_pass_login.setGeometry(QtCore.QRect(140, 180, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_pass_login.setFont(font)
        self.label_pass_login.setObjectName("label_pass_login")
        self.password = QtWidgets.QLineEdit(self.login_frame)
        self.password.setGeometry(QtCore.QRect(80, 220, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setKerning(True)
        self.password.setFont(font)
        self.password.setMaxLength(10)
        self.password.setFrame(False)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.login_btn = QtWidgets.QPushButton(self.login_frame)
        self.login_btn.setGeometry(QtCore.QRect(100, 320, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.register_btn = QtWidgets.QPushButton(self.login_frame)
        self.register_btn.setGeometry(QtCore.QRect(100, 410, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.register_btn.setFont(font)
        self.register_btn.setObjectName("register_btn")
        self.user_pass_err = QtWidgets.QLineEdit(self.login_frame)
        self.user_pass_err.setGeometry(QtCore.QRect(60, 270, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.user_pass_err.setFont(font)
        self.user_pass_err.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.user_pass_err.setMouseTracking(False)
        self.user_pass_err.setFocusPolicy(QtCore.Qt.NoFocus)
        self.user_pass_err.setFrame(False)
        self.user_pass_err.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pass_err.setObjectName("user_pass_err")
        self.title_log = QtWidgets.QLabel(self.login_frame)
        self.title_log.setGeometry(QtCore.QRect(10, 20, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_log.setFont(font)
        self.title_log.setAlignment(QtCore.Qt.AlignCenter)
        self.title_log.setObjectName("title_log")
        self.label = QtWidgets.QLabel(self.login)
        self.label.setGeometry(QtCore.QRect(320, 60, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.login)
        self.registration = QtWidgets.QWidget()
        self.registration.setObjectName("registration")
        self.registration_frame = QtWidgets.QFrame(self.registration)
        self.registration_frame.setGeometry(QtCore.QRect(430, 140, 391, 481))
        self.registration_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_frame.setObjectName("registration_frame")
        self.label_user_register = QtWidgets.QLabel(self.registration_frame)
        self.label_user_register.setGeometry(QtCore.QRect(70, 90, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_register.setFont(font)
        self.label_user_register.setObjectName("label_user_register")
        self.label_pass_register = QtWidgets.QLabel(self.registration_frame)
        self.label_pass_register.setGeometry(QtCore.QRect(40, 180, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_pass_register.setFont(font)
        self.label_pass_register.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pass_register.setObjectName("label_pass_register")
        self.login_back_btn = QtWidgets.QPushButton(self.registration_frame)
        self.login_back_btn.setGeometry(QtCore.QRect(100, 410, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login_back_btn.setFont(font)
        self.login_back_btn.setObjectName("login_back_btn")
        self.username_reg = QtWidgets.QLineEdit(self.registration_frame)
        self.username_reg.setGeometry(QtCore.QRect(80, 130, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setKerning(True)
        self.username_reg.setFont(font)
        self.username_reg.setMaxLength(10)
        self.username_reg.setFrame(False)
        self.username_reg.setAlignment(QtCore.Qt.AlignCenter)
        self.username_reg.setObjectName("username_reg")
        self.user_pass_err_reg = QtWidgets.QLineEdit(self.registration_frame)
        self.user_pass_err_reg.setGeometry(QtCore.QRect(56, 270, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.user_pass_err_reg.setFont(font)
        self.user_pass_err_reg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.user_pass_err_reg.setMouseTracking(False)
        self.user_pass_err_reg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.user_pass_err_reg.setFrame(False)
        self.user_pass_err_reg.setAlignment(QtCore.Qt.AlignCenter)
        self.user_pass_err_reg.setObjectName("user_pass_err_reg")
        self.password_reg = QtWidgets.QLineEdit(self.registration_frame)
        self.password_reg.setGeometry(QtCore.QRect(80, 220, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setKerning(True)
        self.password_reg.setFont(font)
        self.password_reg.setMaxLength(10)
        self.password_reg.setFrame(False)
        self.password_reg.setAlignment(QtCore.Qt.AlignCenter)
        self.password_reg.setObjectName("password_reg")
        self.register_new_btn = QtWidgets.QPushButton(self.registration_frame)
        self.register_new_btn.setGeometry(QtCore.QRect(100, 320, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.register_new_btn.setFont(font)
        self.register_new_btn.setObjectName("register_new_btn")
        self.title_reg = QtWidgets.QLabel(self.registration_frame)
        self.title_reg.setGeometry(QtCore.QRect(10, 20, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_reg.setFont(font)
        self.title_reg.setAlignment(QtCore.Qt.AlignCenter)
        self.title_reg.setObjectName("title_reg")
        self.min_max = QtWidgets.QLabel(self.registration_frame)
        self.min_max.setGeometry(QtCore.QRect(100, 370, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        self.min_max.setFont(font)
        self.min_max.setAlignment(QtCore.Qt.AlignCenter)
        self.min_max.setObjectName("min_max")
        self.label_2 = QtWidgets.QLabel(self.registration)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.registration)
        self.dashboard = QtWidgets.QWidget()
        self.dashboard.setObjectName("dashboard")
        self.dash = QtWidgets.QStackedWidget(self.dashboard)
        self.dash.setGeometry(QtCore.QRect(130, 0, 931, 821))
        self.dash.setObjectName("dash")
        self.notifiche = QtWidgets.QWidget()
        self.notifiche.setObjectName("notifiche")
        self.notifiche_frame = QtWidgets.QFrame(self.notifiche)
        self.notifiche_frame.setGeometry(QtCore.QRect(10, 70, 911, 751))
        self.notifiche_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notifiche_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notifiche_frame.setObjectName("notifiche_frame")
        self.title_info_utenti_eventi = QtWidgets.QLineEdit(self.notifiche_frame)
        self.title_info_utenti_eventi.setGeometry(QtCore.QRect(570, 20, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_info_utenti_eventi.setFont(font)
        self.title_info_utenti_eventi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title_info_utenti_eventi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.title_info_utenti_eventi.setFrame(False)
        self.title_info_utenti_eventi.setAlignment(QtCore.Qt.AlignCenter)
        self.title_info_utenti_eventi.setObjectName("title_info_utenti_eventi")
        self.table_eventi = QtWidgets.QTableWidget(self.notifiche_frame)
        self.table_eventi.setGeometry(QtCore.QRect(20, 80, 531, 651))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.table_eventi.setFont(font)
        self.table_eventi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_eventi.setShowGrid(True)
        self.table_eventi.setCornerButtonEnabled(False)
        self.table_eventi.setObjectName("table_eventi")
        self.table_eventi.setColumnCount(3)
        self.table_eventi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_eventi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_eventi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_eventi.setHorizontalHeaderItem(2, item)
        self.table_eventi.horizontalHeader().setVisible(False)
        self.table_eventi.horizontalHeader().setHighlightSections(False)
        self.table_eventi.verticalHeader().setVisible(False)
        self.table_eventi.verticalHeader().setHighlightSections(False)
        self.dati_personali_eventi = QtWidgets.QListWidget(self.notifiche_frame)
        self.dati_personali_eventi.setEnabled(True)
        self.dati_personali_eventi.setGeometry(QtCore.QRect(570, 80, 321, 651))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.dati_personali_eventi.setFont(font)
        self.dati_personali_eventi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dati_personali_eventi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dati_personali_eventi.setObjectName("dati_personali_eventi")
        self.title_eventi = QtWidgets.QLineEdit(self.notifiche_frame)
        self.title_eventi.setGeometry(QtCore.QRect(20, 20, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_eventi.setFont(font)
        self.title_eventi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title_eventi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.title_eventi.setFrame(False)
        self.title_eventi.setAlignment(QtCore.Qt.AlignCenter)
        self.title_eventi.setObjectName("title_eventi")
        self.dash.addWidget(self.notifiche)
        self.seguiti = QtWidgets.QWidget()
        self.seguiti.setObjectName("seguiti")
        self.seguiti_frame = QtWidgets.QFrame(self.seguiti)
        self.seguiti_frame.setGeometry(QtCore.QRect(10, 70, 911, 741))
        self.seguiti_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seguiti_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seguiti_frame.setObjectName("seguiti_frame")
        self.cerca_btn = QtWidgets.QPushButton(self.seguiti_frame)
        self.cerca_btn.setGeometry(QtCore.QRect(210, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cerca_btn.setFont(font)
        self.cerca_btn.setObjectName("cerca_btn")
        self.ricerca_utente = QtWidgets.QLineEdit(self.seguiti_frame)
        self.ricerca_utente.setGeometry(QtCore.QRect(20, 20, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.ricerca_utente.setFont(font)
        self.ricerca_utente.setMaxLength(15)
        self.ricerca_utente.setFrame(False)
        self.ricerca_utente.setObjectName("ricerca_utente")
        self.check_seguiti = QtWidgets.QCheckBox(self.seguiti_frame)
        self.check_seguiti.setGeometry(QtCore.QRect(20, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(12)
        self.check_seguiti.setFont(font)
        self.check_seguiti.setChecked(True)
        self.check_seguiti.setObjectName("check_seguiti")
        self.table_utenti = QtWidgets.QTableWidget(self.seguiti_frame)
        self.table_utenti.setGeometry(QtCore.QRect(20, 130, 281, 591))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.table_utenti.setFont(font)
        self.table_utenti.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_utenti.setShowGrid(True)
        self.table_utenti.setCornerButtonEnabled(False)
        self.table_utenti.setObjectName("table_utenti")
        self.table_utenti.setColumnCount(2)
        self.table_utenti.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_utenti.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_utenti.setHorizontalHeaderItem(1, item)
        self.table_utenti.horizontalHeader().setVisible(False)
        self.table_utenti.horizontalHeader().setHighlightSections(False)
        self.table_utenti.verticalHeader().setVisible(False)
        self.table_utenti.verticalHeader().setHighlightSections(False)
        self.title_info_utenti = QtWidgets.QLineEdit(self.seguiti_frame)
        self.title_info_utenti.setGeometry(QtCore.QRect(320, 20, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_info_utenti.setFont(font)
        self.title_info_utenti.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title_info_utenti.setFocusPolicy(QtCore.Qt.NoFocus)
        self.title_info_utenti.setFrame(False)
        self.title_info_utenti.setObjectName("title_info_utenti")
        self.title_msg_utenti = QtWidgets.QLineEdit(self.seguiti_frame)
        self.title_msg_utenti.setGeometry(QtCore.QRect(320, 280, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_msg_utenti.setFont(font)
        self.title_msg_utenti.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title_msg_utenti.setFocusPolicy(QtCore.Qt.NoFocus)
        self.title_msg_utenti.setFrame(False)
        self.title_msg_utenti.setAlignment(QtCore.Qt.AlignCenter)
        self.title_msg_utenti.setObjectName("title_msg_utenti")
        self.table_utenti_info = QtWidgets.QTableWidget(self.seguiti_frame)
        self.table_utenti_info.setGeometry(QtCore.QRect(320, 80, 571, 191))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.table_utenti_info.setFont(font)
        self.table_utenti_info.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_utenti_info.setShowGrid(False)
        self.table_utenti_info.setCornerButtonEnabled(False)
        self.table_utenti_info.setObjectName("table_utenti_info")
        self.table_utenti_info.setColumnCount(2)
        self.table_utenti_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_utenti_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_utenti_info.setHorizontalHeaderItem(1, item)
        self.table_utenti_info.horizontalHeader().setVisible(False)
        self.table_utenti_info.horizontalHeader().setHighlightSections(False)
        self.table_utenti_info.verticalHeader().setVisible(False)
        self.table_utenti_info.verticalHeader().setHighlightSections(False)
        self.follow_btn = QtWidgets.QPushButton(self.seguiti_frame)
        self.follow_btn.setGeometry(QtCore.QRect(680, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.follow_btn.setFont(font)
        self.follow_btn.setText("")
        self.follow_btn.setObjectName("follow_btn")
        self.utente_msg_list = QtWidgets.QListWidget(self.seguiti_frame)
        self.utente_msg_list.setGeometry(QtCore.QRect(320, 340, 571, 381))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(19)
        self.utente_msg_list.setFont(font)
        self.utente_msg_list.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.utente_msg_list.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.utente_msg_list.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.utente_msg_list.setProperty("isWrapping", False)
        self.utente_msg_list.setResizeMode(QtWidgets.QListView.Fixed)
        self.utente_msg_list.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.utente_msg_list.setGridSize(QtCore.QSize(392, 100))
        self.utente_msg_list.setUniformItemSizes(False)
        self.utente_msg_list.setBatchSize(100)
        self.utente_msg_list.setWordWrap(True)
        self.utente_msg_list.setObjectName("utente_msg_list")
        self.dash.addWidget(self.seguiti)
        self.bacheca = QtWidgets.QWidget()
        self.bacheca.setObjectName("bacheca")
        self.bacheca_frame = QtWidgets.QFrame(self.bacheca)
        self.bacheca_frame.setGeometry(QtCore.QRect(10, 70, 911, 751))
        self.bacheca_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bacheca_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bacheca_frame.setObjectName("bacheca_frame")
        self.post_btn = QtWidgets.QPushButton(self.bacheca_frame)
        self.post_btn.setGeometry(QtCore.QRect(640, 660, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.post_btn.setFont(font)
        self.post_btn.setObjectName("post_btn")
        self.post_msg = QtWidgets.QLineEdit(self.bacheca_frame)
        self.post_msg.setGeometry(QtCore.QRect(80, 660, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.post_msg.setFont(font)
        self.post_msg.setMaxLength(50)
        self.post_msg.setFrame(False)
        self.post_msg.setObjectName("post_msg")
        self.table_bacheca = QtWidgets.QTableWidget(self.bacheca_frame)
        self.table_bacheca.setGeometry(QtCore.QRect(20, 70, 871, 571))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.table_bacheca.setFont(font)
        self.table_bacheca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_bacheca.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_bacheca.setIconSize(QtCore.QSize(0, 0))
        self.table_bacheca.setShowGrid(True)
        self.table_bacheca.setCornerButtonEnabled(False)
        self.table_bacheca.setObjectName("table_bacheca")
        self.table_bacheca.setColumnCount(3)
        self.table_bacheca.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_bacheca.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bacheca.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bacheca.setHorizontalHeaderItem(2, item)
        self.table_bacheca.horizontalHeader().setVisible(False)
        self.table_bacheca.horizontalHeader().setHighlightSections(False)
        self.table_bacheca.horizontalHeader().setStretchLastSection(True)
        self.table_bacheca.verticalHeader().setVisible(False)
        self.table_bacheca.verticalHeader().setHighlightSections(False)
        self.max_char = QtWidgets.QLabel(self.bacheca_frame)
        self.max_char.setGeometry(QtCore.QRect(680, 711, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        self.max_char.setFont(font)
        self.max_char.setAlignment(QtCore.Qt.AlignCenter)
        self.max_char.setObjectName("max_char")
        self.title_bacheca = QtWidgets.QLabel(self.bacheca_frame)
        self.title_bacheca.setGeometry(QtCore.QRect(20, 10, 871, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.title_bacheca.setFont(font)
        self.title_bacheca.setAlignment(QtCore.Qt.AlignCenter)
        self.title_bacheca.setObjectName("title_bacheca")
        self.dash.addWidget(self.bacheca)
        self.profilo = QtWidgets.QWidget()
        self.profilo.setObjectName("profilo")
        self.profilo_frame = QtWidgets.QFrame(self.profilo)
        self.profilo_frame.setGeometry(QtCore.QRect(9, 69, 911, 751))
        self.profilo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profilo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profilo_frame.setObjectName("profilo_frame")
        self.personal_msg = QtWidgets.QListWidget(self.profilo_frame)
        self.personal_msg.setGeometry(QtCore.QRect(320, 80, 571, 591))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(19)
        self.personal_msg.setFont(font)
        self.personal_msg.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.personal_msg.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.personal_msg.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.personal_msg.setProperty("isWrapping", False)
        self.personal_msg.setResizeMode(QtWidgets.QListView.Fixed)
        self.personal_msg.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.personal_msg.setGridSize(QtCore.QSize(392, 100))
        self.personal_msg.setUniformItemSizes(False)
        self.personal_msg.setBatchSize(100)
        self.personal_msg.setWordWrap(True)
        self.personal_msg.setObjectName("personal_msg")
        self.mod_data_btn = QtWidgets.QPushButton(self.profilo_frame)
        self.mod_data_btn.setGeometry(QtCore.QRect(200, 50, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mod_data_btn.setFont(font)
        self.mod_data_btn.setObjectName("mod_data_btn")
        self.data_mod = QtWidgets.QLineEdit(self.profilo_frame)
        self.data_mod.setGeometry(QtCore.QRect(20, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        self.data_mod.setFont(font)
        self.data_mod.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.data_mod.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.data_mod.setAcceptDrops(True)
        self.data_mod.setMaxLength(15)
        self.data_mod.setFrame(False)
        self.data_mod.setObjectName("data_mod")
        self.combo_mod_dati = QtWidgets.QComboBox(self.profilo_frame)
        self.combo_mod_dati.setGeometry(QtCore.QRect(20, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod_dati.setFont(font)
        self.combo_mod_dati.setFocusPolicy(QtCore.Qt.NoFocus)
        self.combo_mod_dati.setObjectName("combo_mod_dati")
        self.combo_mod_dati.addItem("")
        self.combo_mod_dati.addItem("")
        self.combo_mod_dati.addItem("")
        self.combo_mod_dati.addItem("")
        self.combo_mod_dati.addItem("")
        self.combo_mod_dati.addItem("")
        self.combo_mod_dati.addItem("")
        self.dati_personali = QtWidgets.QListWidget(self.profilo_frame)
        self.dati_personali.setEnabled(True)
        self.dati_personali.setGeometry(QtCore.QRect(20, 150, 281, 581))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.dati_personali.setFont(font)
        self.dati_personali.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dati_personali.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dati_personali.setObjectName("dati_personali")
        self.personal_msg_title = QtWidgets.QLineEdit(self.profilo_frame)
        self.personal_msg_title.setGeometry(QtCore.QRect(320, 20, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.personal_msg_title.setFont(font)
        self.personal_msg_title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.personal_msg_title.setFocusPolicy(QtCore.Qt.NoFocus)
        self.personal_msg_title.setAcceptDrops(True)
        self.personal_msg_title.setText("")
        self.personal_msg_title.setFrame(False)
        self.personal_msg_title.setAlignment(QtCore.Qt.AlignCenter)
        self.personal_msg_title.setObjectName("personal_msg_title")
        self.el_sel_msg = QtWidgets.QPushButton(self.profilo_frame)
        self.el_sel_msg.setGeometry(QtCore.QRect(380, 680, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.el_sel_msg.setFont(font)
        self.el_sel_msg.setObjectName("el_sel_msg")
        self.dash.addWidget(self.profilo)
        self.frame = QtWidgets.QFrame(self.dashboard)
        self.frame.setGeometry(QtCore.QRect(140, -10, 911, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.notifiche_btn = QtWidgets.QPushButton(self.frame)
        self.notifiche_btn.setGeometry(QtCore.QRect(570, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.notifiche_btn.setFont(font)
        self.notifiche_btn.setObjectName("notifiche_btn")
        self.logout_btn = QtWidgets.QPushButton(self.frame)
        self.logout_btn.setGeometry(QtCore.QRect(750, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.logout_btn.setFont(font)
        self.logout_btn.setObjectName("logout_btn")
        self.bacheca_btn = QtWidgets.QPushButton(self.frame)
        self.bacheca_btn.setGeometry(QtCore.QRect(360, 10, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.bacheca_btn.setFont(font)
        self.bacheca_btn.setObjectName("bacheca_btn")
        self.profilo_dati_btn = QtWidgets.QPushButton(self.frame)
        self.profilo_dati_btn.setGeometry(QtCore.QRect(0, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.profilo_dati_btn.setFont(font)
        self.profilo_dati_btn.setObjectName("profilo_dati_btn")
        self.seguiti_btn = QtWidgets.QPushButton(self.frame)
        self.seguiti_btn.setGeometry(QtCore.QRect(180, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.seguiti_btn.setFont(font)
        self.seguiti_btn.setObjectName("seguiti_btn")
        self.stackedWidget.addWidget(self.dashboard)
        self.horizontalLayout.addWidget(self.app)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dash.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_user_login.setText(_translate("MainWindow", "NOME UTENTE"))
        self.label_pass_login.setText(_translate("MainWindow", "PASSWORD"))
        self.login_btn.setText(_translate("MainWindow", "ACCEDI"))
        self.register_btn.setText(_translate("MainWindow", "REGISTRATI"))
        self.title_log.setText(_translate("MainWindow", "ACCEDI AL TUO PROFILO"))
        self.label.setText(_translate("MainWindow", "DISTRIBUTED  SOCIAL"))
        self.label_user_register.setText(_translate("MainWindow", "INSERISCI NOME UTENTE"))
        self.label_pass_register.setText(_translate("MainWindow", "INSERISCI UNA PASSWORD"))
        self.login_back_btn.setText(_translate("MainWindow", "ACCEDI"))
        self.register_new_btn.setText(_translate("MainWindow", "REGISTRATI"))
        self.title_reg.setText(_translate("MainWindow", "CREA UN NUOVO PROFILO"))
        self.min_max.setText(_translate("MainWindow", "(Min 4 - Max 10 caratteri)"))
        self.label_2.setText(_translate("MainWindow", "DISTRIBUTED  SOCIAL"))
        self.title_info_utenti_eventi.setText(_translate("MainWindow", "INFORMAZIONI UTENTE"))
        self.title_eventi.setText(_translate("MainWindow", "STORICO EVENTI"))
        self.cerca_btn.setText(_translate("MainWindow", "CERCA"))
        self.check_seguiti.setText(_translate("MainWindow", "SOLO UTENTI SEGUITI"))
        self.title_info_utenti.setText(_translate("MainWindow", "           INFORMAZIONI UTENTE"))
        self.title_msg_utenti.setText(_translate("MainWindow", "MESSAGGI UTENTE"))
        self.post_btn.setText(_translate("MainWindow", "PUBBLICA"))
        self.max_char.setText(_translate("MainWindow", "(Max 50 caratteri)"))
        self.title_bacheca.setText(_translate("MainWindow", "RESTA IN CONTATTO CON I TUOI AMICI SEGUITI"))
        self.mod_data_btn.setText(_translate("MainWindow", "MODIFICA"))
        self.combo_mod_dati.setItemText(0, _translate("MainWindow", "NOME"))
        self.combo_mod_dati.setItemText(1, _translate("MainWindow", "COGNOME"))
        self.combo_mod_dati.setItemText(2, _translate("MainWindow", "ETA"))
        self.combo_mod_dati.setItemText(3, _translate("MainWindow", "SESSO"))
        self.combo_mod_dati.setItemText(4, _translate("MainWindow", "NAZIONALITA"))
        self.combo_mod_dati.setItemText(5, _translate("MainWindow", "CITTA"))
        self.combo_mod_dati.setItemText(6, _translate("MainWindow", "HOBBY"))
        self.el_sel_msg.setText(_translate("MainWindow", "ELIMINA MESSAGGIO SELEZIONATO"))
        self.notifiche_btn.setText(_translate("MainWindow", "NOTIFICHE"))
        self.logout_btn.setText(_translate("MainWindow", "ESCI"))
        self.bacheca_btn.setText(_translate("MainWindow", "BACHECA"))
        self.profilo_dati_btn.setText(_translate("MainWindow", "PROFILO"))
        self.seguiti_btn.setText(_translate("MainWindow", "UTENTI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
