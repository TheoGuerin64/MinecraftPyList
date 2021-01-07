import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QTabWidget, QWidget, QScrollArea
from PyQt5.QtGui import QIcon
from ListModifier import ListModifier

class Main(QMainWindow):
	""" Main window """

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("MinecraftPyList")
		self.setWindowIcon(QIcon("Assets/icon.png"))
		# https://www.flaticon.com/authors/icongeek26

		self.setMinimumWidth(1000)
		self.setMinimumHeight(700)

		# --- Menu bar ---

		# New list action
		newAct = QAction("&New", self)
		newAct.setShortcut("Ctrl+N")
		newAct.setStatusTip("New list")
		newAct.triggered.connect(self.newAction)

		# Load list action
		loadAct = QAction("&Load", self)
		loadAct.setShortcut("Ctrl+L")
		loadAct.setStatusTip("Load list")
		loadAct.triggered.connect(qApp.quit)

		# Exit action
		exitAct = QAction("E&self.setFixedSize(225,80)xit", self)
		exitAct.setShortcut("Ctrl+Q")
		exitAct.setStatusTip("Exit application")
		exitAct.triggered.connect(qApp.quit)

		# Load menubar
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newAct)
		fileMenu.addAction(loadAct)
		fileMenu.addAction(exitAct)

		# --- Tabs ---

		tabs = QTabWidget()

		# Tab1
		tab1 = ListModifier()

		tabs.addTab(tab1, "List modifier")

		# Tab2
		tab2 = QWidget()
		tabs.addTab(tab2, "List info")

		self.setCentralWidget(tabs)

		self.show()

	def newAction(self):
		from New import New
		new = New(self)

app = QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())