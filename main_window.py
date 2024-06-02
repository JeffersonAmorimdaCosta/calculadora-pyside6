from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """
    Main window class.
    """

    def __init__(self, *args, parent: QWidget | None = None,
                 **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()

        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Calculadora')

    def adjust_fixed_size(self):
        """
        Method to adjust and fix the screen size.
        """
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
