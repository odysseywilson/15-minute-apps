import sys
import unittest

from PyQt5.QtGui import *
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import wordprocessor 

app = QApplication(sys.argv)

class AppTest(unittest.TestCase):
    def setUp(self):
        self.form = wordprocessor.MainWindow()

    def test_bold_button(self):
        # store the state of the bold button
        bold_before = self.form.bold_action.isChecked()

        # get the bold button from the form
        bold_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.bold_action)

        # left click the button
        QTest.mouseClick(bold_button, Qt.LeftButton)

        # store the state of the bold button
        bold_after = self.form.bold_action.isChecked()

        # assert that the button state is not the same before and after the click
        self.assertNotEqual(bold_before, bold_after)

if __name__ == '__main__':
    unittest.main()
