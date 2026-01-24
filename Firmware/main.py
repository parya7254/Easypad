import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, SSD1306, TextEntry

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP27, board.GP28, board.GP29, board.GP0)
keyboard.row_pins = (board.GP3, board.GP4, board.GP2, board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())

rgb = RGB(pixel_pin=board.GP26, num_pixels=16)
keyboard.extensions.append(rgb)


i2c_bus = busio.I2C(board.GP7, board.GP6)
display_driver = SSD1306(
    i2c=i2c_bus,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Mode: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='COMBO', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='RGB', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='FUNC', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='0 1 2', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
    ],
    
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(display)


keyboard.modules.append(Macros())
L0= KC.DF(0)
L1= KC.DF(1)
L2= KC.DF(2)

COPY = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

PASTE = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
)

PASTENF = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.SHIFT),
    Tap(KC.V),
    Release(KC.SHIFT),
    Release(KC.LCTL)
)

CUT = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.X),
    Release(KC.LCTL)
)

UNDO = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Z),
    Release(KC.LCTL)
)
REDO = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.SHIFT),
    Tap(KC.Z),
    Release(KC.SHIFT),
    Release(KC.LCTL)
)

REDO2 = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Y),
    Release(KC.LCTL)
)

NEWTAB = KC.MACRO( 
    Press(KC.LCTL),
    Tap(KC.T),
    Release(KC.LCTL)
)

CLOSETAB = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.W),
    Release(KC.LCTL)
)

REOPENTAB = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.SHIFT),
    Tap(KC.T),
    Release(KC.SHIFT),
    Release(KC.LCTL)
)

CLOSEALLTAB = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.SHIFT),
    Tap(KC.W),
    Release(KC.SHIFT),
    Release(KC.LCTL)
)

SWITCHTABNEXT = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.TAB),
    Release(KC.LCTL)
)

SWITCHTABLAST = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.SHIFT),
    Tap(KC.TAB),
    Release(KC.SHIFT),
    Release(KC.LCTL)
)

keyboard.keymap = [
    # Layer 0
    [
        L1, COPY,    PASTE,    CUT,
        UNDO,   REDO,    PASTENF,    REDO2,
        NEWTAB,   CLOSETAB,    REOPENTAB,    CLOSEALLTAB,
        SWITCHTABNEXT,  SWITCHTABLAST,    KC.LALT,    KC.TAB,
    ],
    # Layer 1
    [
        L2,  KC.RGB_TOG,   KC.RGB_HUI,   KC.RGB_HUD,
        KC.RGB_SAI,  KC.RGB_SAD,   KC.RGB_VAI,   KC.RGB_VAD,
        KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,  KC.RGB_MODE_BREATHE_RAINBOW,  KC.RGB_MODE_RAINBOW,
        KC.RGB_MODE_BREATHE,KC.RGB_MODE_PLAIN, KC.RGB_ANI, KC.RGB_AND,
    ],
    # Layer 2
    [
        L0, KC.F1, KC.F2, KC.F3,
        KC.F4, KC.F5, KC.F6, KC.F7,
        KC.F8, KC.F9, KC.F10, KC.F11,
        KC.F12,KC.ENT, KC.SPC, KC.DEL,
    ],
]

if __name__ == '__main__':
    keyboard.go()