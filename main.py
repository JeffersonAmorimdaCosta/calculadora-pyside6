"""
Main module.
"""

import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from components import Display, Info, MainWindow, setup_theme, WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Estilizando
    setup_theme(app, 'light')

    # Info
    info = Info('12 x 87')
    window.add_widget_to_vlayout(info)

    # Display
    display = Display()
    window.add_widget_to_vlayout(display)

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'CompanyName.ProductName.SubProduct.VersionInformation')

    window.adjust_fixed_size()
    window.show()
    app.exec()
