from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from ItemList import ItemList

class ListModifier(QScrollArea):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.initUI()

	def initUI(self):
		# ItemsLayout
		self.itemsLayout = QVBoxLayout()
		self.itemsLayout.setAlignment(Qt.AlignAbsolute)

		# AddItemBtn
		addItemBtn = QPushButton("+")
		addItemBtn.clicked.connect(self.addItem)

		# MainLayout
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(self.itemsLayout)
		mainLayout.addWidget(addItemBtn, 0, Qt.AlignBottom)

		self.setLayout(mainLayout)

		self.show()

	def addItem(self):
		item = ItemList()
		self.itemsLayout.addWidget(item)

	def getValue(self):
		list = []
		for i in range(self.itemsLayout.count()):
			list.append(self.itemsLayout.itemAt(i).widget().getValue())
		return list