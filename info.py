"""
This Module has the Info class to show the last operations.
"""

from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE


class Info(QLabel):
    """
    Class to show the last operations.
    """

    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.config_style()

    def config_style(self) -> None:
        """
        Info settings.
        """
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(
            f'font-size: {SMALL_FONT_SIZE}px;')
        self.setContentsMargins(*[5 for _ in range(4)])
