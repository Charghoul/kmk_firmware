import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [ MatrixScanner(
            # required arguments:
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            # optional arguments with defaults:
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=0.02,
            max_events=64
        ),
         RotaryioEncoder(
                pin_a=board.GP08,
                pin_b=board.GP09,
                # optional
                divisor=2,
            ),
        #correct way to add second encoder? 
        #both encoders have a click functionality, where to add that? 
        RotaryioEncoder(
                pin_a=board.GP20,
                pin_b=board.GP23,
                # optional
                divisor=2,
            )


        ]
    #updated rows and column pins and diode orientation to match qmk settings
    row_pins = (board.GP04, board.GP05, board.GP06, board.GP07)
    col_pins = (board.GP29, board.GP28, board.GP27, board.GP26, board.GP22)
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.TX
    i2c = board.I2C
    SCL=board.SCL
    SDA=board.SDA

    #copied from microdox keyboard (same layout), no idea what this does 
    # NOQA
    # flake8: noqa
    coord_mapping = [
     0,  1,  2,  3,  4,  24,23,22,21,20,
     5,  6,  7,  8,  9,  29,28,27,26,25,
    10, 11, 12, 13, 14,  34,33,32,31,30,
            17, 18, 19,  39, 38, 37,
    ]


#qmk waterfowl pinout
#define MATRIX_ROW_PINS { D4 -> GP04, C6 -> GP05, D7 -> GP06, E6 -> GP07}
#define MATRIX_COL_PINS { F4 -> GP29 F5 -> GP28 , F6 -> GP27 , F7 -> GP26, B1 ->GP22}
