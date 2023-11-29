import sys
from os import environ
from PyQt5 import QtCore, QtWidgets
from Controller import Controller
from SudokuModel import SudokuModel
from PyQtView import PyQtSudokuView

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

board1 = [
    [5, 3, 8, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 6, 2, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 5, 1, 0],
    [2, 1, 5, 4, 8, 0, 0, 6, 9],
    [0, 8, 0, 2, 7, 5, 4, 0, 0],
    [3, 0, 0, 9, 6, 1, 0, 0, 0],
    [0, 6, 3, 8, 5, 7, 9, 2, 4],
    [0, 0, 7, 1, 0, 0, 0, 5, 3],
    [8, 0, 9, 0, 4, 2, 1, 7, 6]
]


def run_app(orig_board):
    model = SudokuModel(orig_board)
    app = QtWidgets.QApplication(sys.argv)
    main_win = PyQtSudokuView()
    controller = Controller(main_win, model)
    main_win.show()
    return app.exec_()


def main():
    sys.exit(run_app(board1))


if __name__ == "__main__":
    main()

