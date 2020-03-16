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
        button_state_after_left = self.form.bold_action.isChecked()
        # assert that the button state is not the same before and after the click
        self.assertNotEqual(button_state_before, button_state_after_left)
        # right click the button
        QTest.mouseClick(bold_button, Qt.RightButton)
        # store the state of the bold button
        button_state_after_right = self.form.bold_action.isChecked()
        # assert that the button state is not the same before and after the click
        self.assertEqual(button_state_after_left, button_state_after_right)

    def test_italic_button(self):
        # store the state of the italic button
        button_state_before = self.form.italic_action.isChecked()
        # get the italic button from the form
        italic_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.italic_action)
        # left click the button
        QTest.mouseClick(italic_button, Qt.LeftButton)
        # store the state of the italic button
        button_state_after_left = self.form.italic_action.isChecked()
        # assert that the button state is not the same before and after the click
        self.assertNotEqual(button_state_before, button_state_after_left)
        # right click the button
        QTest.mouseClick(italic_button, Qt.RightButton)
        # store the state of the italic button
        button_state_after_right = self.form.italic_action.isChecked()
        # assert that the button state is not the same before and after the click
        self.assertEqual(button_state_after_left, button_state_after_right)

    def test_underline_button(self):
        # store the state of the underline button
        button_state_before = self.form.underline_action.isChecked()
        # get the underline button from the form
        underline_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.underline_action)
        # left click the button
        QTest.mouseClick(underline_button, Qt.LeftButton)
        # store the state of the underline button
        button_state_after_left = self.form.underline_action.isChecked()
        # assert that the button state is not the same before and after the click
        self.assertNotEqual(button_state_before, button_state_after_left)
        # right click the button
        QTest.mouseClick(underline_button, Qt.RightButton)
        # store the state of the underline button
        button_state_after_right = self.form.underline_action.isChecked()
        # assert that the button state is not the same before and after the click
        self.assertEqual(button_state_after_left, button_state_after_right)

    def test_alignl_button(self):
        # get the alignment buttons from the form
        alignl_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignl_action)
        alignc_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignc_action)
        alignr_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignr_action)
        alignj_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignj_action)
        # left click the alignl button
        QTest.mouseClick(alignl_button, Qt.LeftButton)
        # assert that only the correct setting is enabled
        self.assertEqual(self.form.alignl_action.isChecked(), True)
        self.assertEqual(self.form.alignc_action.isChecked(), False)
        self.assertEqual(self.form.alignr_action.isChecked(), False)
        self.assertEqual(self.form.alignj_action.isChecked(), False)

    def test_alignc_button(self):
        # get the alignment buttons from the form
        alignl_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignl_action)
        alignc_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignc_action)
        alignr_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignr_action)
        alignj_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignj_action)
        # left click the alignc button
        QTest.mouseClick(alignc_button, Qt.LeftButton)
        # assert that only the correct setting is enabled
        self.assertEqual(self.form.alignl_action.isChecked(), False)
        self.assertEqual(self.form.alignc_action.isChecked(), True)
        self.assertEqual(self.form.alignr_action.isChecked(), False)
        self.assertEqual(self.form.alignj_action.isChecked(), False)

    def test_alignr_button(self):
        # get the alignment buttons from the form
        alignl_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignl_action)
        alignc_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignc_action)
        alignr_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignr_action)
        alignj_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignj_action)
        # left click the alignr button
        QTest.mouseClick(alignr_button, Qt.LeftButton)
        # assert that only the correct setting is enabled
        self.assertEqual(self.form.alignl_action.isChecked(), False)
        self.assertEqual(self.form.alignc_action.isChecked(), False)
        self.assertEqual(self.form.alignr_action.isChecked(), True)
        self.assertEqual(self.form.alignj_action.isChecked(), False)

    def test_alignj_button(self):
        # get the alignment buttons from the form
        alignl_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignl_action)
        alignc_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignc_action)
        alignr_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignr_action)
        alignj_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.alignj_action)
        # left click the alignj button
        QTest.mouseClick(alignj_button, Qt.LeftButton)
        # assert that only the correct setting is enabled
        self.assertEqual(self.form.alignl_action.isChecked(), False)
        self.assertEqual(self.form.alignc_action.isChecked(), False)
        self.assertEqual(self.form.alignr_action.isChecked(), False)
        self.assertEqual(self.form.alignj_action.isChecked(), True)

if __name__ == '__main__':
    unittest.main()
