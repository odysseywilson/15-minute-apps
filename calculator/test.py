import sys
import unittest
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import *
import calculator

app = QApplication(sys.argv)

class TestCalc(unittest.TestCase):
	
	self.pushButton_ac.pressed.connect(self.reset)
	def setUp(self):
        	self.form = calculator.MainWindow()
	def test_ac(self):
		# store the state of the ac button
		ac_state_before = self.form.pushButton_ac.isChecked()
		# geting the AC botton 
		ac_button = self.form.layout().itemAt(2).widget().widgetForAction(self.form.pushButton_ac)
		QTest.mouseClick(ac_button, Qt.LeftButton)
		button_state_after_left = self.form.pushButton_ac.isChecked()
		# assert that the button state is not the same before and after the click
		self.assertNotEqual(button_state_before, button_state_after_left)
		# right click the button
		QTest.mouseClick(ac_button, Qt.RightButton)
		# store the state of the ac button
		button_state_after_right = self.form.pushButton_ac.isChecked()
		# assert that the button state is not the same before and after the click
		self.assertEqual(button_state_after_left, button_state_after_right)
		

	




if __name__ == '__main__':
	unittest.main()
