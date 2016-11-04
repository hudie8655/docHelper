#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '将TargetOpinionMain python项目转换为exe文件'
__author__ = '皮'
__email__ = 'pipisorry@126.com'
"""
from PyInstaller.__main__ import run

if __name__ == '__main__':
    #opts = ['MainFrmMy.py', '-F']
    # opts = ['MainFrmMy.py', '-F', '-w']
    opts = ['MyDownloaderFrm.py', '-F', '-w', '--icon=writer.ico']#,'--upx-dir','upx308w']
    run(opts)