#!/usr/bin/env python3

import sys
from myfunc import myfunc

if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        from gui import gui
        from PyQt5.QtWidgets import QApplication
        app = QApplication(sys.argv)
        ex = gui.Example()
        sys.exit(app.exec_())
    if len(sys.argv[1:]) > 1:
        print('This script can only handle one input at a time.')
        input = input('Please enter a single number: ')
        output = myfunc.myfunc(input)
        print('{} squared is {}'.format(input, output))
    else:
        input = sys.argv[1]
        output = myfunc.myfunc(input)
        print('{} squared is {}'.format(input, output))
