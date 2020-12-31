from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QPushButton
from ItemList import ItemList

class ListModifier(QScrollArea):
	""" List modifier """

	def __init__(self, parent=None):
		super().__init__(parent)
		self.initUI()

	def initUI(self):
		#itemsLayout
		self.itemsLayout = QVBoxLayout()

		#addItemBtn
		addItemBtn = QPushButton("+")
		addItemBtn.clicked.connect(self.addItem)

		#mainLayout
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(self.itemsLayout)
		mainLayout.addWidget(addItemBtn)
		self.setLayout(mainLayout)

		self.show()

	@profile
	def addItem(self, e):
		item = ItemList()
		self.itemsLayout.addWidget(item)

if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication
	app = QApplication(sys.argv)
	new = ListModifier()
	sys.exit(app.exec_())