"""
This module has the most used variables.
"""

from pathlib import Path

ROOT_FOLDER = Path(__file__).parent.parent
SRC_PATH = ROOT_FOLDER / 'src'
WINDOW_ICON_PATH = SRC_PATH / 'icon.png'
print(ROOT_FOLDER)

# Sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 16
TEXT_MARGIN = 15
MINIMUM_WIDTH = 400
MINIMUN_HEIGHT_BUTTON = 60

# Colors
PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'
