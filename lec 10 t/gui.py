import tkinter

Window = tkinter.Tk()
Window.geometry("250x250+250+250")
Window.title("PRINT MY NAME")
i = 0
while i < 5:
    Window.grid_rowconfigure(i, minsize=20)
    Window.grid_columnconfigure(i, minsize=20)
    i += 1


def PrintName():
    print("mohamed")


def PrintoK():
    print("OK")


def Exit():
    exit()


B1 = tkinter.Button(Window, text="print", bg="blue", command=PrintName)
B1.grid(row=2, column=2)
B2 = tkinter.Button(Window, text="ok", bg="green", command=PrintoK)
B2.grid(row=4, column=6)
B3 = tkinter.Button(Window, text="exit", bg="red", command=Exit)
B3.grid(row=4, column=5)
Window.mainloop()
