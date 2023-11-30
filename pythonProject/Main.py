import sys
from os import environ
from PyQt5 import QtCore, QtWidgets
from Controller import Controller
from SudokuModel import SudokuModel
from PyQtView import PyQtSudokuView
from DialogSudoku import *
from SudokuNiveles import *
import random
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
tablasEasy= SudokuEasy()
easyTables = tablasEasy.getTablas()

mediumTables = []
hardTables = []
##############################################

board1 = [
    [0, 0, 0, 1, 0, 0, 0, 5, 0],
    [0, 5, 0, 0, 4, 0, 0, 0, 0],
    [4, 7, 0, 0, 5, 2, 0, 0, 0],
    [0, 0, 8, 0, 0, 4, 1, 3, 0],
    [3, 0, 2, 0, 0, 9, 0, 7, 0],
    [0, 9, 0, 3, 0, 0, 5, 0, 2],
    [2, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 1],
    [6, 0, 0, 0, 3, 1, 0, 0, 0]
]
mediumTables.append(board1)

board2 = [
    [0, 6, 4, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 9, 0, 0, 3],
    [0, 9, 0, 0, 4, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 2, 0, 0, 1],
    [9, 0, 0, 7, 0, 0, 0, 5, 0],
    [6, 0, 8, 0, 2, 0, 0, 7, 0],
    [5, 0, 0, 0, 0, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 4, 0, 6, 0]
]
mediumTables.append(board2)

###############################################

board1 = [
    [0, 0, 0, 0, 3, 2, 0, 6, 8],
    [0, 0, 0, 5, 0, 8, 0, 0, 3],
    [0, 0, 0, 7, 0, 4, 0, 0, 1],
    [4, 3, 5, 0, 7, 0, 0, 0, 2],
    [0, 0, 6, 0, 0, 9, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [5, 0, 4, 0, 8, 0, 7, 0, 9]
]
hardTables.append(board1)

board2 = [
    [3, 0, 0, 0, 5, 0, 0, 0, 7],
    [8, 0, 0, 6, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 4, 7, 0, 0, 0],
    [0, 9, 0, 4, 0, 1, 0, 0, 6],
    [0, 1, 0, 3, 0, 0, 0, 2, 0],
    [0, 4, 0, 0, 0, 0, 0, 7, 0],
    [2, 0, 0, 1, 0, 0, 0, 6, 0],
    [0, 3, 0, 5, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

hardTables.append(board2)


#easyTables=SudokuEasy.getTablas()
#mediumTables
#hardTables

def setBoard(nivel):
    if(nivel=="Facil"):
        n=len(easyTables)
        posTabla=random.randint(0,n-1)
        return easyTables[posTabla]
    elif(nivel=="Intermedio"):
        n=len(mediumTables)
        posTabla=random.randint(0,n-1)
        return mediumTables[posTabla]
    elif(nivel=="Dificil"):
        n=len(hardTables)
        posTabla=random.randint(0,n-1)
        return hardTables[posTabla]


def run_app():

    app = QtWidgets.QApplication(sys.argv)
   
    dialogSudoku = DialogNivel()
    resultado = dialogSudoku.exec_()
    if resultado == QDialog.Accepted:
        nivel=dialogSudoku.nivel
        board=setBoard(nivel)
       
        model = SudokuModel(board)
        main_win = PyQtSudokuView(nivel)
        controller = Controller(main_win, model)
        main_win.show()
    return app.exec_()


def main():
    sys.exit(run_app())


if __name__ == "__main__":
    main()

