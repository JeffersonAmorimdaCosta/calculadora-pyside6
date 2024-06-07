"""
Module for styling the app.
"""

import qdarktheme  # type:ignore
from PySide6.QtWidgets import QApplication
from .variables import (PRIMARY_COLOR, DARKER_PRIMARY_COLOR,
                        DARKEST_PRIMARY_COLOR, GRAY_COLOR,
                        LIGHTER_PRIMARY_COLOR, WHITE_COLOR, LIGHT_GRAY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: {WHITE_COLOR};
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: {WHITE_COLOR};
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: {WHITE_COLOR};
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:disabled {{
        color: {LIGHT_GRAY_COLOR};
        background: {LIGHTER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="genericButton"]:disabled {{
        color: {LIGHT_GRAY_COLOR};
        background: {GRAY_COLOR};
    }}
"""


def setup_theme(app: QApplication, theme: str) -> None:
    """
    Param:
    app (QApplication): The app that will be styled.
    theme (str): The name of the theme to load.

    """
    app.setStyleSheet(qdarktheme.load_stylesheet(theme))
    app.setStyleSheet(app.styleSheet() + qss)
