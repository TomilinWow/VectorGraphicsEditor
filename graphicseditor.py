from PyQt5 import QtWidgets
from View import View
import sys

def main():
    """
    Запуск программы
    """
    app = QtWidgets.QApplication(sys.argv)
    g = View()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
