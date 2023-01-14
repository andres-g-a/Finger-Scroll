import pyautogui

speed = input('Input speed: ')
sleepTime = input('Time until next scroll: ')

while True:

    pyautogui.time.sleep(3)

    pyautogui.scroll(int(speed))

    pyautogui.time.sleep(int(sleepTime))

