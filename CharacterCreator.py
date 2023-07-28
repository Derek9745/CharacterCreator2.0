from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QLabel, QVBoxLayout
import sys

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CharacterCreator 2.0")
        tabs = QTabWidget()
        tabs.setFixedWidth(600)
        tabs.setFixedHeight(400)
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)
        labelName = QLabel("Character Creator")
        tabs.addTab(labelName,"Character Creator")
        label1 = QLabel("Widget in tab1")
        tabs.addTab(label1,"Char1")
        label2 = QLabel("widget in tab2")
        tabs.addTab(label2,"Char2")
        label3 = QLabel("Widget in tab3")
        tabs.addTab(label3, "Char3")
        label4 = QLabel("Widget in tab4")
        tabs.addTab(label4,"Char4")
        self.setCentralWidget(tabs)

        layout = QVBoxLayout()
        labelName = QLabel("Name: ")
        layout.addWidget(labelName)
        widget = QWidget()
        widget.setLayout(layout)

class CharacterClass():
    def __init__(self, name, Str, Int, Char, Dex, Cons, Class):
        self.name = name
        self.Str = Str
        self.Int = Int
        self.Char = Char
        self.Dex = Dex
        self.Cons = Cons
        self.Class = Class



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
