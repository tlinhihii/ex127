# Form implementation generated from reading ui file 'D:\Python\pycharm\KTLT\ex127\MainWindow127.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(290, 60, 451, 291))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButtonRefresh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRefresh.setFont(font)
        self.pushButtonRefresh.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/2849811_refresh_arrows_multimedia_media_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonRefresh.setIcon(icon)
        self.pushButtonRefresh.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.pushButtonSortPrice = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSortPrice.setGeometry(QtCore.QRect(30, 180, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSortPrice.setFont(font)
        self.pushButtonSortPrice.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/4781834_filter_filters_funnel_list_sort_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSortPrice.setIcon(icon1)
        self.pushButtonSortPrice.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonSortPrice.setObjectName("pushButtonSortPrice")
        self.pushButtonReduce = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonReduce.setGeometry(QtCore.QRect(30, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonReduce.setFont(font)
        self.pushButtonReduce.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/8666819_minimize_2_reduce_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonReduce.setIcon(icon2)
        self.pushButtonReduce.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonReduce.setObjectName("pushButtonReduce")
        self.pushButtonStatistic = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonStatistic.setGeometry(QtCore.QRect(790, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonStatistic.setFont(font)
        self.pushButtonStatistic.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/7030121_statistic_analytics_ui basic_graph_app_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonStatistic.setIcon(icon3)
        self.pushButtonStatistic.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonStatistic.setObjectName("pushButtonStatistic")
        self.pushButtonUSD = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonUSD.setGeometry(QtCore.QRect(790, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonUSD.setFont(font)
        self.pushButtonUSD.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/172529_price_usd_tag_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonUSD.setIcon(icon4)
        self.pushButtonUSD.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonUSD.setObjectName("pushButtonUSD")
        self.pushButtonAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(790, 180, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/3669476_add_circle_ic_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAdd.setIcon(icon5)
        self.pushButtonAdd.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(410, 380, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 202, 246, 255), stop:1 rgba(255, 255, 255, 255));")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:\\Python\\pycharm\\KTLT\\ex127\\images/1564502_basket_delete_remove_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDelete.setIcon(icon6)
        self.pushButtonDelete.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nguyễn Mai Thảo Linh"))
        self.pushButtonRefresh.setText(_translate("MainWindow", "Refresh Data"))
        self.pushButtonSortPrice.setText(_translate("MainWindow", "Sort by Price"))
        self.pushButtonReduce.setText(_translate("MainWindow", "Reduce by Symbol"))
        self.pushButtonStatistic.setText(_translate("MainWindow", "Statistics"))
        self.pushButtonUSD.setText(_translate("MainWindow", "USD Column"))
        self.pushButtonAdd.setText(_translate("MainWindow", "Add New Row"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
