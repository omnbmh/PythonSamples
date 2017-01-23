#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'c8d8z8@gmail.com'

import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

import Tkinter

def get_main_window():
    '''Create main window.'''
    return Tkinter.Tk()

def set_main_window_size(root):
    root.geometry('600x480')

def create_label(root):
    return Tkinter.Label(root, text = '设置', fg='red')
    
def create_text(root):

def label_pack(label):
    label.pack()
def main_loop(root):
    root.mainloop()

def main():
    root = get_main_window()
    set_main_window_size(root)
    label = create_label(root)
    label_pack(label)
    main_loop(root)

if __name__ == '__main__':
    main()



