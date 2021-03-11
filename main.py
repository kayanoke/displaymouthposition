import tkinter
import pyautogui

def repeat():
    x,y  = pyautogui.position()
    score['text'] = str(x) +', '+str(y)
    root.after(10,repeat)

root = tkinter.Tk()
score = tkinter.Label(text='0 , 0',font=('',15))
score.place(x=0, y=0)
xsize = 300
ysize = 40
root.attributes('-topmost',True)
root.geometry(str(xsize)+'x'+str(ysize))
root.after(10,repeat)
root.mainloop()
