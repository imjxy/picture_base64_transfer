import base64
from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader


class Transfer:
    def __init__(self):
        self.ui = QUiLoader().load('base64_turn.ui')
        self.ui.btn_select.clicked.connect(self.open)
        self.ui.btn_start.clicked.connect(self.transfer)
        self.pic_path = ''

    def open(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的图片",  # 标题
            r"d:\\data",  # 起始目录
            "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        if filePath == None:
            QMessageBox.information(self, '提示', '文件为空，请重新操作')
        else:
            self.pic_path = filePath
            pic=QtGui.QPixmap(self.pic_path)
            self.ui.qlb_pic.setPixmap(pic)
            #self.ui.qlb_pic.resize(pic.width(), pic.height())
        self.ui.le_select.setText(self.pic_path)

    def transfer(self):
        f = open(self.pic_path, 'rb')  # 二进制方式打开图文件
        ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        self.ui.tb_base64.setText(str(ls_f))

app = QApplication([])
changer = Transfer()
changer.ui.show()
app.exec_()