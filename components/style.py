"""
Module for styling the app.
"""

import qdarktheme
from PySide6.QtWidgets import QApplication
from .variables import (PRIMARY_COLOR, DARKER_PRIMARY_COLOR,
                        DARKEST_PRIMARY_COLOR)

qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
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
