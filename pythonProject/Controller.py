from PyQtView import Cmds
from SudokuModel import SudokuModel


class Controller:
    def __init__(self, _view, _model):
        func_map = {Cmds.NUM: self.SelectedCellValueUpdated,
                    Cmds.DEL: self.CellValueDeleted,
                    Cmds.MOUSE: self.MouseClick,
                    Cmds.CELLCLICK: self.CellClicked,
                    Cmds.SHOW: self.showBoard,
                    Cmds.SOLVE: self.Solve}

        self.model = _model
        self.view = _view
        self.view.Connect(func_map)
        self.selected_cell = None
        self.ResetBoard()

    def SelectedCellValueUpdated(self, value):
        if self.selected_cell:
            i, j = self.selected_cell.i, self.selected_cell.j

            if self.selected_cell.CanEdit() and self.model.GetCell(i, j) != value:
                self.model.SetCell(i, j, value)
                self.selected_cell.UpdateValue(value)

    def CellValueDeleted(self):
        self.SelectedCellValueUpdated(0)

    def MouseClick(self):
        if self.selected_cell:
            self.selected_cell.Deselect()

        self.selected_cell = None

    def CellClicked(self, clicked_cell):
        cand = 0
        if self.selected_cell:
            if self.selected_cell is not clicked_cell:
                self.selected_cell.Deselect()
            else:
                cand = clicked_cell.FindCandidateClicked()
                if cand > 0:
                    i, j = clicked_cell.i, clicked_cell.j
                    if cand in self.model.GetCands(i, j):
                        self.model.GetCands(i, j).remove(cand)
                        clicked_cell.RemoveCandidate(cand)
                    else:
                        self.model.GetCands(i, j).add(cand)
                        clicked_cell.AddCandidate(cand)

        self.selected_cell = clicked_cell
       
        
    def Solve(self):
        SudokuModel.Solve()
        self.model = SudokuModel
        self.view.UpdateAllCells(self.model.GetBoard())

    def ResetBoard(self):
        self.model.ResetBoard()
        self.view.UpdateAllCells(self.model.GetBoard(), initial=True)

    def showBoard(self):
        board = SudokuModel.GetBoard(self.model)
        for i in board:
            print(*i, sep=' ')
        print('-------------------------------------\n')
