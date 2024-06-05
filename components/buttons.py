"""
This module has the class. 
"""

from PySide6.QtWidgets import QPushButton, QGridLayout
from .variables import MEDIUM_FONT_SIZE
from .utils import is_num_or_dot


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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]

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
