from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QTabWidget, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
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

		self.version = "0.6"

		self.listName = None

		# --- Menu bar ---

		menubar = self.menuBar()

		# -- File menu --
		fileMenu = menubar.addMenu("&File")

		#New list action
		newAct = QAction("&New", self)
		newAct.setShortcut("Ctrl+N")
		newAct.setStatusTip("New list")
		newAct.triggered.connect(self.newAction)

		fileMenu.addAction(newAct)

		#Load menu
		self.loadMenu = fileMenu.addMenu("Load")

		self.updateLoadMenu()

		#Save list action
		saveAct = QAction("&Save", self)
		saveAct.setShortcut("Ctrl+S")
		saveAct.setStatusTip("Save list")
		saveAct.triggered.connect(self.saveAction)

		fileMenu.addAction(saveAct)

		#Import menu in file menu
		importMenu = fileMenu.addMenu("Import list from")

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

		# -- Edit menu --
		editMenu = menubar.addMenu("&Edit")

		#Clear list action
		clearListAct = QAction("&Clear list", self)
		clearListAct.setStatusTip("Clear the list")
		clearListAct.triggered.connect(self.askClear)

		editMenu.addAction(clearListAct)


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
		if new:
			self.listName = new.getValue()
			self.setWindowTitle("MinecraftPyList - " + self.listName)
			self.askClear()

	def saveAction(self):
		import pickle

		if self.listName != None:
			save = {}

			save["version"] = self.version

			itemList = self.tab1.widget().getValue()
			save["itemList"] = itemList

			with open("Saves\\" + self.listName, "wb") as file:
				p = pickle.Pickler(file)
				p.dump(save)

			self.updateLoadMenu()

	def updateLoadMenu(self):
		import os
		from functools import partial

		self.loadMenu.clear()

		for file in os.listdir("Saves"):
			act = self.loadMenu.addAction(file)
			act.triggered.connect(partial(self.loadAction,file))

	def loadAction(self, saveFile):
		import pickle

		with open("Saves\\"+saveFile, "rb") as file:
			dp = pickle.Unpickler(file)
			save = dp.load()

		if save["version"] == self.version or QMessageBox(QMessageBox.Warning, "Warning !", "The version of the save ("+save["version"]+") is different from the version of MinecraftPyList ("+self.version+")\nDo you want to load the save anyway ?", QMessageBox.Yes | QMessageBox.No).exec_() == QMessageBox.Yes:
			self.askClear()
			self.itemListToListModifier(save["itemList"])
			self.setWindowTitle("MinecraftPyList - " + saveFile)

	def itemListToListModifier(self, itemList):
		QApplication.setOverrideCursor(Qt.WaitCursor)
		for item in itemList:
			self.tab1.widget().addItem(None, Item(item, itemList[item]))
		QApplication.restoreOverrideCursor()

	def importNbtAction(self):
		from SchematicToItemList import getItemListFromNbt
		file = QFileDialog.getOpenFileName(None,"","","Schematic (*.nbt)")
		if ".nbt" in file[0]:
			self.askClear()
			itemList = getItemListFromNbt(file[0])
			self.itemListToListModifier(itemList)

	def importTextFileAction(self):
		from SchematicToItemList import getItemListFromTextFile
		file = QFileDialog.getOpenFileName(None,"","","Text file (*.txt)")
		if ".txt" in file[0]:
			self.askClear()
			itemList = getItemListFromTextFile(file[0])
			self.itemListToListModifier(itemList)

	def askClear(self):
		if self.tab1.widget().itemsLayout.count() > 0 and QMessageBox(QMessageBox.Question, "Confirmation", "Do you want to clear the list ?", QMessageBox.Yes | QMessageBox.No).exec_() == QMessageBox.Yes:
			QApplication.setOverrideCursor(Qt.WaitCursor)
			self.tab1.widget().clear()
			QApplication.restoreOverrideCursor()

#Launch the app
import sys

app = QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())