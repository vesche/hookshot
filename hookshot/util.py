
from mss import mss

def get_screenshot():
    with mss() as sct:
        return sct.grab(sct.monitors[0])
