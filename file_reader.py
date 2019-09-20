import pyautogui
import time


def rader(file_txt):
    with open(file_txt, 'r') as file:
        a = file.read()
        b = a.split(', ')

    return b


list_of_fish = rader('ryby.txt')

time.sleep(2)
for fish in list_of_fish:
    # time.sleep(1)
    pyautogui.typewrite(fish)
    pyautogui.hotkey('ENTER')
    pyautogui.typewrite('yes')
    pyautogui.hotkey('ENTER')
    pyautogui.typewrite('yes')
    pyautogui.hotkey('ENTER')