import pyautogui
print(pyautogui.size())
x = 100
for i in range (5):  
    pyautogui.moveTo(x,500, duration = 0.25)
    x += 100
