import sys
import unittest
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import *
import minesweeper

app = QApplication(sys.argv)

class PosTest(unittest.TestCase):
	
	def setUp(self):
		self.form = minesweeper.MainWindow()

	def test_reset_function(self):
	#Set square to true for all bools and to 3 for adjacent_n
		t = self.form.grid.itemAtPosition(0,0).widget()
		t.is_start = 1
		t.is_mine = 1
		t.adjacent_n = 3
		t. is_flagged = 1
		t.is_revealed = 1
	#Call reset 
		t.reset()
	#Ensure all variables have been reset to false/0
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)
		self.assertEqual(t.is_revealed,0)
	#Call reset
		t.reset()
	#Ensure all variables are still set to false/0
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)
		self.assertEqual(t.is_revealed,0)

	def test_right_click(self):
	#First, reset all variables to their default value (0 or False)
		t = self.form.grid.itemAtPosition(0,0).widget()
		t.reset()
	#Ensure reset_map() worked and that all values are set to 0 or FALSE
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)
		self.assertEqual(t.is_revealed,0)
	#Simulate right clicking on the square 
		QTest.mouseClick(t,Qt.RightButton)
	#Test to malke sure the only value that changed was is_flagged->true
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,1)
		self.assertEqual(t.is_revealed,0)
	#Reset everything again and ensure it was successful
		t.reset()
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)
		self.assertEqual(t.is_revealed,0)
	#Set is_flagged to true
		t.is_flagged = 1;
	#Simulate right clicking again
		QTest.mouseClick(t,Qt.RightButton)
	#Make sure nothing changed
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,1)
		self.assertEqual(t.is_revealed,0)





	def test_left_click(self):
	#First, reset all variables to their default value (0 or False)
		t = self.form.grid.itemAtPosition(0,0).widget()
		t.reset()
	#Ensure reset_map() worked and that all values are set to 0 or FALSE
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)
		self.assertEqual(t.is_revealed,0)
	#Simulate left clicking on the square
		QTest.mouseClick(t,Qt.LeftButton)
	#Test to make sure is_revealed->true and everything else stays false
		self.assertEqual(t.is_revealed,1)
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)
	#Simulate another left click
		QTest.mouseClick(t,Qt.LeftButton)
	#Test to ensure nothing changed
		self.assertEqual(t.is_revealed,1)
		self.assertEqual(t.is_start,0)
		self.assertEqual(t.is_mine,0)
		self.assertEqual(t.adjacent_n,0)
		self.assertEqual(t.is_flagged,0)



if __name__ == '__main__':
	unittest.main()
