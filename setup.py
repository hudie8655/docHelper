# -*- coding: utf-8 -*-
#setup代码
from cx_Freeze import setup, Executable
executables = [
    Executable(
    script='MainFrmMy.py', #目标引用脚本
    base="win32gui",     #GUI程序需要隐藏控制台
    targetName = 'Writer.exe',#生成exe的名字
    icon = "icon/writer.ico" #生成exe的的图标
)]
