from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import QPoint, pyqtSignal
from Item import Item

class ItemImage(QLabel):

	#Signal
	clicked = pyqtSignal(QLabel)

	def __init__(self, item):
		super().__init__()
		self.item = item
		self.initUI()

	def initUI(self):
		self.setFixedSize(64,64)

		self.setToolTip(self.item.name) 

		pixmap = QPixmap(self.item.icon)
		self.setPixmap(pixmap)

	def mousePressEvent(self, e):
		self.clicked.emit(self)

	def selected(self):
		new_pix = QPixmap(self.pixmap().size())
		new_pix.fill(QColor("#f0f0f0"))
		painter = QPainter(new_pix)
		painter.setOpacity(40 * 0.01)
		painter.drawPixmap(QPoint(), self.pixmap())
		painter.end()
		self.setPixmap(new_pix)

	def unselected(self):
		pixmap = QPixmap(self.item.icon)
		self.setPixmap(pixmap)