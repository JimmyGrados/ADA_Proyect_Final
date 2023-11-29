from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, pyqtSlot

Signal, Slot = pyqtSignal, pyqtSlot


def Value2String(value):
    return str(value) if (0 < value < 10) else ' '


class Candidate(QLabel):
    def __init__(self, str_value, parent):
        super(QLabel, self).__init__(str_value, parent)
        self.setStyleSheet("""
           Candidate[hilite="red"]      {background-color: red;}
           Candidate[hilite="green"]    {background-color: lightgreen;}
           Candidate[hilite="off"]      {background: transparent;}
            """)

        self.SetHilite('off')

        self.setFont(QFont("Arial", 12))
        self.setAlignment(QtCore.Qt.AlignCenter)

    def SetHilite(self, hilite_colour='off'):
        self.setProperty('hilite', hilite_colour)
        self.style().unpolish(self)
        self.style().polish(self)


class Cell(QLabel):
    selected = Signal(object)

    def __init__(self, parent, i, j, value=0):
        super().__init__(Value2String(value), parent)
        self.i = i
        self.j = j

        self.setStyleSheet("""
           Cell[selected="true"] {background-color: lightblue;}
           Cell[selected="false"] {background-color: white;}
           Cell[edit="true"] {color: darkgrey;}
           Cell[edit="false"] {color: black;}
           Cell[invalid="true"] {color: red;}
            """)
        self.setProperty('selected', False)
        self.SetEditStatus(value == 0)

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont("Arial", 45, QFont.Bold))

        self.gridLayoutBox = QGridLayout()
        self.setLayout(self.gridLayoutBox)

    @staticmethod
    def CandCoordFromValue(value):
        return (value - 1) // 3, (value - 1) % 3

    def CreateCandidates(self, cand_set=None):
        if cand_set is None:
            cand_set = set()

        for cand_value in range(1, 10):
            i, j = self.CandCoordFromValue(cand_value)
            cand_str = str(cand_value) if cand_value in cand_set else ' '
            cand_label = Candidate(cand_str, self)
            self.gridLayoutBox.addWidget(cand_label, i, j)

    def ConnectCelltoWindow(self, ClickFunc):
        self.selected.connect(ClickFunc)

    def CanEdit(self):
        return self.property('edit')

    def UpdateValue(self, value, initial=False):
        str_value = Value2String(value)
        if initial:
            self.SetEditStatus(value == 0)

        if self.CanEdit() or initial:
            if value != 0:
                self.DeleteAllCandidates()
            elif self.gridLayoutBox.count() == 0:
                self.CreateCandidates()

            self.setText(str_value)

    def SetEditStatus(self, status):
        self.setProperty('edit', status)
        self.style().unpolish(self)
        self.style().polish(self)

    def DeleteAllCandidates(self):
        for i in reversed(range(self.gridLayoutBox.count())):
            widget = self.gridLayoutBox.itemAt(i).widget()
            widget.setParent(None)
            widget.deleteLater()

    def RemoveCandidate(self, value):
        if self.text() == ' ':
            i, j = self.CandCoordFromValue(value)
            cand_widget = self.gridLayoutBox.itemAtPosition(i, j).widget()
            cand_widget.setText(' ')

    def AddCandidate(self, value):
        if self.text() == ' ':
            i, j = self.CandCoordFromValue(value)
            cand_widget = self.gridLayoutBox.itemAtPosition(i, j).widget()
            cand_widget.setText(Value2String(value))

    def FindCandidateClicked(self):
        for cand_value in range(1, 10):
            i, j = self.CandCoordFromValue(cand_value)
            cand_widget = self.gridLayoutBox.itemAtPosition(i, j).widget()
            if cand_widget.underMouse():
                return cand_value

        return 0

    def mouseReleaseEvent(self, QMouseEvent):
        if not self.property('selected'):
            self.setProperty('selected', True)
            self.style().unpolish(self)
            self.style().polish(self)

        self.selected.emit(self)#, cand)

    def Deselect(self):
        self.setProperty('selected', False)
        self.style().unpolish(self)
        self.style().polish(self)


class Block(QLabel):
    def __init__(self, parent):
        super(QLabel, self).__init__(parent)
        self.setStyleSheet('background-color: lightgrey;')
        self.gridLayoutBox = QGridLayout()
        self.setLayout(self.gridLayoutBox)

    def AddCell(self, cell_QLabel, i, j):
        self.gridLayoutBox.addWidget(cell_QLabel, i, j)