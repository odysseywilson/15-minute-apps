
from FILE import MAIN_CLASS
#ex.
#from paint import Canvas

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import *

import os
import random
import types

import unittest

app = QApplication([])


class functionTest(unittest.TestCase):
	def setUp(self):
		self.widget = MAIN_CLASS()

	def test_functionName(self):
		#test code

		#basic assertion example
		assertEquals(1,1)

		#PyQtTest's QTest allows for testing of clicking, etc.
		#QTest.mouseClick(thing_to_click, Qt.LeftButton)
		#run other assertions after the click

		# I found a good set of code showing an example of testing a PyQt application
		# https://bitbucket.org/jmcgeheeiv/pyqttestexample/src/default/src/


if __name__ == '__main__':
	unittest.main()