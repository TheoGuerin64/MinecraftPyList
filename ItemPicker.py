from PyQt5.QtWidgets import QDialog, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QScrollArea, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from ItemImage import ItemImage
from Item import Item

class ItemPicker(QDialog):
	""" A dialog to choose an item

	Attributes
	----------
	gridMaxWith : int = 10
		The item width max
	itemList : list = Item.list()
		List of items
	itemNameList : list = Item.nameList()
		List of item names
	selectedItem : ItemImage = None
		The item of the grid selected

	Methods
	-------
	__init__(self, parent)
		Constructs all the necessary attributes for the ItemPicker dialog

		Parameters
		----------
		parent : QWidget
			Define the parent of the ItemPicker dialog

	getValue()
		Return the item selected

		Returns
     	-------
		item : Item
	 """

	def __init__(self, parent):
		super().__init__(parent, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

		self.gridMaxWith = 10
		self.itemList = Item.list()
		self.itemNameList = Item.nameList()
		self.selectedItem = None

		self.initUI()

	def initUI(self):
		self.setWindowTitle("Item picker")
		self.setWindowIcon(QIcon("Assets\\Items\\grass_block.png"))
		self.setFixedSize(753 ,500)

		#seach bar
		self.searchBar = QLineEdit()
		self.searchBar.textChanged.connect(self.searchBarUpdate)

		#item list
		self.grid = QGridLayout()
		self.grid.setSizeConstraint(QGridLayout.SetFixedSize)

		gridWid = QWidget()
		gridWid.setLayout(self.grid)

		scroll = QScrollArea()
		scroll.setWidgetResizable(True)
		scroll.setWidget(gridWid)

		#buttons
		addBtn = QPushButton("Add")
		addBtn.clicked.connect(self.choose)

		cancelBtn = QPushButton("Cancel")
		cancelBtn.clicked.connect(self.reject)

		btnLayout = QHBoxLayout()
		btnLayout.addWidget(addBtn)
		btnLayout.addWidget(cancelBtn)

		#main layout
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.searchBar)
		mainLayout.addWidget(scroll)
		mainLayout.addLayout(btnLayout)
		self.setLayout(mainLayout)

		self.updateGrid(self.itemList)

	def updateGrid(self, itemList):
		if self.selectedItem != None:
			focusedName = self.selectedItem.item.name

		#delete all widgets in the grid
		for i in range(self.grid.count()):
			widToRemove = self.grid.itemAt(0).widget()
			widToRemove.setParent(None)
			widToRemove.deleteLater()

		#add new list of items
		i = 0
		for item in itemList:
			itemWid = ItemImage(item)
			itemWid.clicked.connect(self.itemChoosed)
			self.grid.addWidget(itemWid, i/self.gridMaxWith, i%self.gridMaxWith)
			if self.selectedItem != None and item.name == focusedName:
				self.selectedItem = itemWid
				self.selectedItem.selected()
			i += 1

	def searchBarUpdate(self, e):
		self.updateGrid([Item(name) for name in self.itemNameList if self.searchBar.text().lower() in name.lower()])

	def itemChoosed(self, event):
		if self.selectedItem != None:
			self.selectedItem.unselected()
		self.selectedItem = event
		self.selectedItem.selected()

	def choose(self):
		if self.selectedItem != None:
			self.accept()

	def getValue(self):
		return self.selectedItem.item