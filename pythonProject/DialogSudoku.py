from PyQt5.QtWidgets import QDialog, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel

class DialogNivel(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #PARA TAMAÑO
        self.resize(200, 300)
        self.nivel = None
        self.setWindowTitle('Elige el nivel')
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("")
        self.combo_box.addItem("Facil")
        self.combo_box.addItem("Intermedio")
        self.combo_box.addItem("Dificil")

        layout = QHBoxLayout(self)
        label1 = QLabel('Nivel:')
        layout.addWidget(label1)
        layout.addWidget(self.combo_box)
      

        btnAceptar = QPushButton('Aceptar', self)
        btnAceptar.clicked.connect(self.aceptar_valores)
        layout.addWidget(btnAceptar)

    def aceptar_valores(self):
        # Obtener los valores de los QLineEdit
        # Almacenar los valores como atributos de la instancia
        self.nivel=self.combo_box.currentText()
        if self.nivel != '':
        # Cerrar el cuadro de diálogo con aceptación
            self.accept()
        else:
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setText("Error")
            alerta.setInformativeText("ElIGA UN NIVEL.")
            alerta.setWindowTitle("Alerta")
            alerta.exec_()