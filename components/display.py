"""
Module for creating the 'Display' class
"""

from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from .variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
    """
    This class will be the input of the calculator.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        """
        Display settings.
        """
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        self.setMinimumWidth(MINIMUM_WIDTH)
