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
        button_state_before = self.form.bold_action.isChecked()

        # get the bold button from the form
        bold_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.bold_action)

        # left click the button
        QTest.mouseClick(bold_button, Qt.LeftButton)

        # store the state of the bold button
        button_state_after = self.form.bold_action.isChecked()

        # assert that the button state is not the same before and after the click
        self.assertNotEqual(button_state_before, button_state_after)


    def test_italic_button(self):
        # store the state of the italic button
        button_state_before = self.form.italic_action.isChecked()

        # get the italic button from the form
        italic_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.italic_action)

        # left click the button
        QTest.mouseClick(italic_button, Qt.LeftButton)

        # store the state of the italic button
        button_state_after = self.form.italic_action.isChecked()

        # assert that the button state is not the same before and after the click
        self.assertNotEqual(button_state_before, button_state_after)


    def test_underline_button(self):
        # store the state of the underline button
        button_state_before = self.form.underline_action.isChecked()

        # get the underline button from the form
        underline_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.underline_action)

        # left click the button
        QTest.mouseClick(underline_button, Qt.LeftButton)

        # store the state of the underline button
        button_state_after = self.form.underline_action.isChecked()

        # assert that the button state is not the same before and after the click
        self.assertNotEqual(button_state_before, button_state_after)
    
    
if __name__ == '__main__':
    unittest.main()
