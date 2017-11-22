# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont

__author__ = 'user'
class Highlighter(QSyntaxHighlighter):
    def __init__(self,parent=None ,*keywords):
        super(Highlighter, self).__init__(parent)


        foregroundList = [Qt.red,Qt.blue,Qt.green]
        #keywordFormat.setForeground(Qt.red)

        i=0
        self.highlightingRules=[]
        for k in keywords:
            keywordFormat = QTextCharFormat()
            keywordFormat.setBackground(Qt.yellow)
            keywordFormat.setFontWeight(QFont.Bold)
            keywordFormat.setForeground(foregroundList[i % 3])
            self.highlightingRules.append((k,keywordFormat ))
            i+=1
        #self.highlightingRules = [(pattern, keywordFormat) for pattern in keywords]


    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

