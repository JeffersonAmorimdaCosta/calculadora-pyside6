"""
This module has the class.
"""

from typing import Callable, TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from .variables import MEDIUM_FONT_SIZE, MINIMUN_HEIGHT_BUTTON
from .utils import is_num_or_dot, is_valid_number

if TYPE_CHECKING:
    from .display import Display
    from .info import Info


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
        self.setMinimumHeight(MINIMUN_HEIGHT_BUTTON)


class ButtonsGrid(QGridLayout):
    """
    This class is responsible for the grid button settings.
    """

    def __init__(self, display: 'Display', info: 'Info',
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]

        self.display = display
        self.info = info
        self._equation = ''
        self._equation_initial_value = 'Sua conta'
        self._left: float | None = None
        self._right: float | None = None
        self._op: str | None = None
        self._make_grid()

    @property
    def equation(self) -> str:
        """
        Getter for self._equation.
        """

        return self._equation

    @equation.setter
    def equation(self, value: str) -> None:
        self._equation = value
        self.info.setText(value)

    def _make_grid(self) -> None:
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not button_text:
                    continue

                if not is_num_or_dot(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._setconfig_special_button(button)

                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2)
                else:
                    self.addWidget(button, i, j)

                slot = self._make_slot(self._insert_buttontext_to_display,
                                       button)

                self._connect_button_clicked(button, slot)

    def _setconfig_special_button(self, button: Button):

        if button.text() == 'C':
            self._connect_button_clicked(button, self._clear)

        if button.text() in '+-*/':
            self._connect_button_clicked(button,
                                         self._make_slot(
                                             self._operator_clicked, button))

        if button.text() == '=':
            self._connect_button_clicked(button, self._eq)

    def _connect_button_clicked(self, button: Button, slot):
        """
        Connect the button to a slot.
        """

        button.clicked.connect(slot)

    def _make_slot(self, func: Callable, *args, **kwargs):
        @Slot()
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot

    @Slot(Button)
    def _insert_buttontext_to_display(self, button: Button):
        new_value: str = self.display.text() + button.text()

        if not is_valid_number(new_value):
            return
        self.display.insert(button.text())

    def _clear(self) -> None:
        self._left = self._right = self._op = None
        self.equation = self._equation_initial_value
        self.display.clear()

    def _operator_clicked(self, button: Button):
        button_text = button.text()
        display_text = self.display.text()
        self.display.clear()

        if not is_valid_number(display_text) and self._left is None:
            return

        if self._left is None:
            self._left = float(display_text)

        self._op = button_text
        if self._left is not None:
            self.equation += f'{self._left} {self._op}'
        self.equation = f'{self._left} {self._op}'

    def _eq(self):
        display_text = self.display.text()

        if not is_valid_number(display_text):
            return

        self._right = float(display_text)
        self.equation = f'{self._left} {self._op} {self._right} ='

        result = '0.0'
        try:
            result = str(eval(self.equation.replace('=', '')))
        except ZeroDivisionError:
            result = 'Division by zero'

        self.display.setText(result)

        if not is_valid_number(result):
            result = '0.0'

        self._left = float(result)
        self._right = None
