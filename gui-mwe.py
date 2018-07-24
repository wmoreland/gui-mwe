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
    else:
        print('sys.argv was more than 0')
        print()
