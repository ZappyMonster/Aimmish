# scroll down to the bottom to see the functions the dictionaries take a lot of lines

hex_to_key = {
    0x01: "Left Click",
    0x02: "Right Click",
    0x03: "Control-break processing",
    0x04: "Middle mouse button",
    0x05: "X1",
    0x06: "X2",
    0x08: "Backspace",
    0x09: "Tab",
    0x0C: "CLEAR",
    0x0D: "ENTER",
    0x10: "SHIFT",
    0x11: "CTRL",
    0x12: "ALT",
    0x13: "PAUSE",
    0x14: "CAPS LOCK",
    0x1B: "ESC",
    0x20: "SPACEBAR",
    0x21: "PAGE UP",
    0x22: "PAGE DOWN",
    0x23: "END",
    0x24: "HOME",
    0x25: "LEFT ARROW",
    0x26: "UP ARROW",
    0x27: "RIGHT ARROW",
    0x28: "DOWN ARROW",
    0x29: "SELECT",
    0x2A: "PRINT",
    0x2B: "EXECUTE",
    0x2C: "PRINT SCREEN",
    0x2D: "INS",
    0x2E: "DEL",
    0x2F: "HELP",
    0x30: "0",
    0x31: "1",
    0x32: "2",
    0x33: "3",
    0x34: "4",
    0x35: "5",
    0x36: "6",
    0x37: "7",
    0x38: "8",
    0x39: "9",
    0x41: "A",
    0x42: "B",
    0x43: "C",
    0x44: "D",
    0x45: "E",
    0x46: "F",
    0x47: "G",
    0x48: "H",
    0x49: "I",
    0x4A: "J",
    0x4B: "K",
    0x4C: "L",
    0x4D: "M",
    0x4E: "N",
    0x4F: "O",
    0x50: "P",
    0x51: "Q",
    0x52: "R",
    0x53: "S",
    0x54: "T",
    0x55: "U",
    0x56: "V",
    0x57: "W",
    0x58: "X",
    0x59: "Y",
    0x5A: "Z",
    0x5B: "Left Windows",
    0x5C: "Right Windows",
    0x5D: "Applications",
    0x60: "Numeric keypad 0",
    0x61: "Numeric keypad 1",
    0x62: "Numeric keypad 2",
    0x63: "Numeric keypad 3",
    0x64: "Numeric keypad 4",
    0x65: "Numeric keypad 5",
    0x66: "Numeric keypad 6",
    0x67: "Numeric keypad 7",
    0x68: "Numeric keypad 8",
    0x69: "Numeric keypad 9",
    0x6A: "Multiply",
    0x6B: "Add",
    0x6C: "Separator",
    0x6D: "Subtract",
    0x6E: "Decimal",
    0x6F: "Divide",
    0x70: "F1",
    0x71: "F2",
    0x72: "F3",
    0x73: "F4",
    0x74: "F5",
    0x75: "F6",
    0x76: "F7",
    0x77: "F8",
    0x78: "F9",
    0x79: "F10",
    0x7A: "F11",
    0x7B: "F12",
    0x90: "NUM LOCK",
    0x91: "SCROLL LOCK",
    0xA0: "Left SHIFT",
    0xA1: "Right SHIFT",
    0xA2: "Left CONTROL",
    0xA3: "Right CONTROL",
    0xA4: "Left ALT",
    0xA5: "Right ALT",
}

key_to_hex = {
    "Left Click": 0x01,
    "Right Click": 0x02,
    "Control-break processing": 0x03,
    "Middle mouse button": 0x04,
    "X1": 0x05,
    "X2": 0x06,
    "Backspace": 0x08,
    "Tab": 0x09,
    "CLEAR": 0x0C,
    "ENTER": 0x0D,
    "SHIFT": 0x10,
    "CTRL": 0x11,
    "ALT": 0x12,
    "PAUSE": 0x13,
    "CAPS LOCK": 0x14,
    "ESC": 0x1B,
    "SPACEBAR": 0x20,
    "PAGE UP": 0x21,
    "PAGE DOWN": 0x22,
    "END": 0x23,
    "HOME": 0x24,
    "LEFT ARROW": 0x25,
    "UP ARROW": 0x26,
    "RIGHT ARROW": 0x27,
    "DOWN ARROW": 0x28,
    "SELECT": 0x29,
    "PRINT": 0x2A,
    "EXECUTE": 0x2B,
    "PRINT SCREEN": 0x2C,
    "INS": 0x2D,
    "DEL": 0x2E,
    "HELP": 0x2F,
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    "A": 0x41,
    "B": 0x42,
    "C": 0x43,
    "D": 0x44,
    "E": 0x45,
    "F": 0x46,
    "G": 0x47,
    "H": 0x48,
    "I": 0x49,
    "J": 0x4A,
    "K": 0x4B,
    "L": 0x4C,
    "M": 0x4D,
    "N": 0x4E,
    "O": 0x4F,
    "P": 0x50,
    "Q": 0x51,
    "R": 0x52,
    "S": 0x53,
    "T": 0x54,
    "U": 0x55,
    "V": 0x56,
    "W": 0x57,
    "X": 0x58,
    "Y": 0x59,
    "Z": 0x5A,
    "Left Windows": 0x5B,
    "Right Windows": 0x5C,
    "Applications": 0x5D,
    "Numeric keypad 0": 0x60,
    "Numeric keypad 1": 0x61,
    "Numeric keypad 2": 0x62,
    "Numeric keypad 3": 0x63,
    "Numeric keypad 4": 0x64,
    "Numeric keypad 5": 0x65,
    "Numeric keypad 6": 0x66,
    "Numeric keypad 7": 0x67,
    "Numeric keypad 8": 0x68,
    "Numeric keypad 9": 0x69,
    "Multiply": 0x6A,
    "Add": 0x6B,
    "Separator": 0x6C,
    "Subtract": 0x6D,
    "Decimal": 0x6E,
    "Divide": 0x6F,
    "F1": 0x70,
    "F2": 0x71,
    "F3": 0x72,
    "F4": 0x73,
    "F5": 0x74,
    "F6": 0x75,
    "F7": 0x76,
    "F8": 0x77,
    "F9": 0x78,
    "F10": 0x79,
    "F11": 0x7A,
    "F12": 0x7B,
    "NUM LOCK": 0x90,
    "SCROLL LOCK": 0x91,
    "Left SHIFT": 0xA0,
    "Right SHIFT": 0xA1,
    "Left Control": 0xA2,
    "Right Control": 0xA3,
    "Left Alt": 0xA4,
    "Right Alt": 0xA5,
}


def print_key(value):
    return hex_to_key.get(value, "Unknown Keybind")

def get_keycode(keybind_description):
    lowercase_description = keybind_description.lower()
    for description, keycode in key_to_hex.items():
        if description.lower() == lowercase_description:
            return keycode
    return None
