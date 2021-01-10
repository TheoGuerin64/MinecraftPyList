from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class New(QDialog):
	def __init__(self, parent):
		super().__init__(parent, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
		self.initUI()

	def initUI(self):
		self.setWindowTitle("New list")
		self.setWindowIcon(QIcon("Assets/new.png"))

		self.setFixedSize(225,71)

		#FormLayout
		formLayout = QFormLayout()
		formLayout.setFormAlignment(Qt.AlignCenter)

		#Name
		self.nameText = QLineEdit()
		formLayout.addRow("Name :",self.nameText)

		#Buttons
		createBtn = QPushButton("Create")
		createBtn.clicked.connect(self.create)

		cancelBtn = QPushButton("Cancel")
		cancelBtn.clicked.connect(self.reject)

		btnLayout = QHBoxLayout()
		btnLayout.addWidget(createBtn)
		btnLayout.addWidget(cancelBtn)

		#MainLayout
		mainLayout = QVBoxLayout()

		mainLayout.addLayout(formLayout)
		mainLayout.addLayout(btnLayout)

		self.setLayout(mainLayout)

		self.exec_()

	def create(self):
		if self.nameText.text() != "":
			self.accept()

	def getValue(self):
		return self.nameText.text()