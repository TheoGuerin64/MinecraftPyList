import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QTabWidget, QWidget, QFileDialog
from PyQt5.QtGui import QIcon
from ListModifier import ListModifier
from Item import Item

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("MinecraftPyList")
		self.setWindowIcon(QIcon("Assets/icon.png"))
		self.setMinimumSize(1000,700)

		# --- Menu bar ---

		menubar = self.menuBar()

		# -- File menu --
		fileMenu = menubar.addMenu('&File')

		#New list action
		newAct = QAction("&New", self)
		newAct.setShortcut("Ctrl+N")
		newAct.setStatusTip("New list")
		newAct.triggered.connect(self.newAction)

		fileMenu.addAction(newAct)

		#Load list action
		loadAct = QAction("&Load", self)
		loadAct.setShortcut("Ctrl+L")
		loadAct.setStatusTip("Load list")
		loadAct.triggered.connect(qApp.quit)

		fileMenu.addAction(loadAct)

		#Import menu in file menu
		importMenu = fileMenu.addMenu("Import from schematic")

		#Nbt action
		nbtAct = QAction("&NBT", self)
		nbtAct.setStatusTip("Import list from nbt schematic")
		nbtAct.triggered.connect(self.importNbtAction)

		importMenu.addAction(nbtAct)

		#Text file action
		textFileAct = QAction("&Text file", self)
		textFileAct.setStatusTip("Import list from text file")
		textFileAct.triggered.connect(self.importTextFileAction)

		importMenu.addAction(textFileAct)

		#Exit action
		exitAct = QAction("E&xit", self)
		exitAct.setShortcut("Ctrl+Q")
		exitAct.setStatusTip("Exit application")
		exitAct.triggered.connect(qApp.quit)

		fileMenu.addAction(exitAct)

		# --- Tabs ---

		tabs = QTabWidget()

		#Tab1
		self.tab1 = ListModifier()
		tabs.addTab(self.tab1, "List modifier")

		#Tab2
		tab2 = QWidget()
		tabs.addTab(tab2, "List info")

		self.setCentralWidget(tabs)

		self.show()

	def newAction(self):
		from New import New
		new = New(self)

	def itemListToListModifier(self, itemList):
		for item in itemList:
			self.tab1.widget().addItem(None, Item(item, itemList[item]))

	def importNbtAction(self):
		from SchematicToItemList import getItemListFromNbt
		file = QFileDialog.getOpenFileName(None,"","","Schematic (*.nbt)")
		itemList = getItemListFromNbt(file[0])
		self.itemListToListModifier(itemList)

	def importTextFileAction(self):
		from SchematicToItemList import getItemListFromTextFile
		file = QFileDialog.getOpenFileName(None,"","","Text file (*.txt)")
		itemList = getItemListFromTextFile(file[0])
		self.itemListToListModifier(itemList)

app = QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())