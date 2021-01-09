from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpinBox, QAbstractSpinBox, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from ItemPicker import ItemPicker
from ItemImage import ItemImage
from Item import Item

class ItemList(QWidget):
	def __init__(self, parent, item=Item()):
		super().__init__()

		self.parent = parent
		self.item = item

		self.initUI()

	def initUI(self):
		self.setFixedSize(435,85)

		#Item
		self.itemImage = ItemImage(self.item)
		self.itemImage.clicked.connect(self.itemChoose)

		self.itemText = QLabel(self.item.name)
		self.itemText.setMinimumWidth(170)
		self.itemText.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.itemLayout = QHBoxLayout()
		self.itemLayout.addWidget(self.itemImage)
		self.itemLayout.addWidget(self.itemText)

		#Number of items
		self.itemNb = QSpinBox()
		self.itemNb.valueChanged.connect(self.nbChanged)
		self.itemNb.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.itemNb.setAlignment(Qt.AlignCenter)
		self.itemNb.setFixedSize(50,25)
		self.itemNb.setRange(0, 999999)
		self.itemNb.setValue(self.item.nb)

		#MinusBtn
		minusBtn = QPushButton("-")
		minusBtn.setStyleSheet("border:0px;")
		minusBtn.clicked.connect(self.minusNb)

		#AddBtn
		addBtn = QPushButton("+")
		addBtn.setStyleSheet("border:0px;")
		addBtn.clicked.connect(self.addNb)

		#ItemNbLayout
		itemNbLayout = QHBoxLayout()
		itemNbLayout.addWidget(minusBtn)
		itemNbLayout.addWidget(self.itemNb)
		itemNbLayout.addWidget(addBtn)

		#ItemNbPerClick
		self.itemNbPerClick = QComboBox()
		self.itemNbPerClick.addItem("1")
		self.itemNbPerClick.addItem("16 (quarter stack)")
		self.itemNbPerClick.addItem("32 (half-stack)")
		self.itemNbPerClick.addItem("64 (stack)")
		self.itemNbPerClick.addItem("128 (double stack)")
		self.itemNbPerClick.addItem("1728 (chest)")
		self.itemNbPerClick.addItem("3456 (double chest)")
		self.itemNbPerClick.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
		self.itemNbPerClick.setFixedWidth(110)

		#NbLayout
		nbLayout = QVBoxLayout()
		nbLayout.addLayout(itemNbLayout)
		nbLayout.addWidget(self.itemNbPerClick)

		#DestroyBtn
		destroyBtn = QPushButton()
		destroyBtn.setIcon(QIcon("Assets/remove.png"))
		destroyBtn.setStyleSheet("border:0px;")
		destroyBtn.clicked.connect(self.delete)

		#ContentLayout
		contentLayout = QHBoxLayout()
		contentLayout.addLayout(self.itemLayout)
		contentLayout.addLayout(nbLayout)

		#MainLayout
		mainLayout = QHBoxLayout()
		mainLayout.addWidget(destroyBtn, 0, Qt.AlignRight)
		mainLayout.addLayout(contentLayout)

		self.setLayout(mainLayout)

	def minusNb(self):
		nb = self.itemNb.value() - [1,16,32,64,128,1728,3456][self.itemNbPerClick.currentIndex()]
		self.itemNb.setValue(nb)

	def addNb(self):
		nb = self.itemNb.value() + [1,16,32,64,128,1728,3456][self.itemNbPerClick.currentIndex()]
		self.itemNb.setValue(nb)

	def itemChoose(self):
		itemPicker = ItemPicker(self)
		if itemPicker.exec_():
			self.item = itemPicker.getValue()

			#Delete old item image
			self.itemImage.setParent(None)
			self.itemImage.deleteLater()

			#Add new item image
			self.itemImage = ItemImage(self.item)
			self.itemImage.clicked.connect(self.itemChoose)
			self.itemLayout.insertWidget(0, self.itemImage)

			#Update item name
			self.itemText.setText(self.item.name)

	def nbChanged(self):
		self.item.nb = self.itemNb.value()

	def delete(self):
		self.parent.itemsLayout.removeWidget(self)
		self.deleteLater()
		self.parent.parent.updateLabel()

	def getValue(self):
		return self.item