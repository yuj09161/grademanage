import os,subprocess,re

files=os.listdir()

header="# -\*- coding: utf-8 -\*-\r\n\r\n################################################################################\r\n## Form generated from reading UI file '.+.ui'\r\n##\r\n## Created by: Qt User Interface Compiler version 5.15.0\r\n##\r\n## WARNING! All changes made in this file will be lost when recompiling UI file!\r\n################################################################################\r\n\r\nfrom PySide2.QtCore import \(QCoreApplication, QDate, QDateTime, QMetaObject,\r\n    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt\)\r\nfrom PySide2.QtGui import \(QBrush, QColor, QConicalGradient, QCursor, QFont,\r\n    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,\r\n    QPixmap, QRadialGradient\)\r\nfrom PySide2.QtWidgets import \*\r\n\r\n\r\n"
header2="################################################################################\r\n## Form generated from reading UI file '.+.ui'\r\n##\r\n## Created by: Qt User Interface Compiler version 5.15.0\r\n##\r\n## WARNING! All changes made in this file will be lost when recompiling UI file!\r\n################################################################################\r\n\r\n"

a=''

k=0
for file in files:
    if os.path.splitext(file)[1]=='.ui':
        print(file,k)
        tmp=subprocess.run('pyside2-uic %s' %(file,),stdout=subprocess.PIPE).stdout.decode("utf-8")
        if k>0:
            a+=re.sub(header,'',tmp)
        else:
            a+=re.sub(header2,'',tmp)
        k+=1

with open('UI.py','w',encoding='utf-8',) as file:
    file.write(a)