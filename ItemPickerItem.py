from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QIcon

class ItemPickerItem(QListWidgetItem):
	def __init__(self, item):
		super().__init__()

		self.item = item

		self.initUI()

	def initUI(self):
		self.setIcon(QIcon(self.item.icon))
		self.setToolTip(self.item.name)