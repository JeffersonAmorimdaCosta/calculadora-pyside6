"""
This module has the class.
"""

from typing import Callable, TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from .variables import MEDIUM_FONT_SIZE, MINIMUN_HEIGHT_BUTTON
from .utils import (is_num_or_dot, is_valid_number,
                    is_numeric_expression_or_void)

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
        self._initial_value = 0.0
        self._left: float = self._initial_value
        self._right: float = self._initial_value
        self._op: str | None = None
        self._eq_pressed: bool = False
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
        self.display.eq_pressed.connect(self._eq)
        self.display.delete_pressed.connect(self.display.backspace)
        self.display.clear_pressed.connect(self._clear)
        self.display.input_pressed.connect(self._insert_to_display)
        self.display.operator_pressed.connect(self._config_left_op)

        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not button_text:
                    continue

                if not is_num_or_dot(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._setconfig_special_button(button)
                else:
                    button.setProperty('cssClass', 'genericButton')

                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2)
                else:
                    self.addWidget(button, i, j)

                slot = self._make_slot(self._insert_to_display,
                                       button_text)

                self._connect_button_clicked(button, slot)

    def _setconfig_special_button(self, button: Button):
        text = button.text()

        if text == 'C':
            self._connect_button_clicked(button, self._clear)

        if text in '+-*/^':
            self._connect_button_clicked(button,
                                         self._make_slot(
                                             self._config_left_op, text))

        if text == '=':
            self._connect_button_clicked(button, self._eq)

        if text == '◀':
            self._connect_button_clicked(button, self.display.backspace)

    def _connect_button_clicked(self, button: Button, slot):
        """
        Connect the button to a slot.
        """

        button.clicked.connect(slot)

    def enable_or_desable_buttons(self, on_off: bool) -> None:
        """
        Enable or desable the buttons except for the 'C' button.
        """

        count = self.count()

        for index in range(count):
            layout_item = self.itemAt(index)
            button = layout_item.widget()

            if isinstance(button, Button) and button.text() != 'C':
                button.setEnabled(on_off)

    @Slot()
    def _make_slot(self, func: Callable, *args, **kwargs):
        @Slot()
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot

    @Slot(str)
    def _insert_to_display(self, text: str) -> None:
        new_value: str = self.display.text() + text

        if not is_valid_number(new_value):
            return
        self.display.insert(text)

    @Slot()
    def _clear(self) -> None:
        self._left = self._right = self._initial_value
        self._op = None
        self.equation = self._equation_initial_value
        self._eq_pressed = False
        self.display.clear()
        self.enable_or_desable_buttons(True)

    @Slot(str)
    def _config_left_op(self, text: str) -> None:
        button_text = text  # Operation

        display_text = self.display.text()

        self.display.clear()

        if not is_numeric_expression_or_void(display_text):
            return

        if display_text:
            self._left = float(display_text)
        self._op = button_text

        if self.equation == self._equation_initial_value or self._eq_pressed:
            self.equation = f' {self._left} {self._op}'

        elif self.equation != self._equation_initial_value and display_text:
            self.equation += f' {self._left} {self._op}'

        else:
            self.equation = self.equation[:-1] + self._op

        self._eq_pressed = False

    @Slot()
    def _eq(self):
        display_text = self.display.text()

        if not is_valid_number(display_text):
            return

        self._right = float(display_text)

        if self._op is None:
            self.equation = display_text

        elif not self._eq_pressed:
            self.equation += f' {str(self._right)}'

        else:
            self.equation += f' {self._op} {str(self._right)}'
        self.info.setText(self.equation + ' =')

        result = '0.0'
        try:
            # type: ignore
            result = str(eval(self.equation.replace('^', '**')))
            self.display.setText(result)
        except ZeroDivisionError:
            self.display.setText('Divisão por zero')
            self.enable_or_desable_buttons(False)
        except OverflowError:
            self.display.setText('Estouro')
            self.enable_or_desable_buttons(False)

        self._left = float(result)
        self._right = self._initial_value
        self._eq_pressed = True
