import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit,
                             QPushButton, QVBoxLayout, QAction, QMenuBar,
                             QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Calculator - Aries Rio')

        self.textLine = QLineEdit(self)

        grid = QGridLayout()
        grid.addWidget(self.textLine, 0, 0, 1, 4)

        names = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'sin', 'cos', '^',
            '(', ')'
        ]

        positions = [(i, j) for i in range(1, 7) for j in range(4)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.on_button_click)

        menubar = QMenuBar(self)
        file_menu = menubar.addMenu('File')
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_to_file)
        exit_action = QAction('Exit - Ctrl + Q', self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        vbox = QVBoxLayout()
        vbox.setMenuBar(menubar)
        vbox.addLayout(grid)
        self.setLayout(vbox)

        self.show()

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == '=':
            try:
                expression = self.textLine.text().replace('^', '**')
                expression = expression.replace('sin', 'math.sin').replace('cos', 'math.cos')
                result = eval(expression)
                self.textLine.setText(str(result))
                self.save_operation(expression, result)
            except Exception:
                self.textLine.setText('Error')
        elif text == 'C':
            self.textLine.clear()
        else:
            current_text = self.textLine.text()
            self.textLine.setText(current_text + text)

    def save_operation(self, operation, result):
        with open('calculations.txt', 'a') as f:
            f.write(f"{operation} = {result}\n")

    def save_to_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write("Calculation History:\n")
                with open('calculations.txt', 'r') as history:
                    f.write(history.read())
            QMessageBox.information(self, 'Saved', 'Calculations have been saved successfully!')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit Confirmation', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q and event.modifiers() == Qt.ControlModifier:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
