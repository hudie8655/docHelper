# -*- coding: utf-8 -*-
from PyQt5.uic.properties import QtGui

__author__ = 'user'
import logging
import sqlite3
from PyQt5.QtGui import QStandardItemModel, QTextCursor, QTextCharFormat, QTextDocument,QIcon#,QPixmap, QPalette
import pickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QFileDialog#,QDialog,QMessageBox
#from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtCore import Qt, QEvent#, QFile,QTextStream
from mainFrm import Ui_MainWindow

import zipfile
from testOfflineDB import News

logging.basicConfig(level=logging.INFO)

class MainFrmMy(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.content_lose_focus() #设置初始界面比例



        self.model = createNewsModel(self)
        self.resulttreeView.setModel(self.model)
        self.resulttreeView.selectionModel().selectionChanged.connect(self.updateActions)

        self.searchlineEdit.returnPressed.connect(lambda: self.search('title'))
        self.pushButton.clicked.connect(lambda: self.search('title'))
        self.searchContentButton.clicked.connect(lambda: self.search('content'))
        self.contenttextEdit.installEventFilter(self)
        #self.contenttextEdit.enterEvent.connect(self.content_get_focus)

        self.loadOfflineAction.triggered.connect(self.open)

    def content_get_focus(self):
        w = self.geometry().width()
        self.splitter.setSizes([w/4,3*w/4])
        #TODO 调整大小 根据焦点
        #TODO 根据内容搜索
        #TODO 不同新闻放到不同的表里

    def content_lose_focus(self):
        w = self.geometry().width()
        self.splitter.setSizes([3*w/4,w/4])

    def eventFilter(self, obj, e):
        if obj == self.contenttextEdit:
            if e.type() == QEvent.FocusIn:
                self.content_get_focus()
                return False
            elif e.type() == QEvent.FocusOut:
                self.content_lose_focus()
                return False
        return False


    def open(self):
        filename,_ = QFileDialog.getOpenFileName()#None,'Choose File','e:\\','.txt')
        #with zipfile.ZipFile('news.zip','r',compression=zipfile.ZIP_BZIP2) as myzip:#zipfile.ZipFile.open(filename,'r') as f:
        #    myzip.extractall()
        #TODO 不能这么来，临时的
        with open(filename,'rb') as f:
            try:
                conn = sqlite3.connect('test.db')
                #x=[(news['name'],news['content'],'人民日报',news['date'],news['ban']) for news in json]

                while True:
                    news = pickle.load(f)
                    conn.execute("INSERT INTO NEWS (TITLE,CONTENT,TYPE,DATE,BANCI)   VALUES (?,?,?,?,?)",(news.title,news.content,news.type,news.date,news.banci))
                    conn.commit()
                    logging.info(str(news.title))
                    self.statusbar.showMessage(str(news.title))#('导入%d%%' %(i/len(newList)*100))
            except EOFError:
                self.statusbar.showMessage('导入完成')
            finally:
                 conn.close()
        return


    def updateActions(self):
        hasCurrent = self.resulttreeView.selectionModel().currentIndex().isValid()
        if hasCurrent:
            index = self.resulttreeView.selectionModel().currentIndex()
            title=self.resulttreeView.selectionModel().currentIndex().sibling(index.row(),0).data()
            self.handlelist(title)
           # if self.resulttreeView.selectionModel().currentIndex().parent().isValid():
                #title = self.resulttreeView.selectionMode().itemFromIndex(index)

                #self.statusBar().showMessage("Position: (%d,%d)" % (row, column))
           # else:
               # self.statusBar().showMessage("Position: (%d,%d) in top level" % (row, column))


    def search(self,s='title'):
        #TODO 清空结果 不知道为什么clear不行，难道把关联关系一并清除了？
        self.model.removeRows(0,self.model.rowCount())
        keywords=self.searchlineEdit.text().split()
        if keywords:
            sql='SELECT Num,TITLE,TYPE ,DATE ,BANCI FROM NEWS WHERE '+s+' like \'%'+str('%\' and '+s+' like \'%').join(keywords)+'%\' order by date'

            self.statusbar.showMessage('正在查询'+str(keywords))
            conn = sqlite3.connect('test.db')
            cur=conn.execute(sql)
            #self.resultlistView.
            for row in cur:
                logging.info(str(row[0])+'\t'+'\t'.join(row[1:]))
                addNews(self.model,*row)
            self.statusbar.showMessage('完成查询'+str(keywords)+sql)

            for column in range(self.model.columnCount()):
                self.resulttreeView.resizeColumnToContents(column)


    def handlelist(self,title):
        conn = sqlite3.connect('test.db')
        rows=conn.execute("SELECT CONTENT FROM NEWS WHERE Num=\'"+str(title)+'\'')
        for row in rows:
            self.contenttextEdit.setPlainText(row[0])

        for i,word in enumerate(self.searchlineEdit.text().split()):
            self.mark_keywords(word,i)

    def mark_keywords(self,keyword,i):
        search_text = keyword

        document = self.contenttextEdit.document()
        found = False
        highlight_cursor = QTextCursor(document)
        cursor = QTextCursor(document)
        #cursor.setPosition(QTextCursor.Start)
        #highlight_cursor.setPosition(QTextCursor.Start)


        cursor.beginEditBlock()

        color_format = QTextCharFormat(highlight_cursor.charFormat())
        color_format.setForeground(Qt.red)
        color_format.setBackground(Qt.yellow)
        while (not highlight_cursor.isNull() and not highlight_cursor.atEnd()):
            #查找指定的文本，匹配整个单词
            #if i%2:
             #   highlight_cursor = document.find(search_text, highlight_cursor, QTextDocument.FindBackward)
            #else:
            highlight_cursor = document.find(search_text, highlight_cursor, QTextDocument.FindWholeWords)
            if (not highlight_cursor.isNull()):
                if(not found):
                    found = True
                highlight_cursor.mergeCharFormat(color_format)

        cursor.endEditBlock()


def addNews(model, *args):
    model.insertRow(0)
    for i,arg in enumerate(args):
        model.setData(model.index(0, i), str(arg).strip())



def createNewsModel(parent):
    model = QStandardItemModel(0, 5, parent)

    model.setHeaderData(0, Qt.Horizontal, "编号")
    model.setHeaderData(1, Qt.Horizontal, "标题")
    model.setHeaderData(2, Qt.Horizontal, "报纸")
    model.setHeaderData(3, Qt.Horizontal, "日期")
    model.setHeaderData(4, Qt.Horizontal, "版面")
    return model

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainFrmMy()
    win.setWindowIcon(QIcon('icon/writer.ico'))
    win.showMaximized()
    sys.exit(app.exec_())

