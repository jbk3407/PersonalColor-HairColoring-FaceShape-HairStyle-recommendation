from tkinter import *

window = Tk()
window.geometry('400x300')
window.title('PythonGuides')
window['bg'] = '#5d8a82'

f = ("Times bold", 14)


def nextPage():
    window.destroy()
    import page2

def prevPage():
    window.destroy()
    import page3


Label(
    window,
    text="This is First page",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    window,
    text="Previous Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Next Page",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

window.mainloop()