from tkinter import *

root = Tk()

root.title("Dennis's Python GUI test")
root.geometry("500x500")

btn = Button(root, text= '1번 버튼')
btn.pack()
btn2 = Button(root, text= '2번 버튼')
btn2.pack()

root.mainloop()
