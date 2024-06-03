import sys
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 50px')
    window.add_widget_to_vlayout(label1)

    window.adjust_fixed_size()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'CompanyName.ProductName.SubProduct.VersionInformation')

    window.show()
    app.exec()
