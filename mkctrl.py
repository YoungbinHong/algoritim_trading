import pyautogui

if __name__ == '__main__':
    print(pyautogui.size())
    position = pyautogui.position()
    print(position.x, position.y)