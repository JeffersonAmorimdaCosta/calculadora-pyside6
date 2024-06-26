"""
This module has the main window class.
"""

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLayout


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

    def adjust_fixed_size(self) -> None:
        """
        Method to adjust and fix the window size.
        """

        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_vlayout(self, widget: QWidget) -> None:
        """
        Add a widget to the v_layout.
        """

        self.v_layout.addWidget(widget)

    def add_layout_to_vlayout(self, layout: QLayout) -> None:
        """
        Add a layout to the v_layout
        """

        self.v_layout.addLayout(layout)
