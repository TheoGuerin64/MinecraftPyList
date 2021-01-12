from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class About(QDialog):
	def __init__(self, parent):
		super().__init__(parent, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
		self.initUI()

	def initUI(self):
		self.setWindowTitle("About MinecraftPyList")
		self.setWindowIcon(QIcon("Assets/icon.png"))

		contentLayout = QHBoxLayout()

		icon = QLabel()
		icon.setPixmap(QPixmap("Assets/icon.png").scaled(100, 100))

		contentLayout.addWidget(icon)

		text = QLabel("MinecraftPyList<br>Version : "+self.parent().version+"<br><br>Thanks to <a href='https://www.flaticon.com/authors/icongeek26'>icongeek26</a> for the icons<br><br>GNU General Public License v3.0")
		text.setTextFormat(Qt.RichText)

		contentLayout.addWidget(text)

		self.setLayout(contentLayout)

		self.exec_()