from PyQt5.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from ItemPickerItem import ItemPickerItem
from Item import Item

class ItemPicker(QDialog):
	def __init__(self, parent):
		super().__init__(parent, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

		self.itemList = Item.list()
		self.itemNameList = Item.nameList()

		self.initUI()

	def initUI(self):
		self.setWindowTitle("Item picker")
		self.setWindowIcon(QIcon("Assets\\Items\\grass_block.png"))
		self.resize(728 ,500)

		# Seach bar
		self.searchBar = QLineEdit()
		self.searchBar.textChanged.connect(self.searchBarUpdate)

		# Item list
		self.list = QListWidget()
		self.list.setViewMode(QListWidget.IconMode)
		self.list.setResizeMode(QListWidget.Adjust)
		self.list.setIconSize(QSize(32, 32))

		for item in self.itemList:
			self.list.addItem(ItemPickerItem(item))

		# Buttons
		addBtn = QPushButton("Add")
		addBtn.clicked.connect(self.add)

		cancelBtn = QPushButton("Cancel")
		cancelBtn.clicked.connect(self.reject)

		btnLayout = QHBoxLayout()
		btnLayout.addWidget(addBtn)
		btnLayout.addWidget(cancelBtn)

		# Main layout
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.searchBar)
		mainLayout.addWidget(self.list)
		mainLayout.addLayout(btnLayout)
		self.setLayout(mainLayout)

	def updateGrid(self, itemList):
		for i in range(1120):
			self.list.item(i).setHidden(not(self.list.item(i).item.name in itemList))

	def searchBarUpdate(self, e):
		self.updateGrid([name for name in self.itemNameList if self.searchBar.text().lower() in name.lower()])

	def add(self):
		if self.list.selectedItems() != []:
			self.accept()

	def getValue(self):
		return self.list.selectedItems()[0].item