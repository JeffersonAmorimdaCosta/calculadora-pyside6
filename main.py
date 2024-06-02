import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 50px')
    window.v_layout.addWidget(label1)
    window.adjust_fixed_size()
    window.show()
    app.exec()
