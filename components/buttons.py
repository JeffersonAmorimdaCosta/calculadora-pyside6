"""
This module has the class. 
"""

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from typing import Callable
from .variables import MEDIUM_FONT_SIZE
from .utils import is_num_or_dot
from .display import Display


class Button(QPushButton):
    """
    This class is responsible for the settings of buttons.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.config_style()

    def config_style(self) -> None:
        """
        Buttons settings.
        """

        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)


class ButtonsGrid(QGridLayout):
    """
    This class is responsible for the grid button settings.
    """

    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]

        self.display = display
        self._make_grid()

    def _make_grid(self) -> None:
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not button_text:
                    continue

                if not is_num_or_dot(button_text):
                    button.setProperty('cssClass', 'specialButton')

                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2)
                else:
                    self.addWidget(button, i, j)
                button.clicked.connect(self.__make_button_display_slot(
                    self._insert_buttontext_to_display,
                    button)
                )

    def __make_button_display_slot(self, func: Callable, *args, **kwargs):
        @Slot()
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot

    @Slot(Button)
    def _insert_buttontext_to_display(self, button: Button):
        self.display.insert(button.text())
