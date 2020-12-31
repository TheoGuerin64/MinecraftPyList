from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpinBox, QAbstractSpinBox, QPushButton, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from ExtendedComboBox import ExtendedComboBox
from itemAssetsList import itemAssetsList

class ItemList(QWidget):
	""" A widget made for being used in a list and get the number of item and the item name wanted

	Parameters
	----------
	parent : QWidget = None
		the parent of self
	item : str = "Grass Block"
		default item
	nb : int = 0
		default number of items
	modifyMode : bool = True
		if False the close button is hidden and the item can't be modified

	Attributes
	----------
	maxRange : int = 999999
		max range of the number of items

	Methods
	-------

	getItem()
		return the item name

		Returns
     	-------
		item : str
			name of item

	getNb()
		return the number of items

		Returns
     	-------
		nb : int
			number of items
	 """

	#Attributes
	maxRange = 999999

	def __init__(self, parent=None, item="Grass Block", nb=0, modifyMode=True):
		super().__init__(parent)
		self.modifyMode = modifyMode

		self.initUI()

		#Load parameters
		self.itemList.setCurrentIndex(self.itemList.findText(item))
		self.itemNb.setValue(nb)
		if not self.modifyMode:
			self.itemList.setEnabled(False)
			self.itemNb.setMaximum(nb)

	def initUI(self):
		if self.modifyMode:
			self.setFixedSize(405,107)
		else:
			self.setFixedSize(405,88)

		#Item list
		self.itemList = ExtendedComboBox()
		self.itemList.setStyleSheet(":disabled { color: black; }")
		for item in itemAssetsList:
			icon = QIcon()
			icon.addPixmap(QPixmap(itemAssetsList[item]), QIcon.Active)
			icon.addPixmap(QPixmap(itemAssetsList[item]), QIcon.Disabled)
			self.itemList.addItem(icon, item)

		#Number of items
		self.itemNb = QSpinBox()
		self.itemNb.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.itemNb.setAlignment(Qt.AlignCenter)
		self.itemNb.setFixedSize(50,25)
		self.itemNb.setRange(0, self.maxRange)

		#minusBtn
		minusBtn = QPushButton("-")
		minusBtn.setStyleSheet("QPushButton {border:0px}")
		minusBtn.clicked.connect(self.minusNb)

		#addBtn
		addBtn = QPushButton("+")
		addBtn.setStyleSheet("QPushButton {border:0px}")
		addBtn.clicked.connect(self.addNb)

		#itemNbLayout
		itemNbLayout = QHBoxLayout()
		itemNbLayout.addWidget(minusBtn)
		itemNbLayout.addWidget(self.itemNb)
		itemNbLayout.addWidget(addBtn)

		#itemNbPerClick
		self.itemNbPerClick = QComboBox()
		self.itemNbPerClick.addItem("1")
		self.itemNbPerClick.addItem("16 (quarter stack)")
		self.itemNbPerClick.addItem("32 (half-stack)")
		self.itemNbPerClick.addItem("64 (stack)")
		self.itemNbPerClick.addItem("128 (double stack)")
		self.itemNbPerClick.addItem("1728 (chest)")
		self.itemNbPerClick.addItem("3456 (double chest)")

		#nbLayout
		nbLayout = QVBoxLayout()
		nbLayout.addLayout(itemNbLayout)
		nbLayout.addWidget(self.itemNbPerClick)

		#destroyBtn
		destroyBtn = QPushButton("x")
		destroyBtn.setStyleSheet("QPushButton {margin:0px; border:0px;}")
		destroyBtn.clicked.connect(self.destroy)

		#contentLayout
		contentLayout = QHBoxLayout()
		contentLayout.addWidget(self.itemList)
		contentLayout.addLayout(nbLayout)

		#mainLayout
		mainLayout = QVBoxLayout()
		if self.modifyMode:
			mainLayout.addWidget(destroyBtn, 0, Qt.AlignRight)
		mainLayout.addLayout(contentLayout)
		self.setLayout(mainLayout)

	def minusNb(self):
		self.itemNb.setValue(self.itemNb.value() - [1,16,32,64,128,1728,3456][self.itemNbPerClick.currentIndex()])

	def addNb(self):
		self.itemNb.setValue(self.itemNb.value() + [1,16,32,64,128,1728,3456][self.itemNbPerClick.currentIndex()])

	def destroy(self):
		self.deleteLater()

	def getItem(self):
		return self.itemList.currentText()

	def getNb(self):
		self.itemNb.value()