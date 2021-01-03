from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpinBox, QAbstractSpinBox, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from itemAssetsList import itemAssetsList
from ItemPicker import ItemPicker
from ItemImage import ItemImage
from Item import Item

class ItemList(QWidget):
	def __init__(self, item=Item("Dirt")):
		super().__init__()

		self.item = item

		self.initUI()

	def initUI(self):
		self.setFixedSize(370,100)

		#item
		self.itemImage = ItemImage(self.item)
		self.itemImage.clicked.connect(self.itemChoose)

		self.itemText = QLabel(self.item.name)
		self.itemText.setMinimumWidth(150)
		self.itemText.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.itemLayout = QHBoxLayout()
		self.itemLayout.addWidget(self.itemImage)
		self.itemLayout.addWidget(self.itemText)

		#number of items
		self.itemNb = QSpinBox()
		self.itemNb.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.itemNb.setAlignment(Qt.AlignCenter)
		self.itemNb.setFixedSize(50,25)
		self.itemNb.setRange(0, 999999)
		self.itemNb.setValue(self.item.nb)

		#minusBtn
		minusBtn = QPushButton("-")
		minusBtn.setStyleSheet("border:0px;")
		minusBtn.clicked.connect(self.minusNb)

		#addBtn
		addBtn = QPushButton("+")
		addBtn.setStyleSheet("border:0px;")
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
		self.itemNbPerClick.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)

		#nbLayout
		nbLayout = QVBoxLayout()
		nbLayout.addLayout(itemNbLayout)
		nbLayout.addWidget(self.itemNbPerClick)

		#destroyBtn
		destroyBtn = QPushButton("x")
		destroyBtn.setStyleSheet("border:0px;")
		destroyBtn.clicked.connect(self.deleteLater)

		#contentLayout
		contentLayout = QHBoxLayout()
		contentLayout.addLayout(self.itemLayout)
		contentLayout.addLayout(nbLayout)

		#mainLayout
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(destroyBtn, 0, Qt.AlignRight)
		mainLayout.addLayout(contentLayout)
		self.setLayout(mainLayout)

	def minusNb(self):
		self.itemNb.setValue(self.itemNb.value() - [1,16,32,64,128,1728,3456][self.itemNbPerClick.currentIndex()])

	def addNb(self):
		self.itemNb.setValue(self.itemNb.value() + [1,16,32,64,128,1728,3456][self.itemNbPerClick.currentIndex()])

	def itemChoose(self):
		itemPicker = ItemPicker(self)
		if itemPicker.exec_():
			self.item = itemPicker.getValue()

			#delete old item image
			self.itemImage.setParent(None)
			self.itemImage.deleteLater()

			#add new item image
			self.itemImage = ItemImage(self.item)
			self.itemImage.clicked.connect(self.itemChoose)
			self.itemLayout.insertWidget(0, self.itemImage)

			#update item name
			self.itemText.setText(self.item.name)

if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication
	app = QApplication(sys.argv)
	new = ItemList()
	new.show()
	sys.exit(app.exec_())