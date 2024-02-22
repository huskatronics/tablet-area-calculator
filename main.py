import pyautogui
import json
import time
from processor import process_result


def record_pointer_positions():
    # Record the screen coordinates of the pointer and saving them into a file
    cursor_positions = []
    while True:
        cursor_position = pyautogui.position()
        if cursor_position.x >= 0:
            cursor_positions.append([cursor_position.x, cursor_position.y])
            time.sleep(0.5)
        else:
            with open('storage.json', 'w') as f:
                json.dump(cursor_positions, f)
            break


if __name__ == '__main__':
    # countdown before the recording starts
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    record_pointer_positions()
    process_result()
