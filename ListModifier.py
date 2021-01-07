from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QPushButton, QAbstractSlider
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from ItemList import ItemList

class ListModifier(QScrollArea):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWidget(ListModifierWidget(self))
		self.setWidgetResizable(True)

	def scollDown(self):
		vbar = self.verticalScrollBar()
		vbar.setValue(vbar.maximum())

class ListModifierWidget(QWidget):
	def __init__(self, parent):
		super().__init__(parent)

		self.parent = parent

		self.initUI()

	def initUI(self):
		# ItemsLayout
		self.itemsLayout = QVBoxLayout()
		self.itemsLayout.setAlignment(Qt.AlignAbsolute)

		# AddItemBtn
		self.addItemBtn = QPushButton()
		self.addItemBtn.setIcon(QIcon("Assets/add.png"))
		self.addItemBtn.setStyleSheet("border:0px;")
		self.addItemBtn.setIconSize(QSize(50,50))
		self.addItemBtn.clicked.connect(self.addItem)

		# MainLayout
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(self.itemsLayout)
		mainLayout.addWidget(self.addItemBtn, 0, Qt.AlignBottom | Qt.AlignHCenter)

		self.setLayout(mainLayout)

		self.show()

	def addItem(self):
		item = ItemList()
		self.itemsLayout.addWidget(item)

	def resizeEvent(self, event):
		self.parent.scollDown()

	def getValue(self):
		list = []
		for i in range(self.itemsLayout.count()):
			list.append(self.itemsLayout.itemAt(i).widget().getValue())
		return list