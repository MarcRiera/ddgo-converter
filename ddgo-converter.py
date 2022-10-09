#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from gui.main import MainWindow

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_view = MainWindow(None)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
