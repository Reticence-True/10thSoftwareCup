# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vdoplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer):
        VideoPlayer.setObjectName("VideoPlayer")
        VideoPlayer.resize(962, 631)
        self.video = QVideoWidget(VideoPlayer)
        self.video.setGeometry(QtCore.QRect(1, 1, 960, 540))
        self.video.setStyleSheet("QWidget{\n"
"    background-color: #fff;\n"
"}")
        self.video.setObjectName("video")
        self.play = QtWidgets.QPushButton(VideoPlayer)
        self.play.setGeometry(QtCore.QRect(822, 556, 61, 61))
        self.play.setStyleSheet("QPushButton{\n"
"   ./dist/X-Trace/ border:none;\n"
"    background-image:url(./images/play.png);\n"
"}\n"
"QPushButton::hover{\n"
"    background-image:url(./images/playhighlight.png);\n"
"}")
        self.play.setText("")
        self.play.setIconSize(QtCore.QSize(50, 50))
        self.play.setObjectName("play")
        self.pause = QtWidgets.QPushButton(VideoPlayer)
        self.pause.setGeometry(QtCore.QRect(826, 560, 51, 51))
        self.pause.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-image:url(./dist/X-Trace/images/pause.png);\n"
"}\n"
"QPushButton::hover{\n"
"    background-image:url(./dist/X-Trace/images/pausehighlight.png);\n"
"}")
        self.pause.setText("")
        self.pause.setIconSize(QtCore.QSize(50, 50))
        self.pause.setObjectName("pause")
        self.progress = QtWidgets.QSlider(VideoPlayer)
        self.progress.setGeometry(QtCore.QRect(176, 572, 611, 31))
        self.progress.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.progress.setStyleSheet("QSlider::groove{\n"
"border: 1px solid #ff0000; /* 边框颜色 */\n"
"height: 10px; /* 整体高度 */\n"
"margin: 0px 0; /* 0px 设置已划过的地方高度, \"0\" 距离父控件的距离*/\n"
"}\n"
"\n"
"QSlider::handle{\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"border: 1px solid #5c5c5c; /*边框*/\n"
"width: 18px;\n"
"margin: -3px 0; /*滑块大小设置*/\n"
"border-radius: 3px; /* 圆角设置 */\n"
"background-color: #fe0000;\n"
"cursor:\n"
"}\n"
"\n"
"/* 已划过的设置*/\n"
"QSlider::sub-page:horizontal\n"
"{\n"
"border: 1px solid #ff0000; /* 边框颜色 */\n"
"background:#ffaa50;\n"
"border-radius: 3px;\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"")
        self.progress.setPageStep(5)
        self.progress.setProperty("value", 0)
        self.progress.setOrientation(QtCore.Qt.Horizontal)
        self.progress.setObjectName("progress")
        self.subtime = QtWidgets.QLabel(VideoPlayer)
        self.subtime.setGeometry(QtCore.QRect(128, 578, 46, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.subtime.setFont(font)
        self.subtime.setObjectName("subtime")
        self.alltime = QtWidgets.QLabel(VideoPlayer)
        self.alltime.setGeometry(QtCore.QRect(81, 578, 40, 19))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.alltime.setFont(font)
        self.alltime.setObjectName("alltime")
        self.label = QtWidgets.QLabel(VideoPlayer)
        self.label.setGeometry(QtCore.QRect(121, 580, 8, 15))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(VideoPlayer)
        QtCore.QMetaObject.connectSlotsByName(VideoPlayer)

    def retranslateUi(self, VideoPlayer):
        _translate = QtCore.QCoreApplication.translate
        VideoPlayer.setWindowTitle(_translate("VideoPlayer", "视频"))
        self.play.setToolTip(_translate("VideoPlayer", "点击以开始"))
        self.pause.setToolTip(_translate("VideoPlayer", "点击以暂停"))
        self.subtime.setText(_translate("VideoPlayer", "00:00"))
        self.alltime.setText(_translate("VideoPlayer", "00:00"))
        self.label.setText(_translate("VideoPlayer", "/"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
