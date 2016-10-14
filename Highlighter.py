# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont

__author__ = 'user'
class Highlighter(QSyntaxHighlighter):
    def __init__(self,parent=None ,*keywords):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.red)
        keywordFormat.setBackground(Qt.yellow)
        keywordFormat.setFontWeight(QFont.Bold)

        self.highlightingRules = [(pattern, keywordFormat)
                for pattern in keywords]


    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

