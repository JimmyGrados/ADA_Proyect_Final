from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QGroupBox, QRadioButton, QHBoxLayout

from UIElements import Cell, Block
from enum import Enum, auto


class Cmds(Enum):
    NUM = auto()
    DEL = auto()
    MOUSE = auto()
    CELLCLICK = auto()
    IMPORT = auto()
    RESTART = auto()
    SOLVE = auto()
    FILLSINGLE = auto()
    CLEAR = auto()
    SHOW = auto()


def GenButtonMap():
    return {Cmds.IMPORT: 'Start',
            Cmds.CLEAR: 'Clear my work',
            Cmds.SOLVE: 'Solve by Backtracking',
            Cmds.FILLSINGLE: 'Solve by Coloring Graph',
            Cmds.SHOW: 'Show board in console',
            Cmds.RESTART: 'Restart'
    
            }


class PyQtSudokuView(QMainWindow):
    def __init__(self,nivel):
        super(QMainWindow, self).__init__()
        self.nivel=nivel
        button_map = GenButtonMap()
        self.key_table = {k: Cmds.NUM for k in range(QtCore.Qt.Key_0, QtCore.Qt.Key_9+1)}
        self.key_table.update({QtCore.Qt.Key_Backspace: Cmds.DEL})
        self.func_map = {}

        board_layout, side_ui_layout = self.SetupWindow()
        
        #conectar a los evenesos
        self.btnBack.clicked.connect(self.solveBack)


        self.cells = self.CreateBoard(self, board_layout)

        for cmd in button_map:
            title = button_map[cmd]
            self.AddButton(side_ui_layout, title, lambda state, x=cmd: self.ExecuteCmd(x))

    def SetupWindow(self):
        self.setGeometry(500, 30, 1200, 900)
        self.setWindowTitle("Simple Sudoku")
        #FONDO DE PANTALLA
        self.setStyleSheet("background-color: grey;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        outer_layout = QGridLayout()
        board_layout = QGridLayout()
        side_ui_layout = QVBoxLayout()
        central_widget.setLayout(outer_layout)

       

        lblTipoAlgoritmo=QLabel("Tipo algoritmo:")
        self.tipoALgoritmo=QLabel("")
        lblTiempo=QLabel("Tiempo(s):")
        self.tiempo=QLabel("")

        #MARCO INFO TIEMPO
        groupProcesamiento=QGroupBox("Tiempo de procesamiento")
        groupProcesamiento.setFixedHeight(100)

        lytGroupProcesamiento=QHBoxLayout()
        lytGroupProcesamiento.addWidget(lblTipoAlgoritmo)
        lytGroupProcesamiento.addWidget(self.tipoALgoritmo)
        lytGroupProcesamiento.addWidget(lblTiempo)
        lytGroupProcesamiento.addWidget(self.tiempo)
        groupProcesamiento.setLayout(lytGroupProcesamiento)   
       
       
        #MARCO COMPARAR TIEMPOS
        groupComparar=QGroupBox("Info Comparacion")
        lblBack=QLabel("Tiempo backtracking")
        lblColor=QLabel("Tiempo Color")
        self.TiempoBack=QLabel("s")
        self.TiempoColor=QLabel("s")

    

        lytGroupComparar=QVBoxLayout()
        lytGroupComparar.addWidget(lblBack)
        lytGroupComparar.addWidget(self.TiempoBack)
        lytGroupComparar.addWidget(lblColor)
        lytGroupComparar.addWidget(self.TiempoColor)
        groupComparar.setLayout(lytGroupComparar)   

        #MARCO BOTONES
        self.btnBack=QPushButton("Resolver por Backtracking")
        self.btnColor=QPushButton("Resolver por GraphColoring")
        self.btnComparar=QPushButton("Comparar Tiempos")

        groupButtons=QGroupBox("Botones")
        lytGroupButtons=QVBoxLayout()
        lytGroupButtons.addWidget(self.btnBack)
        lytGroupButtons.addWidget(self.btnColor)
        lytGroupButtons.addWidget(self.btnComparar)
        groupButtons.setLayout(lytGroupButtons)   

        #AGREGANDO MARCOS
        side_ui_layout.addWidget(groupProcesamiento)
        side_ui_layout.addWidget(groupComparar)
        side_ui_layout.addWidget(groupButtons)
        

        outer_layout.addLayout(board_layout, 0, 0, 9, 9)
        outer_layout.addLayout(side_ui_layout, 2, 9, 4, 3)
        
        return board_layout, side_ui_layout

    def solveBack(self):
        #MODIFICAR TU ETIQUETA TIPO ALGORITMO

        self.tipoALgoritmo.setText("Backtracking")
        print("ENTRE A LA SOLUCION back")

    def solveColor(self):
        print("ENTRE A LA SOLUCION color")

    def compararTiempos(self):
        print("COMPARAR TIEMPO")







    @staticmethod
    def AddButton(layout, title, func):
        button = QPushButton(title)
        button.clicked.connect(func)
        layout.addWidget(button)
        return button

    @staticmethod
    def CreateBlock(parent, layout, bi, bj):
        block = Block(parent)
        layout.addWidget(block, bi, bj)
        return block

    @staticmethod
    def CreateCell(i, j, boxes, click_func):
        bi, bj = i // 3, j // 3
        parent_box = boxes[bi][bj]
        cell = Cell(parent_box, i, j)
        cell.ConnectCelltoWindow(click_func)
        parent_box.AddCell(cell, i - 3*bi, j - 3*bj)
        return cell

    def CreateBoard(self, parent, layout):
        blocks = [[self.CreateBlock(parent, layout, bi, bj) for bj in range(3)] for bi in range(3)]
        return [[self.CreateCell(i, j, blocks, self.CellClicked) for j in range(9)] for i in range(9)]

    def ExecuteCmd(self, cmd, data=None):
        if cmd in self.func_map:
            if data is not None:
                self.func_map[cmd](data)
            else:
                self.func_map[cmd]()

    def Connect(self, func_map):
        self.func_map = func_map
    
    def keyPressEvent(self, event):
        key = event.key()

        if key in self.key_table:
            cmd = self.key_table[key]
            if QtCore.Qt.Key_0 <= key <= QtCore.Qt.Key_9:
                num = int(key) - int(QtCore.Qt.Key_0)
                self.ExecuteCmd(cmd, num)
            else:
                self.ExecuteCmd(cmd)

    def mouseReleaseEvent(self, QMouseEvent):
        self.ExecuteCmd(Cmds.MOUSE)

    def CellClicked(self, cell):
        self.ExecuteCmd(Cmds.CELLCLICK, cell)

    def UpdateAllCells(self, board, initial=False):
        for i in range(0, 9):
            for j in range(0, 9):
                self.cells[i][j].UpdateValue(board[i][j], initial)
