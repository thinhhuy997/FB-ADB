import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')

        # Creating a simple action for the main menu
        new_action = QAction('New', self)
        file_menu.addAction(new_action)

        # Creating a submenu under the "File" menu
        sub_menu = QMenu('Open Recent', self)

        # Adding actions to the submenu
        sub_menu.addAction('File 1')
        sub_menu.addAction('File 2')
        sub_menu.addAction('File 3')

        # Adding the submenu to the "File" menu
        file_menu.addMenu(sub_menu)

        # Setting up the main window
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menu with Submenu Example')

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()