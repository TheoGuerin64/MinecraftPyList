from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QAbstractSlider, QLabel, QSpacerItem
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from ItemList import ItemList
from Item import Item

class ListModifier(QScrollArea):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWidget(ListModifierWidget(self))
		self.setWidgetResizable(True)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

		#Items nb label
		self.label = QLabel("Item(s) : " + str(self.widget().itemsLayout.count()), self)
		self.label.setAlignment(Qt.AlignRight)
		self.label.setFixedSize(100,22)

		font = self.label.font()
		font.setPointSize(12)
		self.label.setFont(font)

		box = QHBoxLayout(self)
		box.setAlignment(Qt.AlignRight | Qt.AlignTop)
		box.addWidget(self.label)
		box.addSpacerItem(QSpacerItem(18,0))

	def scollDown(self):
		vbar = self.verticalScrollBar()
		vbar.setValue(vbar.maximum())

	def updateLabel(self):
		self.label.setText("Item(s) : " + str(self.widget().itemsLayout.count()))

class ListModifierWidget(QWidget):
	def __init__(self, parent):
		super().__init__(parent)

		self.parent = parent

		self.initUI()

	def initUI(self):
		#ItemsLayout
		self.itemsLayout = QVBoxLayout()
		self.itemsLayout.setAlignment(Qt.AlignAbsolute)

		#AddItemBtn
		self.addItemBtn = QPushButton()
		self.addItemBtn.setIcon(QIcon("Assets/add.png"))
		self.addItemBtn.setStyleSheet("border:0px;")
		self.addItemBtn.setIconSize(QSize(50,50))
		self.addItemBtn.clicked.connect(self.addItem)

		#MainLayout
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(self.itemsLayout)
		mainLayout.addWidget(self.addItemBtn, 0, Qt.AlignBottom | Qt.AlignHCenter)

		self.setLayout(mainLayout)

		self.show()

	def resizeEvent(self, event):
		self.parent.scollDown()

	def addItem(self, e, item=Item()):
		itemList = ItemList(self, item)
		self.itemsLayout.addWidget(itemList)
		self.parent.updateLabel()

	def clear(self):
		for i in range(self.itemsLayout.count()):
			self.itemsLayout.itemAt(0).widget().delete()
		self.parent.updateLabel()

	def getValue(self):
		itemList = {}
		for i in range(self.itemsLayout.count()):
			item = self.itemsLayout.itemAt(i).widget().getValue()
			itemList[item.name] = item.nb
		return itemList