from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

class ItemImage(QLabel):

	# Signal
	clicked = pyqtSignal(QLabel)

	def __init__(self, item):
		super().__init__()
		self.item = item
		self.initUI()

	def initUI(self):
		self.setFixedSize(64,64)

		pixmap = QPixmap(self.item.icon)
		self.setPixmap(pixmap)

	def mousePressEvent(self, e):
		self.clicked.emit(self)