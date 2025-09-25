import tkinter
import tkinter.font
import random

lotto_num = range(1,46)

def buttonClick():
    print(random.sample(lotto_num,6))
window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200")
window.resizable(False,False)
button = tkinter.Button(window, overrelief="solid",text="번호확인",width=30,command=buttonClick,repeatdelay=5000,repeatinterval=500)
button.pack()
window.mainloop()