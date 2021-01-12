from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QTabWidget, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ListModifier import ListModifier
from ItemList import ItemList
from About import About
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
		self.historic = {"undo":[],"redo":[]}

		# --- Menu bar ---

		menubar = self.menuBar()

		# -- File menu --
		fileMenu = menubar.addMenu("&File")

		#New list action
		newAct = QAction("&New", self)
		newAct.setShortcut("Ctrl+N")
		newAct.triggered.connect(self.newAction)

		fileMenu.addAction(newAct)

		#Load menu
		self.loadMenu = fileMenu.addMenu("Load")

		self.updateLoadMenu()

		#Save list action
		saveAct = QAction("&Save", self)
		saveAct.setShortcut("Ctrl+S")
		saveAct.triggered.connect(self.saveAction)

		fileMenu.addAction(saveAct)

		#Import menu in file menu
		importMenu = fileMenu.addMenu("Import list from")

		#Nbt action
		nbtAct = QAction("&NBT", self)
		nbtAct.triggered.connect(self.importNbtAction)

		importMenu.addAction(nbtAct)

		#Text file action
		textFileAct = QAction("&Text file", self)
		textFileAct.triggered.connect(self.importTextFileAction)

		importMenu.addAction(textFileAct)

		#Exit action
		exitAct = QAction("E&xit", self)
		exitAct.setShortcut("Ctrl+Q")
		exitAct.triggered.connect(qApp.quit)

		fileMenu.addAction(exitAct)

		# -- Edit menu --
		editMenu = menubar.addMenu("&Edit")

		#Undo action
		undoAct = QAction("&Undo", self)
		undoAct.setShortcut("Ctrl+Z")
		undoAct.triggered.connect(self.undoAction)

		editMenu.addAction(undoAct)

		#Redo action
		redoAct = QAction("&Repeat", self)
		redoAct.setShortcut("Ctrl+Y")
		redoAct.triggered.connect(self.redoAction)

		editMenu.addAction(redoAct)

		#Clear list action
		clearListAct = QAction("&Clear list", self)
		clearListAct.triggered.connect(self.askClear)

		editMenu.addAction(clearListAct)

		# -- Help menu --
		helpMenu = menubar.addMenu("&Help")

		#About MinecraftPyList
		aboutAct = QAction("About &MinecraftPyList", self)
		aboutAct.triggered.connect(partial(About,self))

		helpMenu.addAction(aboutAct)

		#About Qt action
		aboutQtAct = QAction("About &Qt", self)
		aboutQtAct.triggered.connect(partial(QMessageBox.aboutQt,self))

		helpMenu.addAction(aboutQtAct)


		# --- Tabs ---

		tabs = QTabWidget()

		#Tab1
		self.tab1 = ListModifier(self)
		tabs.addTab(self.tab1, "List modifier")

		#Tab2
		tab2 = QWidget()
		tabs.addTab(tab2, "List info")

		self.setCentralWidget(tabs)

		self.show()

	def undoAction(self):
		if self.historic["undo"] != []:
			i = len(self.historic["undo"])-1
			undo = self.historic["undo"][i]

			if undo[0] == "name":
				if undo[1][0] != None:
					self.listName = undo[1][0]
					self.setWindowTitle("MinecraftPyList - " + undo[1][0])
				else:
					self.listName = None
					self.setWindowTitle("MinecraftPyList")
			elif undo[0] == "add":
				self.tab1.widget().itemsLayout.itemAt(self.tab1.widget().itemsLayout.count()-1).widget().delete()
			elif undo[0] == "adds":
				for k in range(len(undo[1])):
					self.tab1.widget().itemsLayout.itemAt(self.tab1.widget().itemsLayout.count()-1).widget().delete()
			elif undo[0] == "delete":
				self.tab1.widget().itemsLayout.insertWidget(undo[1][1], ItemList(self.tab1.widget(), undo[1][0]))
			elif undo[0] == "clear":
				for item in undo[1]:
					self.tab1.widget().addItem(item)
			elif undo[0] == "valueChanged":
				undo[1][0].itemNb.blockSignals(True)
				undo[1][0].itemNb.setValue(undo[1][1])
				undo[1][0].itemNb.blockSignals(False)
			elif undo[0] == "itemChanged":
				undo[1][0].item = undo[1][1]
				undo[1][0].updateItem()

			self.historic["redo"].append(undo)
			del self.historic["undo"][i]

	def redoAction(self):
		if self.historic["redo"] != []:
			i = len(self.historic["redo"])-1
			redo = self.historic["redo"][i]

			if redo[0] == "name":
				if redo[1][1] != None:
					self.listName = redo[1][1]
					self.setWindowTitle("MinecraftPyList - " + redo[1][1])
				else:
					self.listName = None
					self.setWindowTitle("MinecraftPyList")
			elif redo[0] == "add":
				self.tab1.widget().addItem()
			elif redo[0] == "adds":
				self.itemListToListModifier(redo[1], False)
			elif redo[0] == "delete":
				self.tab1.widget().itemsLayout.itemAt(redo[1][1]).widget().delete()
			elif redo[0] == "clear":
				for k in range(len(redo[1])):
					self.tab1.widget().itemsLayout.itemAt(self.tab1.widget().itemsLayout.count()-1).widget().delete()
			elif redo[0] == "valueChanged":
				redo[1][0].itemNb.blockSignals(True)
				redo[1][0].itemNb.setValue(redo[1][2])
				redo[1][0].itemNb.blockSignals(False)
			elif redo[0] == "itemChanged":
				redo[1][0].item = redo[1][2]
				redo[1][0].updateItem()

			self.historic["undo"].append(redo)
			del self.historic["redo"][i]

	def addUndo(self, list):
		self.historic["undo"].append(list)
		self.historic["redo"] = []
		print(self.historic["undo"])

	def newAction(self):
		from New import New
		new = New(self)
		if new.exec_():
			self.addUndo(["name", [self.listName, new.getValue()]])
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

	def itemListToListModifier(self, itemList, undo=True):
		QApplication.setOverrideCursor(Qt.WaitCursor)
		if undo:
			self.addUndo(["adds", itemList])
		for item in itemList:
			self.tab1.widget().addItem(True, Item(item, itemList[item]))
		QApplication.restoreOverrideCursor()

	def importNbtAction(self):
		from SchematicToItemList import getItemListFromNbt
		file = QFileDialog.getOpenFileName(None,"","","Schematic (*.nbt)")
		if ".nbt" in file[0]:
			self.askClear()
			QApplication.setOverrideCursor(Qt.WaitCursor)
			itemList = getItemListFromNbt(file[0])
			self.itemListToListModifier(itemList)
			QApplication.restoreOverrideCursor()

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