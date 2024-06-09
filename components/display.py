"""
Module for creating the 'Display' class
"""

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from .variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from .utils import is_empty, is_num_or_dot


class Display(QLineEdit):
    """
    This class will be the input of the calculator.
    """

    eq_pressed = Signal()
    delete_pressed = Signal()
    clear_pressed = Signal()
    input_pressed = Signal(str)
    operator_pressed = Signal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_style()

        self.setReadOnly(True)

    def config_style(self) -> None:
        """
        Display settings.
        """
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        self.setMinimumWidth(MINIMUM_WIDTH)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key_text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_delete = key in [KEYS.Key_Delete, KEYS.Key_Backspace]
        is_esc = key in [KEYS.Key_Escape, KEYS.Key_C]
        is_operator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash,
                              KEYS.Key_Asterisk, KEYS.Key_P]

        if is_enter:
            self.eq_pressed.emit()
            return event.ignore()

        if is_delete:
            self.delete_pressed.emit()
            return event.ignore()

        if is_esc:
            self.clear_pressed.emit()
            return event.ignore()

        if is_operator:
            if key_text.lower() == 'p':
                key_text = '^'
            self.operator_pressed.emit(key_text)
            return event.ignore()

        if is_empty(key_text):
            return event.ignore()

        if is_num_or_dot(key_text):
            self.input_pressed.emit(key_text)
            return event.ignore()
