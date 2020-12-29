from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class New(QDialog):
	""" New popup """

	def __init__(self, parent):
		super().__init__(parent, Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)
		self.initUI()

	def initUI(self):
		self.setWindowTitle('New list')
		self.setWindowIcon(QIcon('Assets/new.png'))

		self.setMinimumWidth(225)

		# --- formLayout ---
		formLayout = QFormLayout()
		formLayout.setFormAlignment(Qt.AlignCenter)

		# Name
		nameText = QLineEdit()
		formLayout.addRow("Name :",nameText)

		# --- buttons ---
		createBtn = QPushButton("Create")
		createBtn.clicked.connect(self.create)

		cancelBtn = QPushButton("Cancel")
		cancelBtn.clicked.connect(self.close)

		btnLayout = QHBoxLayout()
		btnLayout.addWidget(createBtn)
		btnLayout.addWidget(cancelBtn)

		# --- mainLayout ---
		mainLayout = QVBoxLayout()

		mainLayout.addLayout(formLayout)
		mainLayout.addLayout(btnLayout)

		self.setLayout(mainLayout)

		self.exec_()

	def create(self):
		pass

if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication
	app = QApplication(sys.argv)
	new = New(None)
	sys.exit(app.exec_())